import decimal

import partials
from costings.models.Ledger import Ledger
from lib_src.serializers import (ApportionmentSerializer, ExpenseSerializer,
                                 LedgerSerializer,
                                 OrderInvoiceDetailSerializer,
                                 OrderInvoiceSerializer, OrderSerializer,
                                 PaidInvoiceDetailSerializer,
                                 PaidInvoiceSerializer, PartialSerializer,
                                 RateExpenseSerializer, SupplierSerializer)
from logs.app_log import loggin
from orders.models.Order import Order
from orders.models.OrderInvoice import OrderInvoice
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from paids.models.Expense import Expense
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail
from paids.models.RateExpense import RateExpense
from partials.models.Apportionment import Apportionment
from partials.models.Partial import Partial
from suppliers.models.Supplier import Supplier


class CompleteOrderInfo(object):
    ''' 
    Obtiene la informacion completa de in pedido
        Gastos iniciales a detalle
        listado de parciales
    '''

    def __init__(self):
        self.status_order = {
            'order' : True,
            'order_invoice' : False,
            'order_invoice_details' : False,
            'init_expenses' : False,
            'ledger' : False,
            'taxes' : False
        }

        self.request = None
        self.init_ledger = 0
        self.serialized = False
        self.nro_order = None
        self.tributes = None
        self.total_expenses = 0
        self.total_invoiced = 0
        self.total_provisions = 0
        self.tipo_cambio_trimestral = 1
        self.incoterm = None
        self.last_apportionment = None 


    def get_data(self, nro_order, serialized=False, request=None):
        '''
        [summary]
        retorna la informacion del pedido luego de acceder a las base de datos

        Arguments:
            nro_order {string} -- Nro de pedido
        
        Keyword Arguments:
            serialized {bool} -- indica si el resultado es serializado (default: {False})
            request {http-request} -- django session object (default: {None})
        
        Returns:
            [type] -- [description]
        '''
        self.nro_order = nro_order
        self.serialized = serialized
        self.request = request
        loggin(
            'i',
            'Recopilacion de informacion completa del pedido {nro_order}'
            .format(nro_order = self.nro_order),
            self.request
            )
        order  = self.get_order()

        if order is None:
            return None

        return {
            'order': order,
            'order_invoice':self.get_order_invoice(),
            'tipo_cambio_trimestral': self.tipo_cambio_trimestral, 
            'expenses':self.get_expenses(),
            'taxes' : self.get_taxes(),
            'ledger' : self.get_ledger(),
            'partials' : self.get_partials(),
            'status' : self.status_order,
            'tributes' : self.tributes,
            'init_ledger' : self.init_ledger,
            'total_expenses' : (self.total_expenses + self.init_ledger),
            'init_expenses' : self.total_expenses,
            'total_invoiced' : self.total_invoiced + self.init_ledger,
            'total_provisions' : self.total_provisions,
            'last_apportionment' : self.last_apportionment,
            }


    def get_order(self):
        order = Order.get_by_order(nro_order=self.nro_order)
        self.tributes = {
            'exoneracion' : 0,
            'arancel_advalorem' : 0,
            'arancel_especifico' : 0,
            'fondinfa' : 0,
            'ice_advalorem' : 0,
            'ice_especifico' : 0,
            'total' : 0,
        }

        if order is None:
            self.status_order['order'] = False
            return None

        self.incoterm = order.incoterm
        
        if order.regimen == '10' and order.bg_isliquidated == 1 :
            self.status_order['taxes'] = True
            self.tributes['arancel_advalorem'] = order.arancel_advalorem_pagar_pagado
            self.tributes['arancel_especifico'] = order.arancel_especifico_pagar_pagado
            self.tributes['fondinfa'] = order.fodinfa_pagado
            self.tributes['ice_advalorem'] = order.ice_especifico_pagado
            self.tributes['ice_especifico'] = order.ice_advalorem_pagado

            self.tributes['total'] = (
                        + (order.arancel_advalorem_pagar_pagado)
                        + (order.arancel_especifico_pagar_pagado)
                        + (order.fodinfa_pagado)
                        + (order.ice_especifico_pagado)
                        + (order.ice_advalorem_pagado)
            )
        elif order.regimen == '70':
            self.status_order['taxes'] = True

        self.init_ledger += self.tributes['total']

        if self.serialized:
            order_serializer = OrderSerializer(order)
            return order_serializer.data

        return order


    def get_order_invoice(self):
        order_items = {
            'order_invoice' : None,
            'supplier' : None,
            'order_invoice_details' : None,
            'totals' : None,
        }

        order_invoice = OrderInvoice.get_by_order(self.nro_order)

        if order_invoice is None:
            return None

        self.tipo_cambio_trimestral = order_invoice.tipo_cambio
        self.status_order['order_invoice'] = True
        order_items['order_invoice'] = order_invoice
        order_items['order_invoice_details'] = OrderInvoiceDetail.get_by_id_order_invoice(order_invoice.id_pedido_factura)
        order_items['supplier'] = Supplier.get_by_ruc(order_invoice.identificacion_proveedor_id)
        order_items['totals'] = {
            'items' : int(order_items['order_invoice_details'].count()),
            'boxes' : 0,
            'value' : 0,
            'bottles' : 0,
        }

        if order_items['order_invoice_details']:
            self.status_order['order_invoice_details'] = True

        for line_item in order_items['order_invoice_details']:
            order_items['totals']['bottles'] += (line_item.nro_cajas * line_item.cod_contable.cantidad_x_caja)
            order_items['totals']['boxes'] += line_item.nro_cajas
            order_items['totals']['value']  += (line_item.nro_cajas * line_item.costo_caja)
            self.init_ledger  += (line_item.nro_cajas * line_item.costo_caja) * order_invoice.tipo_cambio

        if self.serialized:
            order_invoice_serializer = OrderInvoiceSerializer(order_items['order_invoice'])
            order_invoice_det_serializer = OrderInvoiceDetailSerializer(order_items['order_invoice_details'],many=True)
            supplier_serializer = SupplierSerializer(order_items['supplier'])

            return {
                'order_invoice' : order_invoice_serializer.data,
                'supplier' : supplier_serializer.data,
                'order_invoice_detail' : order_invoice_det_serializer.data,
                'order_invoice_detail_sums' : order_items['totals'],
                'parcial' : False,
                'provision' : (order_items['order_invoice'].valor != order_items['totals']['value']),
                'complete' : (order_items['order_invoice'].valor == order_items['totals']['value'])
            }

        return order_items


    def get_expenses(self):
        data_expenses = []
        expenses = Expense.get_all_by_order(self.nro_order)

        if expenses.count() == 0:
            return expenses

        self.status_order['init_expenses'] = True
        for item in expenses:
            paids = []
            item.paids = PaidInvoiceDetail.get_by_expense(item)
            item.invoiced_value = 0
            item.ledger = 0
            self.total_expenses += item.valor_provisionado

            if item.concepto == 'ISD':
                #se usa para mostrar el gasto en la app Vue
                item.invoiced_value = item.valor_provisionado
                item.ledger = item.valor_provisionado
                self.total_invoiced += item.valor_provisionado
                item.bg_closed = 1
                item.paids = []

            
            if item.concepto == 'FLETE' and self.incoterm == 'CFR':
                #El flete de los CFRS se registran como pagados
                item.invoiced_value = item.valor_provisionado
                item.ledger = item.valor_provisionado
                self.total_invoiced += item.valor_provisionado
                item.bg_closed = 1
                item.paids = []

            for paid in item.paids:
                self.total_invoiced += paid.valor
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
            self.total_provisions += item.sale

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
                    'parcial' : (bool(item.sale) and (item.sale != item.valor_provisionado)),
                    'provision' : (item.sale == item.valor_provisionado),
                    'complete' : bool(item.bg_closed),
                })

        if self.serialized:
            return data_expenses

        return expenses


    def get_ledger(self):
        '''Return last ledger from order'''
        return None
        order = Order.get_by_order(self.nro_order)
        if order is None or order.bg_isclosed == 0:
            loggin(
            'w',
            'No se puede retornar el mayor del pedido {} abierto o inexistente'
            .format(self.nro_order)
            )
            return None

        ledger = Ledger().get_by_order(self.nro_order)

        if self.serialized and ledger:
            ledger_serializer = LedgerSerializer(ledger, many=True)
            return ledger_serializer.data

        return ledger


    def get_taxes(self):
        taxes =  Order.get_paid_taxes(self.nro_order)
        return taxes
    
    
    def get_partials(self):
        partials = Partial.get_by_order(self.nro_order)
        if partials.count() == 0:
            return None
        
        last_partial = Partial.get_last_close_partial(self.nro_order)
        
        if last_partial:
            last_apportionment = Apportionment.get_by_parcial(last_partial.id_parcial)
            if self.serialized:
                apportioment_serializer = ApportionmentSerializer(last_apportionment)
                self.last_apportionment = apportioment_serializer.data
            else:
                self.last_apportionment = last_apportionment

        if self.serialized:
            partial_serializer = PartialSerializer(partials, many=True)
            return partial_serializer.data
        
        return partials
