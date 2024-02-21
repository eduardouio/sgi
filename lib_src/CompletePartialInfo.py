from costings.models import Ledger
from filemanager.models import FileManager
from lib_src import CompleteOrderInfo
from lib_src.serializers import (ApportionmentDetailSerializer,
                                 ApportionmentSerializer, ExpenseSerializer,
                                 FileManagerSerializer,
                                 InfoInvoiceDetailSerializer,
                                 InfoInvoiceSerializer, LedgerSerializer,
                                 PaidInvoiceDetailSerializer,
                                 PaidInvoiceSerializer, PartialSerializer,
                                 SupplierSerializer)
from logs.app_log import loggin
from orders.models import OrderInvoiceDetail
from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from partials.models import (Apportionment, ApportionmentDetail, InfoInvoice,
                             InfoInvoiceDetail, Partial)
from suppliers.models import Supplier


class CompletePartialInfo(object):
    '''
        Return all information from parcial include order data and int Expenses
        etste es un ejemplo del comentario en el navegador
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
            'have_files' : False,
            'have_ice_reliquidado' : False
        }
        self.id_partial = None
        self.nro_order = None
        self.request = None
        self.partial_ledger = 0
        self.serialized = False
        self.tributes = None
        self.total_expenses = 0
        self.total_invoiced = 0
        self.total_provisions = 0
        self.type_change_trimestral = 0
        self.partial_isclosed = False


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
            'Iniciando clase de recuperacion informacion parcial {} serializado {} '
            .format(id_partial, serialized) 
            )
        self.id_partial  = id_partial
        self.serialized = serialized
        self.type_change_trimestral = type_change_trimestral
        partial = self.get_partial()

        if partial is None:
            return None

        ledger = self.get_ledger()

        return ({
            'partial': partial,
            'info_invoice': self.get_info_invoice(),
            'expenses':self.get_expenses(),
            'ledger' : ledger,
            'apportiomen' : self.get_apportioment(),
            'ice_reliquidado' : self.get_ice_reliquidated(partial, ledger),
            'status' : self.status_parcial,
            'taxes' : self.get_taxes(),
            'files' : self.get_files(),
            'total_expenses' : self.total_expenses,
            'total_invoiced' : (self.partial_ledger + self.total_invoiced),
            'total_taxes_product' : self.partial_ledger,
            'total_provisions' : self.total_provisions,
            })

    def get_ice_reliquidated(self, partial, ledger):
        """Retorna el valor del ice reliquidado en el sistema, 
        solo para parciales cerrados
        """
        if self.serialized:
            return None

        if bool(partial.bg_isclosed):
            self.status_parcial['have_ice_reliquidado'] = True
            
            ice_reliquidado = {
                'expense' : 'ICE ADVALOREM RELIQUIDADO',
                'provision' : ledger.reliquidacion_ice,
                'invoiced_value' : 0,
                'legder' : 0,
            }

            if ledger.bg_mayor:
                ice_reliquidado['ledger'] = ledger.reliquidacion_ice
                ice_reliquidado['invoiced_value'] = ledger.reliquidacion_ice

            return ice_reliquidado
            
        return None


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
                + partial.fodinfa_pagado)

        self.partial_ledger += self.tributes['total']
        self.partial_isclosed = partial.bg_isclosed

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
            'items' : partial_items['info_invoice_details'].count(),
            'boxes' : 0,
            'value' : 0,
            'value_tct' : 0,
            'bottles' : 0,
        }

        if partial_items['info_invoice_details']:
            self.status_parcial['info_invoice_details'] = True
            self.status_parcial['info_invoice'] = True

        for line_item in partial_items['info_invoice_details']:
            partial_items['totals']['boxes'] += line_item.nro_cajas
            order_ivoice_detail = OrderInvoiceDetail.get_by_id(line_item.detalle_pedido_factura_id)
            partial_items['totals']['bottles'] += (line_item.nro_cajas * order_ivoice_detail.cod_contable.cantidad_x_caja)
            partial_items['totals']['value'] += (line_item.nro_cajas * order_ivoice_detail.costo_caja)
            partial_items['totals']['value_tct'] += (line_item.nro_cajas * order_ivoice_detail.costo_caja * self.type_change_trimestral)

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
                #'complete' : (partial_items['info_invoice'].valor != partial_items['totals']['value']),
                'complete' : True
            }

        return partial_items

    def get_expenses(self):
        data_expenses = []
        expenses = Expense.get_by_parcial(self.id_partial)

        if expenses is None:
            return None
        
        self.status_parcial['expenses'] = True
        self.status_parcial['partial_expenses'] = True

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
            self.total_expenses += item.valor_provisionado
            self.total_invoiced +=  item.invoiced_value
            item.sale = (item.valor_provisionado - item.invoiced_value)
            self.total_provisions += item.sale 

            if self.serialized:
                expense_serializer = ExpenseSerializer(item)
                paids_serialized = []

                for p in paids:
                    paid_serializer = PaidInvoiceDetailSerializer(p['paid'])
                    invoice_serializer = PaidInvoiceSerializer(p['invoice'])
                    supplier_serializer = SupplierSerializer(p['supplier'])
                    paids_serialized.append({
                        'paid' : paid_serializer.data,
                        'invoice' : invoice_serializer.data,
                        'supplier': supplier_serializer.data,
                        })

                data_expenses.append({
                    'expense' : expense_serializer.data,
                    'paids' : paids_serialized,
                    'invoiced_value' : item.invoiced_value,
                    'sale' : item.sale,
                    'legder' : item.ledger,
                    'parcial' : (bool(item.sale) and (item.sale != item.valor_provisionado)),
                    'provision' : (item.sale == item.valor_provisionado),
                    'complete' : bool(item.bg_closed),
                })

        if self.serialized:
            return data_expenses

        return expenses


    def get_apportioment(self):
        apportionment = Apportionment.get_by_parcial(self.id_partial)
        
        if apportionment is None:
            loggin('w','Este parcial {} no tiene prorrateos'. format(self.id_partial))
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


    def get_taxes(self):
        return Partial.get_paid_taxes(self.id_partial)

    
    def get_ledger(self):
        ''' Recupera el mayor del Parcial solo si esta cerrado'''
        if self.partial_isclosed == False:
            loggin('w', 'Parcial abierto no tiene mayor parcial {}'
            .format(self.id_partial))
            return None
        ledger =  Ledger.get_by_parcial(self.id_partial)
        
        loggin('i', 'Mayor parcial recuperado')
        if self.serialized:
            ledger_serializer = LedgerSerializer(ledger)
            loggin('i', 'Retornando mayor del parcial')
            return ledger_serializer.data

        return ledger
    

    def get_files(self):
        '''Obtiene los archivos relacionados con el Parcial'''
        files = FileManager.get_by_model_id(
            app_label='partials', 
            model_name= 'Partial',
            id_row = self.id_partial
            )
            
        if isinstance(files, list):
            loggin(
                'w', 
                'El parcial {} no tiene archivos relacionados'
                .format(self.id_partial)
            )
        
            return None

        self.status_parcial['have_files'] = True

        if self.serialized:
            file_serializer = FileManagerSerializer(files, many=True)
            return file_serializer.data
        
        return files