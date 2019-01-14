from costings.models.Ledger import Ledger
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.serializers import ApportionmentDetailSerializer, \
    ApportionmentSerializer, ExpenseSerializer, InfoInvoiceDetailSerializer, \
    InfoInvoiceSerializer, LedgerSerializer, PaidInvoiceDetailSerializer, \
    PaidInvoiceSerializer, PartialSerializer, SupplierSerializer
from logs.app_log import loggin
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from paids.models.Expense import Expense
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail
from partials.models.Apportionment import Apportionment
from partials.models.ApportionmentDetail import ApportionmentDetail
from partials.models.InfoInvoice import InfoInvoice
from partials.models.InfoInvoiceDetail import InfoInvoiceDetail
from partials.models.Partial import Partial
from suppliers.models.Supplier import Supplier


class CompleteParcialInfo(object):
    '''
        Return all information from parcial include order data and int Expenses
    '''
    def __init__(self):
        self.status_parcial = {
            'parial' : False,
            'info_invoice' : False,
            'info_invoice_details' : False,
            'apportioment' : False,
            'apportioment_detail' : False,
            'partial_expenses' : False,
            'ledger' : False,
            'taxes' : False,
        }
        self.id_partial = None
        self.nro_order = None
        self.request = None
        self.init_ledger = 0
        self.partial_ledger = 0
        self.serialized = False
        self.tributes = None
        self.total_expenses = 0
        self.total_invoiced = 0
        self.total_provisions = 0
        self.type_change_trimestral = 0


    def get_data(self, id_partial, serialized = False, type_change_trimestral=1):
        """
        Returns all data of parcial
        Args:
        id_partial (int) : identificador del parcial a consultar
        serialized (bool) : modo retorno data dict | object
        request (Request) : información de sesion de usuario
        type_change_trimestral: tipo de cambio trimestral de un parcial

        Returns:
            dic | object : informacion completa
        """
        loggin(
            'i',
            'Iniciando clase de recuperacion informacion parcial {}'
            .format(id_partial)
            )
        self.id_partial  = id_partial
        self.serialized = serialized
        self.type_change_trimestral = type_change_trimestral

        return ({
            'partial': self.get_partial(),
            'info_invoice': self.get_info_invoice(),
            'expenses':self.get_expenses(),
            'ledger' : self.get_ledger(),
            'apportiomen' : self.get_apportioment(),
            'status' : self.status_parcial,
            'prorrateos' : {},
            })


    def get_partial(self):
        partial = Partial.get_by_id(self.id_partial)
        self.tributes = {
            'exoneracion' : 0,
            'arancel_advalorem' : 0,
            'arancel_especifico' : 0,
            'fondinfa' : 0,
            'ice_advalorem' : 0,
            'ice_especifico' : 0,
            'total' : 0,
        }

        if partial is None:
            return None

        if partial.bg_isliquidated:
            self.status_parcial['taxes'] = True
            self.tributes['arancel_advalorem'] = partial.arancel_advalorem_pagar_pagado
            self.tributes['arancel_especifico'] = partial.arancel_especifico_pagar_pagado
            self.tributes['fondinfa'] = partial.fodinfa_pagado
            self.tributes['ice_especifico'] = partial.ice_especifico_pagado
            self.tributes['ice_advalorem'] = partial.ice_advalorem_pagado

            self.tributes['total'] = (
                partial.arancel_advalorem_pagar_pagado
                + partial.arancel_especifico_pagar_pagado
                + partial.ice_especifico_pagado
                + partial.ice_advalorem_pagado
                + partial.fodinfa_pagado
            )

        self.partial_ledger += self.tributes['total']

        if self.serialized:
            partia_serializer = PartialSerializer(partial)
            return partia_serializer.data

        return partial


    def get_info_invoice(self):
        partial_items = {
            'info_invoice' : None,
            'supplier' : None,
            'info_invoice_details' : None,
            'totals' : None,
        }

        info_invoice = InfoInvoice.get_by_id_partial(self.id_partial)

        if info_invoice is None:
            return None 
        
        self.status_parcial['info_invoice'] = True
        partial_items['info_invoice'] = info_invoice
        partial_items['info_invoice_details'] = InfoInvoiceDetail.get_by_info_invoice(info_invoice.id_factura_informativa)
        partial_items['supplier'] = Supplier.get_by_ruc(info_invoice.identificacion_proveedor_id)
        partial_items['totals'] = {
            'items' : int(partial_items['info_invoice_details'].count()),
            'boxes' : 0,
            'value' : 0,
            'bottles' : 0,
        }

        if partial_items['info_invoice_details']:
            self.status_parcial['info_invoice_details'] = True
        
        for line_item in partial_items['info_invoice_details']:
            partial_items['totals']['boxes'] += line_item.nro_cajas
            order_ivoice_detail = OrderInvoiceDetail.get_by_id(line_item.detalle_pedido_factura_id)
            partial_items['totals']['bottles'] += (line_item.nro_cajas * order_ivoice_detail.cod_contable.cantidad_x_caja)
            partial_items['totals']['value'] += (line_item.nro_cajas * order_ivoice_detail.costo_caja)
        
        self.partial_ledger += (partial_items['totals']['value'] * self.type_change_trimestral)

        if self.serialized:
            info_invoice_serializer = InfoInvoiceSerializer(partial_items['info_invoice'])
            info_invoice_details_serializer = InfoInvoiceDetailSerializer(partial_items['info_invoice_details'], many=True)
            supplier_serializer = SupplierSerializer(partial_items['supplier'])

            return {
                'info_invoice' : info_invoice_serializer.data,
                'info_invoice_detail' : info_invoice_details_serializer.data,
                'supplier' : supplier_serializer.data,
                'info_invoice_detail_sums' : partial_items['totals'],
                'parcial' : False,
                'provision' : (partial_items['info_invoice'].valor != partial_items['totals']['value']),
                'complete' : (partial_items['info_invoice'].valor != partial_items['totals']['value']),
            }

        
        return partial_items


    def get_expenses(self):
        data_expenses = []
        expenses = Expense.get_by_parcial(self.id_partial)
        
        if expenses is None:
            return None
        self.status_parcial['expenses'] = True

        for item in expenses:
            paids = []
            item.paids = PaidInvoiceDetail.get_by_expense(item)
            item.invoiced_value = 0
            item.ledger = 0

            for paid in item.paids:
                item.invoiced_value += paid.valor
                paid.invoice = PaidInvoice.get_by_id(paid.id_documento_pago_id)
                paid.supplier = Supplier.get_by_ruc(paid.invoice.identificacion_proveedor_id)

                paids.append(
                    {
                        'paid' : paid,
                        'invoice' : paid.invoice,
                        'supplier': paid.supplier,
                    }
                )

                if paid.bg_mayor == 1:
                    item.ledger += paid.valor

            item.sale = (item.valor_provisionado - item.invoiced_value)

            if self.serialized:
                expense_serializer = ExpenseSerializer(item)
                paids_serialized = []

                for p in paids:
                    paid_serializer = PaidInvoiceDetailSerializer(p['paid'])
                    invoice_serializer = PaidInvoiceSerializer(p['invoice'])
                    supplier_serializer = SupplierSerializer(p['supplier'])
                    paids_serialized.append(
                        {
                        'paid' : paid_serializer.data,
                        'invoice' : invoice_serializer.data,
                        'supplier': supplier_serializer.data,
                        }
                    )

                data_expenses.append({
                    'expense' : expense_serializer.data,
                    'paids' : paids_serialized,
                    'invoiced_value' : item.invoiced_value,
                    'sale' : item.sale,
                    'legder' : item.ledger,
                })

        if self.serialized:
            return data_expenses

        return expenses


    def get_apportioment(self):
        apportionment = Apportionment.get_by_parcial(self.id_partial)
        if apportionment is None:
            return None

        self.status_parcial['apportioment'] = True        

        apportionment.apportionment_detail = ApportionmentDetail.get_by_apportionment(apportionment.id_prorrateo)
        if apportionment.apportionment_detail:

            self.status_parcial['apportioment_detail'] = True

        if self.serialized:
            apportionment_serializer = ApportionmentSerializer(apportionment)
            apportionment_detail_serializer = ApportionmentDetailSerializer(apportionment.apportionment_detail, many=True)

            return {
                'apportioment': apportionment_serializer.data,
                'apportionment_detail' : apportionment_detail_serializer.data
            }

        return apportionment


    def get_ledger(self):
        pass