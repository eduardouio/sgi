from .OrderProductSale import OrderProductSale
from logs import loggin
from orders.models import Order


class CloseOpenOrdersWithoutProduct(object):
    '''cierra los pedidos que tienen todos los parciales cerrados'''

    def check_order(self, nro_order) -> bool:
        '''
        comprueba el salfo de un pedido y lo cierra si amerita
        '''
        loggin('i', 'comprobando saldo de pedido {}'.format(nro_order))
        order = Order.get_by_order(nro_order)
        if order is None:
            loggin('w', 'El pedido no existe')
            return False

        if order.bg_isclosed:
            loggin('i', 'pedido ya esta cerrado')
            return True

        order_sale = OrderProductSale(nro_order).get_sale()
        if order_sale['sums']['cajas'] == order_sale['sums']['nacionalizado']:
            order.bg_isclosed = 1
            order.save()
            loggin('s', 'pedido {} fue cerrado'.format(nro_order))
            return True

        loggin('i', 'El pedido {} no fue cerrado'.format(nro_order))
        return False
