from django.test import TestCase
from lib_src import CloseOpenOrdersWithoutProduct
from orders.models import Order


class CloseOpenOrdersWithoutProductTEST(TestCase):

    def test_check_order(self):
        # pedido abierto con saldo
        order_sale = CloseOpenOrdersWithoutProduct().check_order('247-18')
        order = Order.get_by_order('247-18')
        self.assertEqual(order_sale, False)
        self.assertEqual(bool(order.bg_isclosed), False)
        # pedido abierto sin saldo
        order_sale = CloseOpenOrdersWithoutProduct().check_order('350-19')
        order = Order.get_by_order('350-19')
        self.assertEqual(order_sale, True)
        self.assertEqual(bool(order.bg_isclosed), True)
        # pedido cerrado
        order_sale = CloseOpenOrdersWithoutProduct().check_order('235-19')
        order = Order.get_by_order('235-19')
        self.assertEqual(order_sale, True)
        self.assertEqual(bool(order.bg_isclosed), True)
