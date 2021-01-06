from django.test import TestCase
from lib_src import OrderDetailProductSale
from orders.models import OrderInvoiceDetail


class TestGeneralStatusOrders(TestCase):

    def test_get_r10_liquidated(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('360-19')
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 1164,
                'cod_contable': '01011080050317010750',
                'nro_cajas': 1176,
                'costo_caja': 18.50,
            }],
            'nationalized': [{
                'detalle_pedido_factura': 1164,
                'cod_contable': '01011080050317010750',
                'nro_cajas': 1176,
                'costo_caja': 18.50,
            }],
            'sale': [{
                'detalle_pedido_factura': 1164,
                'cod_contable': '01011080050317010750',
                'nro_cajas': 0,
                'costo_caja': 18.50,
                'product': OrderInvoiceDetail.get_by_id(1164)
            }]
        }

        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

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
                'costo_caja': 29.41,
                'product': OrderInvoiceDetail.get_by_id(936)
            }, {
                'detalle_pedido_factura': 794,
                'cod_contable': '01012090550702010750',
                'nro_cajas': 0,
                'costo_caja': 25.21,
                'product': OrderInvoiceDetail.get_by_id(794)
            }, {
                'detalle_pedido_factura': 791,
                'cod_contable': '01042091050602010750',
                'nro_cajas': 0,
                'costo_caja': 29.66,
                'product': OrderInvoiceDetail.get_by_id(791)
            }, {
                'detalle_pedido_factura': 790,
                'cod_contable': '01042091050702010750',
                'nro_cajas': 0,
                'costo_caja': 32.40,
                'product': OrderInvoiceDetail.get_by_id(790)
            }, {
                'detalle_pedido_factura': 792,
                'cod_contable': '01042091050802010750',
                'nro_cajas': 0,
                'costo_caja': 36.40,
                'product': OrderInvoiceDetail.get_by_id(792)
            }]
        }
        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

    def test_R10WithoutLiquidation(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('198-20')
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 1457,
                'cod_contable': '01011080010407011000',
                'nro_cajas': 1725,
                'costo_caja': 16.60
            }],
            'nationalized': [{
                'detalle_pedido_factura': 1457,
                'cod_contable': '01011080010407011000',
                'nro_cajas': 0,
                'costo_caja': 16.60
            }],
            'sale': [{
                'detalle_pedido_factura': 1457,
                'cod_contable': '01011080010407011000',
                'nro_cajas': 1725,
                'costo_caja': 16.60,
                'product': OrderInvoiceDetail.get_by_id(1457)
            }]
        }
        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

    def test_R70withClosePartials(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('104-19')
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 782,
                'cod_contable': '01022093100501010750',
                'nro_cajas': 70,
                'costo_caja': 138.68
            },
            {
                'detalle_pedido_factura': 783,
                'cod_contable': '01022093100303010750',
                'nro_cajas': 400,
                'costo_caja': 19.89
            },
            {
                'detalle_pedido_factura': 784,
                'cod_contable': '01022093100407010750',
                'nro_cajas': 200,
                'costo_caja': 26.25
            },
            {
                'detalle_pedido_factura': 785,
                'cod_contable': '01022093120102010750',
                'nro_cajas': 1035,
                'costo_caja': 13.77
            }],
            'nationalized': [{
                'detalle_pedido_factura': 782,
                'cod_contable': '01022093100501010750',
                'nro_cajas': 70,
                'costo_caja': 138.68
            },
            {
                'detalle_pedido_factura': 783,
                'cod_contable': '01022093100303010750',
                'nro_cajas': 400,
                'costo_caja': 19.89
            },
            {
                'detalle_pedido_factura': 784,
                'cod_contable': '01022093100407010750',
                'nro_cajas': 200,
                'costo_caja': 26.25
            },
            {
                'detalle_pedido_factura': 785,
                'cod_contable': '01022093120102010750',
                'nro_cajas': 1035,
                'costo_caja': 13.77
            }],
            'sale': [{
                'detalle_pedido_factura': 782,
                'cod_contable': '01022093100501010750',
                'nro_cajas': 0,
                'costo_caja': 138.68,
                'product': OrderInvoiceDetail.get_by_id(782)
            },
            {
                'detalle_pedido_factura': 783,
                'cod_contable': '01022093100303010750',
                'nro_cajas': 0,
                'costo_caja': 19.89,
                'product': OrderInvoiceDetail.get_by_id(783)
            },
            {
                'detalle_pedido_factura': 784,
                'cod_contable': '01022093100407010750',
                'nro_cajas': 0,
                'costo_caja': 26.25,
                'product': OrderInvoiceDetail.get_by_id(784)
            },
            {
                'detalle_pedido_factura': 785,
                'cod_contable': '01022093120102010750',
                'nro_cajas': 0,
                'costo_caja': 13.77,
                'product': OrderInvoiceDetail.get_by_id(785)
            }]
        }
        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

    def test_R70withClosePartialAndSale(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('091-20')
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 1336,
                'cod_contable': '02012130020104080750',
                'nro_cajas': 812,
                'costo_caja': 123.00
            }],
            'nationalized': [{
                'detalle_pedido_factura': 1336,
                'cod_contable': '02012130020104080750',
                'nro_cajas': 390,
                'costo_caja': 123.00
            }],
            'sale': [{
                'detalle_pedido_factura': 1336,
                'cod_contable': '02012130020104080750',
                'nro_cajas': 422,
                'costo_caja': 123.00,
                'product': OrderInvoiceDetail.get_by_id(1336)
            }]
        }
        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

    def test_R70WithSaleandPartialWithouClosed(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('147-19', ignore_liquidated=True)
        spected = {
            'init_sale': [{
                'detalle_pedido_factura': 840,
                'cod_contable': '01011080010503010750',
                'nro_cajas': 882,
                'costo_caja': 24.00
            },{
                'detalle_pedido_factura': 841,
                'cod_contable': '01011080010508010750',
                'nro_cajas': 98,
                'costo_caja': 24.00
            }],
            'nationalized': [{
                'detalle_pedido_factura': 840,
                'cod_contable': '01011080010503010750',
                'nro_cajas': 0,
                'costo_caja': 24.00
            },{
                'detalle_pedido_factura': 841,
                'cod_contable': '01011080010508010750',
                'nro_cajas': 0,
                'costo_caja': 24.00
            }],
            'sale': [{
                'detalle_pedido_factura': 840,
                'cod_contable': '01011080010503010750',
                'nro_cajas': 882,
                'costo_caja': 24.00,
                'product': OrderInvoiceDetail.get_by_id(840)
            },{
                'detalle_pedido_factura': 841,
                'cod_contable': '01011080010508010750',
                'nro_cajas': 98,
                'costo_caja': 24.00,
                'product': OrderInvoiceDetail.get_by_id(841)
            }]
        }
        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

    def test_order_without_ptoduct(self):
        OrderDetSale = OrderDetailProductSale()
        sale = OrderDetSale.get('555-16', ignore_liquidated=True)
        spected = {
            'init_sale': [],
            'nationalized': [],
            'sale': []
        }
        self.match(spected['init_sale'], sale['init_sale'])
        self.match(spected['nationalized'], sale['nationalized'])
        self.match(spected['sale'], sale['sale'])

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
                #import ipdb; ipdb.set_trace()
                if s['detalle_pedido_factura'] == r['detalle_pedido_factura']:
                    self.assertEqual(s, r)
        return True
