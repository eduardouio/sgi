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
                'cod_contable': '01011080050317010750',
                'nro_cajas': 1176,
                'costo_caja': Decimal(18.50)
            }],
            'nationalized': [{
                'cod_contable': '01011080050317010750',
                'nro_cajas': 1176,
                'costo_caja': Decimal(18.50)
            }],
            'sale': [{
                'cod_contable': '01011080050317010750',
                'nro_cajas': 0,
                'costo_caja': Decimal(18.50)
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
                'cod_contable': '01012090550411010375',
                'nro_cajas': 540,
                'costo_caja': Decimal(29.41)
            }, {
                'cod_contable': '01012090550702010750',
                'nro_cajas': 500,
                'costo_caja': Decimal(25.21)
            }, {
                'cod_contable': '01042091050602010750',
                'nro_cajas': 50,
                'costo_caja': Decimal(29.66)
            }, {
                'cod_contable': '01042091050702010750',
                'nro_cajas': 100,
                'costo_caja': Decimal(32.40)
            }, {
                'cod_contable': '01042091050802010750',
                'nro_cajas': 50,
                'costo_caja': Decimal(36.40)
            }],
            'nationalized': [{
                'cod_contable': '01012090550411010375',
                'nro_cajas': 540,
                'costo_caja': Decimal(29.41)
            }, {
                'cod_contable': '01012090550702010750',
                'nro_cajas': 500,
                'costo_caja': Decimal(25.21)
            }, {
                'cod_contable': '01042091050602010750',
                'nro_cajas': 50,
                'costo_caja': Decimal(29.66)
            }, {
                'cod_contable': '01042091050702010750',
                'nro_cajas': 100,
                'costo_caja': Decimal(32.40)
            }, {
                'cod_contable': '01042091050802010750',
                'nro_cajas': 50,
                'costo_caja': Decimal(36.40)
            }],
            'sale': [{
                'cod_contable': '01012090550411010375',
                'nro_cajas': 0,
                'costo_caja': Decimal(29.41)
            }, {
                'cod_contable': '01012090550702010750',
                'nro_cajas': 0,
                'costo_caja': Decimal(25.21)
            }, {
                'cod_contable': '01042091050602010750',
                'nro_cajas': 0,
                'costo_caja': Decimal(29.66)
            }, {
                'cod_contable': '01042091050702010750',
                'nro_cajas': 0,
                'costo_caja': Decimal(32.40)
            }, {
                'cod_contable': '01042091050802010750',
                'nro_cajas': 0,
                'costo_caja': Decimal(36.40)
            }]
        }

        self.assertTrue(self.match(spected['init_sale'], sale['init_sale']))
        #self.assertTrue(self.match(spected['nationalized'], sale['nationalized']))
        #self.assertTrue(self.match(spected['sale'], sale['sale']))

    def match(self, spected, recived):
        """Realiza el test de igualdad en los items de los diccionarios

        Arguments:
            spected {list} -- Lista Esperada
            recived {list} -- Lista devuelta
        Return:100
            {boolean}
        """
        for s in spected:
            for r in recived:
                if s['cod_contable'] == r['cod_contable'].cod_contable:
                    if s['nro_cajas'] != r['nro_cajas']:
                        loggin('t', 'Falla en cajas')
                        return False
                    if s['costo_caja'] != r['costo_caja']:
                        loggin('t', 'Falla en costo')
                        return False
        return True
