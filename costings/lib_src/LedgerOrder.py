"""
Obtiene el saldo mayor de un pedido para productos
"""
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from partials.models import Partial, InfoInvoice, InfoInvoiceDetail
from paids.models import Expense, PaidInvoiceDetail
from decimal import Decimal
from costings.models import Ledger
from lib_src import OrderDetailProductSale


class LedgerOrder():

    def __init__(self):
        self.order = None
        self.order_invoice = None
        self.origin_expense = None,

    def get_sale(self, nro_order):
        self.nro_order = nro_order
        self.order = Order.get_by_order(nro_order)
        if self.order is None or nro_order == '000-00':
            loggin('e', 'El pedido no existe')
            return None

        return {
            'product' : self.get_fob_sale(),
            'expenses': self.get_expenses_sale(),
        }

    def get_fob_sale(self):
        product_sale = {
            'initial_sale':0,
            'downloaded': 0,
            'sale':0,
        }
        self.order_invoice = OrderInvoice.get_by_order(self.order.nro_pedido)
        if self.order_invoice is None:
            return product_sale

        nro_invoice = self.order_invoice.id_factura_proveedor.upper()
        if nro_invoice.startswith('SF-'):
            return product_sale

        init_sale = OrderInvoiceDetail.get_by_order(self.order.nro_pedido)
        order_sale = OrderDetailProductSale().get(self.order.nro_pedido)

        product_sale['initial_sale'] = float(sum(
            [p.nro_cajas * p.costo_caja for p in init_sale]
        )* self.order_invoice.tipo_cambio).__round__(2)

        product_sale['sale'] = float(sum(
            [p['nro_cajas'] * p['costo_caja'] for p in order_sale['sale']]
        )* float(self.order_invoice.tipo_cambio)).__round__(2)

        product_sale['downloaded'] = (
            product_sale['initial_sale'] - product_sale['sale']
        )
        return product_sale

    def get_expenses_sale(self):
        expenses_sale = {
            'initial_sale': 0,
            'downloaded': 0,
            'sale':0,
            'justified': 0,
        }
        expenses = Expense.get_complete_expenses(self.order.nro_pedido)
        self.origin_expense = (
            self.order.gasto_origen * self.order_invoice.tipo_cambio
        ) if self.order.incoterm == 'FOB' else 0
        partials = Partial.get_by_order(self.order.nro_pedido)
        taxes = self.__get_taxes(partials)
        expenses_sale['initial_sale'] = float(
            sum([i.valor_provisionado for i in expenses]) 
            + self.origin_expense 
            + taxes['initial_sale']
        )
        expenses_sale['downloaded'] = self.__get_downloaded_expenses(
            partials
        )

        expenses_sale['justified'] = (
            self.__get_invoiced_value(expenses) + float(taxes['initial_sale'])
        ).__round__(2)

        expenses_sale['sale'] = (
            expenses_sale['initial_sale'] - expenses_sale['downloaded']
        ).__round__(2)
        return expenses_sale;

    def __get_downloaded_expenses(self, partials):
        total_downloaded = 0.0
        for partial in partials:
            if partial.bg_isclosed:
                items_invoice = InfoInvoiceDetail.get_by_partial(
                    partial.id_parcial
                )
                total_downloaded += float(sum(
                  [p.prorrateos_total for p in items_invoice]  
                )).__round__(2)
        return total_downloaded.__round__(2)

    def __get_taxes(self, partials):
        taxes_sale = {
            'initial_sale': 0,
            'downloaded':0,
        }

        for partial in partials:
            if partial.bg_isliquidated:
                taxes_sale['initial_sale'] += partial.arancel_advalorem_pagar_pagado
                taxes_sale['initial_sale'] += partial.arancel_especifico_pagar_pagado
                taxes_sale['initial_sale'] += partial.fodinfa_pagado
                taxes_sale['initial_sale'] += partial.ice_advalorem_pagado
                taxes_sale['initial_sale'] += partial.ice_especifico_pagado
            if partial.bg_isclosed:
                taxes_sale['downloaded'] += partial.arancel_advalorem_pagar_pagado
                taxes_sale['downloaded'] += partial.arancel_especifico_pagar_pagado
                taxes_sale['downloaded'] += partial.fodinfa_pagado
                taxes_sale['downloaded'] += partial.ice_advalorem_pagado
                taxes_sale['downloaded'] += partial.ice_especifico_pagado
        return taxes_sale

    def __get_invoiced_value(self, expenses):
        total = 0.0
        for expense in expenses:
            if expense.concepto == 'ISD':
                total += float(expense.valor_provisionado)

            paids = PaidInvoiceDetail.get_by_expense(
                expense
            )
            total += float(sum([p.valor for p in paids])).__round__(2)

        total += float(self.origin_expense)
        return total
