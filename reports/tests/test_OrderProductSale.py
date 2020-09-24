from django.test import TestCase
from reports.src import OrderProductSale
from products.models import Product
from orders.models import Order


class TestOrderProductSale(TestCase):

    def test_R70_without_partials(self):
        """Valida un R70 con salido inicial, sin parciales"""
        order = Order().get_by_order('020-20')        
        product = Product().get_by_cod_contable('02012130020202010750')
        spected_sale = {
            'order': order,
            'init_sale': [{
                'cod_contable': product,
                'cajas': 784,
                'costo_caja': 61.00
            }],
            'nationalized': [{
                'cod_contable': product,
                'cajas': 0,
                'costo_caja': 61.00
            }],
            'sale': [{
                'cod_contable': product,
                'cajas': 784,
                'costo_caja': 61.00
            }]
        }

        sale = OrderProductSale().get('020-20')
        import pudb; pudb.set_trace()
        self.assertDictEqual(spected_sale, sale)

    def test_R70_with_partials_sale(self):
        return 0
           
        """Valida un pedido con parciales sin saldo"""
        sale = OrderProductSale().get('110-19')
        order = Order().get_by_order('110-19')
        product = [
            Product().get_by_cod_contable('01042091050702010750'),
            Product().get_by_cod_contable('01042091050602010750'),
            Product().get_by_cod_contable('01042091050802010750'),
            Product().get_by_cod_contable('01012090550702010750'),
            Product().get_by_cod_contable('01012090550411010375')
        ]
        sale_spected = {
            'order': order,
            'init_sale': [
                {
                    'cod_contable': product[0],
                    'cajas': 100,
                    'costo_caja': 32.40
                }, {
                    'cod_contable': product[1],
                    'cajas': 50,
                    'costo_caja': 29.66
                }, {
                    'cod_contable': product[2],
                    'cajas': 50,
                    'costo_caja': 36.40
                }, {
                    'cod_contable': product[3],
                    'cajas': 500,
                    'costo_caja': 25.21
                }, {
                    'cod_contable': product[4],
                    'cajas': 540,
                    'costo_caja': 29.41
                }
            ],
            'nationalized': [
                {
                    'cod_contable': product[0],
                    'cajas': 100,
                }, {
                    'cod_contable': product[1],
                    'cajas': 50,
                }, {
                    'cod_contable': product[2],
                    'cajas': 50,
                }, {
                    'cod_contable': product[3],
                    'cajas': 200,
                }, {
                    'cod_contable': product[4],
                    'cajas': 200,
                }
            ],
            'sale': [
                {
                    'cod_contable': product[0],
                    'cajas': 0,
                    'costo_caja': 32.40
                }, {
                    'cod_contable': product[1],
                    'cajas': 514,
                    'costo_caja': 29.66
                }, {
                    'cod_contable': product[2],
                    'cajas': 0,
                    'costo_caja': 36.40
                }, {
                    'cod_contable': product[3],
                    'cajas': 400,
                    'costo_caja': 25.21
                }, {
                    'cod_contable': product[4],
                    'cajas': 300,
                    'costo_caja': 29.41
                }
            ]
        }
        self.assertEqual.__self__.maxDiff = None
        self.assertListEqual(sale_spected['init_sale'], sale['init_sale'])
        self.assertListEqual(sale_spected['nationalized'], sale['nationalized'])
        #self.assertListEqual(sale_spected['sale'], sale['sale'])

    def test_R70_with_partials_not_sale(self):
        """ Valida un pedido con Parciales sin saldo"""
        pass

    def test_order_without_init_sale(self):
        """Valida un pedido sin saldo inicial"""
        pass

    def test_order_whitout_partials(self):
        pass

    def test_order_whit_partial_liquidated(self):
        pass
