from decimal import Decimal

from django.test import TestCase
from lib_src import OrderDetailProductSale
from logs.app_log import loggin


class TestGeneralStatusOrders(TestCase):

    def test_get_r10_liquidated(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('360-19')
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 1164,
                'cod_contable': '01011080050317010750',
                'nro_cajas': 1176,
                'costo_caja': 18.50
            }],
            'nationalized': [{
                'detalle_pedido_factura': 1164,
                'cod_contable': '01011080050317010750',
                'nro_cajas': 1176,
                'costo_caja': 18.50
            }],
            'sale': [{
                'detalle_pedido_factura': 1164,
                'cod_contable': '01011080050317010750',
                'nro_cajas': 0,
                'costo_caja': 18.50
            }]
        }

        self.assertTrue(self.match(spected['init_sale'], sale['init_sale']))
        self.assertTrue(self.match(spected['nationalized'], sale['nationalized']))
        self.assertTrue(self.match(spected['sale'], sale['sale']))

    def test_get_r70_liquidated(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('110-19')
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 936,
                'cod_contable': '01012090550411010375',
                'nro_cajas': 540,
                'costo_caja': 29.41
            }, {
                'detalle_pedido_factura': 794,
                'cod_contable': '01012090550702010750',
                'nro_cajas': 500,
                'costo_caja': 25.21
            }, {
                'detalle_pedido_factura': 791,
                'cod_contable': '01042091050602010750',
                'nro_cajas': 50,
                'costo_caja': 29.66
            }, {
                'detalle_pedido_factura': 790,
                'cod_contable': '01042091050702010750',
                'nro_cajas': 100,
                'costo_caja': 32.40
            }, {
                'detalle_pedido_factura': 792,
                'cod_contable': '01042091050802010750',
                'nro_cajas': 50,
                'costo_caja': 36.40
            }],
            'nationalized': [{
                'detalle_pedido_factura': 936,
                'cod_contable': '01012090550411010375',
                'nro_cajas': 540,
                'costo_caja': 29.41
            }, {
                'detalle_pedido_factura': 794,
                'cod_contable': '01012090550702010750',
                'nro_cajas': 500,
                'costo_caja': 25.21
            }, {
                'detalle_pedido_factura': 791,
                'cod_contable': '01042091050602010750',
                'nro_cajas': 50,
                'costo_caja': 29.66
            }, {
                'detalle_pedido_factura': 790,
                'cod_contable': '01042091050702010750',
                'nro_cajas': 100,
                'costo_caja': 32.40
            }, {
                'detalle_pedido_factura': 792,
                'cod_contable': '01042091050802010750',
                'nro_cajas': 50,
                'costo_caja': 36.40
            }],
            'sale': [{
                'detalle_pedido_factura': 936,
                'cod_contable': '01012090550411010375',
                'nro_cajas': 0,
                'costo_caja': 29.41
            }, {
                'detalle_pedido_factura': 794,
                'cod_contable': '01012090550702010750',
                'nro_cajas': 0,
                'costo_caja': 25.21
            }, {
                'detalle_pedido_factura': 791,
                'cod_contable': '01042091050602010750',
                'nro_cajas': 0,
                'costo_caja': 29.66
            }, {
                'detalle_pedido_factura': 790,
                'cod_contable': '01042091050702010750',
                'nro_cajas': 0,
                'costo_caja': 32.40
            }, {
                'detalle_pedido_factura': 792,
                'cod_contable': '01042091050802010750',
                'nro_cajas': 0,
                'costo_caja': 36.40
            }]
        }

        #self.match(spected['init_sale'], sale['init_sale'])
        #self.match(spected['nationalized'], sale['nationalized'])
        #self.assertTrue(self.match(spected['sale'], sale['sale']))

    def test_R10WithoutLiquidation(self):
        pass

    def match(self, spected, recived, pause=False):
        """Realiza el test de igualdad en los items de los diccionarios

        Arguments:
            spected {list} -- Lista Esperada
            recived {list} -- Lista devuelta
        Return:100
            {boolean}
        """
        if pause:
            import ipdb; ipdb.set_trace()

        for s in spected:
            for r in recived:
                if s['detalle_pedido_factura'] == r['detalle_pedido_factura']:
                    self.assertEqual(s, r)
        return True
