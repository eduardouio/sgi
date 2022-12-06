"""
Obtiene el saldo mayor de un pedido para productos
"""
from orders.models import Order, OrderInvoice
from partials.models import Partial
from paids.models import Expense, PaidInvoiceDetail
from decimal import Decimal
from costings.models import Ledger
from lib_src import OrderDetailProductSale
from logs.app_log import loggin


class LedgerOrder():

    def __init__(self):
        self.order = None
        self.order_invoice = None

    def get_sale(self, nro_order):
        loggin('i', 'Solicitando Mayor Pedido {}'.format(nro_order))
        self.nro_order = nro_order
        self.order = Order.get_by_order(nro_order)
        if self.order is None or nro_order == '000-00':
            loggin('e', 'El pedido no existe')
            return None

        fob_tct = self.get_fob_sale()
        expenses = self.get_expenses_sale()
                    
        return {
            'nro_order': nro_order,
            'fob_tct': fob_tct,
            'expenses': expenses,
            'sale': fob_tct + expenses
        }

    def get_fob_sale(self):
        self.order_invoice = OrderInvoice.get_by_order(self.order.nro_pedido)
        if self.order_invoice is None:
            loggin('e', 'el pedido {} no tiene factura'.format(
                self.order.nro_pedido
            ))
            return 0.0

        nro_invoice = self.order_invoice.id_factura_proveedor.upper()
        if nro_invoice.startswith('SF-'):
            loggin('e', 'el pedido {} factura sin numero SF-'.format(
                self.order.nro_pedido
            ))
            return 0.0

        product_sale = OrderDetailProductSale().get(self.order.nro_pedido)
        sale = sum(
            [p['nro_cajas'] * p['costo_caja'] for p in product_sale['sale']]
        )
        loggin('i', 'Se entrega el saldo correcto {}'.format(
            self.order.nro_pedido
        ))
        return (sale * float(self.order_invoice.tipo_cambio)).__round__(2)

    def get_expenses_sale(self):
        expenses = Expense.get_complete_expenses(self.order.nro_pedido)
        total_expenses = Decimal(0)

        for exp in expenses:
            if exp.concepto == 'ISD':
                nro_invoice = self.order_invoice.id_factura_proveedor.upper()
                if not nro_invoice.startswith('SF-'):
                    total_expenses += exp.valor_provisionado
            elif exp.concepto == 'FLETE' and self.order.incoterm == 'CFR':
                total_expenses += exp.valor_provisionado
            else:
                paids = PaidInvoiceDetail.get_by_expense(exp)
                total_expenses += sum([p.valor for p in paids])

        partials = Partial.get_by_order(self.order.nro_pedido)
        taxes_partials = [p.get_paid_taxes(p.id_parcial) for p in partials]
        total_taxes = sum([t['total_pagado'] for t in taxes_partials])

        origin_expense = 0
        if self.order.incoterm == 'fob':
            origin_expense = (
                self.order.gasto_origen * self.order_invoice.tipo_cambio
            )

        total = total_expenses + total_taxes + origin_expense

        ledgers = [
            Ledger.get_by_parcial(p.id_parcial) for p in partials
            if p.bg_isclosed == 1
            ]

        total_down = sum([l.precio_entrega for l in ledgers])

        return float(total - total_down).__round__(2)
