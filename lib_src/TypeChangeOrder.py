from logs import loggin
from orders.models import Order, OrderInvoice
from partials.models import Partial


def get_by_order(nro_order):
    order_invoice = OrderInvoice.get_by_order(nro_order)
    return order_invoice.tipo_cambio


def get_by_parcial(id_partial):
    partial = Partial.get_by_id(id_partial)
    order_invoice = OrderInvoice.get_by_order(partial.nro_pedido)
    return order_invoice.tipo_cambio
