import decimal

from costings.models import Ledger
from lib_src.serializers import (ApportionmentSerializer, ExpenseSerializer,
                                 LedgerSerializer,
                                 OrderInvoiceDetailSerializer,
                                 OrderInvoiceSerializer, OrderSerializer,
                                 PaidInvoiceDetailSerializer,
                                 PaidInvoiceSerializer, PartialSerializer,
                                 RateExpenseSerializer, SupplierSerializer)
from logs import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from paids.models import Expense, PaidInvoice, PaidInvoiceDetail, RateExpense
from partials.models import (Apportionment, InfoInvoice, InfoInvoiceDetail,
                             Partial)
from suppliers.models.Supplier import Supplier


class CompleteOrderInfo(object):
    ''' 
    Obtiene la informacion completa de in pedido
        Gastos iniciales a detalle
        listado de parciales
    '''

    def __init__(self):
        self.status_order = {
            'order': True,
            'order_invoice': False,
            'order_invoice_details': False,
            'init_expenses': False,
            'ledger': False,
            'taxes': False
        }

        self.request = None
        self.init_ledger = 0
        self.serialized = False
        self.nro_order = None
        self.tributes = None
        self.origin_expeses_tct = 0
        self.total_expenses = 0
        self.total_invoiced = 0
        self.total_provisions = 0
        self.tipo_cambio_trimestral = 1
        self.incoterm = None
        self.etiquetas_fiscales = 0
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
            [dict] : Diccionario con toda la informacion del pedido
                    sin tomar en cuenta los parciales 
        '''
        self.nro_order = nro_order
        self.serialized = serialized
        self.request = request
        loggin('i', 'Informacion pedido {}'.format(
            self.nro_order), self.request)
        order = self.get_order()

        if order is None:
            return None

        return {
            'order': order,
            'order_invoice': self.get_order_invoice(),
            'tipo_cambio_trimestral': self.tipo_cambio_trimestral,
            'expenses': self.get_expenses(),
            'taxes': self.get_taxes(),
            'ledger': self.get_ledger(),
            'partials': self.get_partials(),
            'partials_details': self.get_partial_details(),
            'status': self.status_order,
            'tributes': self.tributes,
            'init_ledger': self.init_ledger,
            'total_expenses': (self.total_expenses + self.init_ledger),
            'etiquetas_fiscales': self.etiquetas_fiscales,
            'init_expenses': self.total_expenses,
            'origin_expenses_tct': (self.origin_expeses_tct 
                                            * self.tipo_cambio_trimestral),
            'total_invoiced': self.total_invoiced + self.init_ledger,
            'total_provisions': self.total_provisions,
            'last_apportionment': self.last_apportionment,
        }

    def get_order(self):
        order = Order.get_by_order(nro_order=self.nro_order)
        if order is None:
            self.status_order['order'] = False
            return None

        self.tributes = {
            'exoneracion': 0,
            'arancel_advalorem': 0,
            'arancel_especifico': 0,
            'fondinfa': 0,
            'ice_advalorem': 0,
            'ice_especifico': 0,
            'total': 0,
        }

        self.incoterm = order.incoterm

        if order.regimen == '10' and order.bg_isliquidated == 1:
            self.status_order['taxes'] = True
            self.tributes['arancel_advalorem'] = order.arancel_advalorem_pagar_pagado
            self.tributes['arancel_especifico'] = order.arancel_especifico_pagar_pagado
            self.tributes['fondinfa'] = order.fodinfa_pagado
            self.tributes['ice_especifico'] = order.ice_especifico_pagado
            self.tributes['ice_advalorem'] = order.ice_advalorem_pagado

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
        if order.incoterm == 'FOB':
            self.origin_expeses_tct = order.gasto_origen

        if self.serialized:
            order_serializer = OrderSerializer(order)
            return order_serializer.data

        return order

    def get_order_invoice(self):
        order_items = {
            'order_invoice': None,
            'supplier': None,
            'order_invoice_details': None,
            'totals': None,
        }

        order_invoice = OrderInvoice.get_by_order(self.nro_order)

        if order_invoice is None:
            return None

        self.tipo_cambio_trimestral = order_invoice.tipo_cambio
        self.status_order['order_invoice'] = True
        order_items['order_invoice'] = order_invoice
        order_items['order_invoice_details'] = OrderInvoiceDetail.get_by_id_order_invoice(
            order_invoice.id_pedido_factura)
        order_items['supplier'] = Supplier.get_by_ruc(
            order_invoice.identificacion_proveedor_id)
        order_items['totals'] = {
            'items': order_items['order_invoice_details'].count(),
            'boxes': 0,
            'value': 0,
            'value_tct': 0,
            'bottles': 0,
        }

        if order_items['order_invoice_details']:
            self.status_order['order_invoice_details'] = True
            for line_item in order_items['order_invoice_details']:
                order_items['totals']['bottles'] += (
                    line_item.nro_cajas * line_item.cod_contable.cantidad_x_caja)
                order_items['totals']['boxes'] += line_item.nro_cajas
                order_items['totals']['value'] += (
                    line_item.nro_cajas * line_item.costo_caja)
                order_items['totals']['value_tct'] += (
                    line_item.nro_cajas * line_item.costo_caja) * order_invoice.tipo_cambio
                self.init_ledger += (line_item.nro_cajas *
                                     line_item.costo_caja) * order_invoice.tipo_cambio

        if self.serialized:
            order_invoice_serializer = OrderInvoiceSerializer(
                order_items['order_invoice'])
            order_invoice_det_serializer = OrderInvoiceDetailSerializer(
                order_items['order_invoice_details'], many=True)
            supplier_serializer = SupplierSerializer(order_items['supplier'])

            return {
                'order_invoice': order_invoice_serializer.data,
                'supplier': supplier_serializer.data,
                'order_invoice_detail': order_invoice_det_serializer.data,
                'order_invoice_detail_sums': order_items['totals'],
                'parcial': False,
                'provision': (order_items['order_invoice'].valor != order_items['totals']['value']),
                'complete': (order_items['order_invoice'].valor == order_items['totals']['value'])
            }

        return order_items

    def get_expenses(self):
        data_expenses = []
        expenses = Expense.get_all_by_order(self.nro_order)

        if not expenses:
            return expenses

        if expenses.count() == 0:
            return expenses

        self.status_order['init_expenses'] = True
        for item in expenses:
            item.paids = PaidInvoiceDetail.get_by_expense(item)
            item.invoiced_value = 0
            item.ledger = 0
            self.total_expenses += item.valor_provisionado

            if item.concepto == 'ISD':
                # se usa para mostrar el gasto en la app Vue
                item.invoiced_value = item.valor_provisionado
                item.ledger = item.valor_provisionado
                self.total_invoiced += item.valor_provisionado
                item.bg_closed = 1
                item.paids = []

            if item.concepto == 'FLETE' and self.incoterm == 'CFR':
                # El flete de los CFRS se registran como pagados
                item.invoiced_value = item.valor_provisionado
                item.ledger = item.valor_provisionado
                self.total_invoiced += item.valor_provisionado
                item.bg_closed = 1
                item.paids = []

            if item.concepto == 'ETIQUETAS FISCALES':
                self.etiquetas_fiscales = item.valor_provisionado

            paids = []
            for paid in item.paids:
                self.total_invoiced += paid.valor
                item.invoiced_value += paid.valor
                paid.invoice = PaidInvoice.get_by_id(paid.id_documento_pago_id)
                paid.supplier = Supplier.get_by_ruc(
                    paid.invoice.identificacion_proveedor_id)

                paids.append({
                    'paid': paid,
                    'invoice': paid.invoice,
                    'supplier': paid.supplier,
                })

                if paid.bg_mayor == 1:
                    item.ledger += paid.valor

            item.sale = (item.valor_provisionado - item.invoiced_value)
            if item.sale < 0:
                loggin('e', 'Gasto {} con saldo negativo'.format(
                    item), self.request)

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
                            'paid': paid_serializer.data,
                            'invoice': invoice_serializer.data,
                            'supplier': supplier_serializer.data,
                        }
                    )

                data_expenses.append({
                    'expense': expense_serializer.data,
                    'paids': paids_serialized,
                    'invoiced_value': item.invoiced_value,
                    'sale': item.sale,
                    'legder': item.ledger,
                    'parcial': (bool(item.sale) and (item.sale != item.valor_provisionado)),
                    'provision': (item.sale == item.valor_provisionado),
                    'complete': bool(item.bg_closed),
                })

        if self.serialized:
            return data_expenses

        return expenses

    def get_ledger(self):
        '''
            Retorna el mayor de un pedido desde la base de datos del sistema
        '''
        order = Order.get_by_order(self.nro_order)
        if order is None or order.bg_isclosed == 0:
            loggin('w', 'pedido {} abierto o inexistente'.format(self.nro_order),
                   self.request)
            return None

        ledger = Ledger().get_by_order(self.nro_order)

        if self.serialized and ledger:
            ledger_serializer = LedgerSerializer(ledger)
            return ledger_serializer.data

        return ledger

    def get_taxes(self):
        taxes = Order.get_paid_taxes(self.nro_order)
        return taxes

    def get_partials(self):
        partials = Partial.get_by_order(self.nro_order)
        if partials.count() == 0:
            return None

        if self.serialized:
            partial_serializer = PartialSerializer(partials, many=True)
            return partial_serializer.data

        return partials

    def get_partial_details(self):
        """
        Retorna informacion consolidad de un parcial, obtiene los datos de la
        factura informativa y sus totales
        """
        partials = Partial.get_by_order(self.nro_order)
        if partials.count() == 0:
            return None

        partials_details = []

        for partial in partials:
            item_data = {
                'id_parcial': partial.id_parcial,
                'nro_refrendo': None,
                'ordial_parcial': partial.ordinal_parcial,
                'fecha_llegada_cliente': partial.fecha_llegada_cliente,
                'fecha_salida_autorizada_almagro': partial.fecha_salida_autorizada_almagro,
                'nro_liquidacion': partial.nro_liquidacion,
                'tipo_cambio': partial.tipo_cambio,
                'bg_isclosed': partial.bg_isclosed,
                'bg_isliquidated': partial.bg_isliquidated,
                'id_factura_informativa': None,
                'nro_factura_informativa': None,
                'moneda': None,
                'nro_cajas': 0,
                'valor_total': 0,
            }

            info_invoice = InfoInvoice.get_by_id_partial(partial.id_parcial)

            if info_invoice:
                item_data['id_factura_informativa'] = (
                    info_invoice.id_factura_informativa
                    )
                item_data['nro_factura_informativa'] = (
                    info_invoice.nro_factura_informativa
                    )
                item_data['nro_refrendo'] = info_invoice.nro_refrendo
                item_data['moneda'] = info_invoice.moneda

            totals_detail = InfoInvoiceDetail.get_totals(partial.id_parcial)

            if totals_detail:
                item_data['nro_cajas'] = totals_detail['nro_cajas']
                item_data['valor_total'] = totals_detail['valor_total']

            partials_details.append(item_data)

        last_partial = Partial.get_last_close_partial(self.nro_order)

        if last_partial:
            last_apportionment = Apportionment.get_by_parcial(
                last_partial.id_parcial)
            if self.serialized:
                apportioment_serializer = ApportionmentSerializer(
                    last_apportionment)
                self.last_apportionment = apportioment_serializer.data
            else:
                self.last_apportionment = last_apportionment

        if self.serialized:
            partial_serializer = PartialSerializer(partials, many=True)
            return partial_serializer.data

        return partials_details if partials_details else None
