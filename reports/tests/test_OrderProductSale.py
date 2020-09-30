from django.test import TestCase
from logs.app_log import loggin
from reports.src import OrderProductSale
from orders.models import OrderInvoiceDetail, Order


class TestOrderProductSale(TestCase):

    def test_order_dont_exist(self):
        self.assertIsNone(OrderProductSale().get('01987'))

    def test_R70_without_partials(self):
        """Valida un R70 con salido inicial, sin parciales"""
        loggin('t', 'Saldo de pedido sin parciales')
        order = Order().get_by_order('020-20')
        spected_sale = {
            'order': order,
            'init_sale': [
                {
                    'detalle_pedido_factura': 1225,
                    'cajas': 784,
                    'costo_caja': 61.00}
                ],
            'nationalized': [
                {
                    'detalle_pedido_factura': 1225,
                    'cajas': 0,
                    'costo_caja': 61.00
                }
                ],
            'sale': [
                {
                    'detalle_pedido_factura': 1225,
                    'cajas': 784,
                    'costo_caja': 61.00
                }
                ]
        }

        sale = OrderProductSale().get('020-20')
        self.assertDictEqual(spected_sale, sale)

    def test_R70_with_partials(self):
        loggin('t', 'Testeando saldo pedido con parciales')
        order = Order().get_by_order('104-19')
        spected_sale = {
            'order': order,
            'init_sale': [
                {
                    'detalle_pedido_factura': 782,
                    'cajas': 70,
                    'costo_caja': 138.68
                },
                {
                    'detalle_pedido_factura': 783,
                    'cajas': 400,
                    'costo_caja': 19.89
                },
                {
                    'detalle_pedido_factura': 784,
                    'cajas': 200,
                    'costo_caja': 26.25
                },
                {
                    'detalle_pedido_factura': 785,
                    'cajas': 1035,
                    'costo_caja': 13.77
                }
            ],
            'nationalized': [
                {
                    'detalle_pedido_factura': 782,
                    'cajas': 70,
                    'costo_caja': 138.68
                },
                {
                    'detalle_pedido_factura': 783,
                    'cajas': 400,
                    'costo_caja': 19.89
                },
                {
                    'detalle_pedido_factura': 784,
                    'cajas': 200,
                    'costo_caja': 26.25
                },
                {
                    'detalle_pedido_factura': 785,
                    'cajas': 0,
                    'costo_caja': 13.77
                }
            ],
            'sale': [
                {
                    'detalle_pedido_factura': 782,
                    'cajas': 0,
                    'costo_caja': 138.68
                },
                {
                    'detalle_pedido_factura': 783,
                    'cajas': 0,
                    'costo_caja': 19.89
                },
                {
                    'detalle_pedido_factura': 784,
                    'cajas': 0,
                    'costo_caja': 26.25
                },
                {
                    'detalle_pedido_factura': 785,
                    'cajas': 1035,
                    'costo_caja': 13.77
                }
            ]
        }

        sale = OrderProductSale().get('104-19')
        self.assertListEqual(spected_sale['init_sale'], sale['init_sale'])
        self.assertListEqual(spected_sale['nationalized'], sale['nationalized'])