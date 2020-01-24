from django.test import TestCase

from lib_src import OrderProductSale
from logs import loggin


class testOrderProductSale(TestCase):

    def setUp(self):
        self.order_product_sale = OrderProductSale('105-19')
        return super().setUp()

    def test_get_init_sale(self):
        '''Colmprobamos el salfo inicial del pedido'''
        spected_init_sale = [
            {'detalle_pedido_factura': 773,'nombre' : 'VINO TINTO DARK RED DIABLO', 'cajas' :	528, 'costo_caja':70,},
            {'detalle_pedido_factura': 774,'nombre' : 'VINO CASILLERO MERLOT','cajas' : 210,'costo_caja':40,},
            {'detalle_pedido_factura': 775,'nombre' : 'VINO TINTO RED BLEND CASILLERO DEL DIABLO','cajas' : 350, 'costo_caja':40,},
            {'detalle_pedido_factura': 776,'nombre' : 'VINO ALMAVIVA CAB. SAUV.','cajas' : 3,'costo_caja':715,},
        ]
        
        init_sale = self.order_product_sale.get_init_sale()
        self.assertEqual(init_sale.__len__(), spected_init_sale.__len__())
        self.assertListEqual(spected_init_sale, init_sale)
        none_sale = OrderProductSale('dontExist').get_init_sale()
        self.assertEqual(None,none_sale)


    def test_get_nationalized(self):
        '''Retornamos todo el producto nacionalizado'''
        spected_nationalized = [
            {'detalle_pedido_factura': 773,'nombre' : 'VINO TINTO DARK RED DIABLO', 'cajas' :	300, 'costo_caja':70, 'fob_tct' : 21000},
            {'detalle_pedido_factura': 774,'nombre' : 'VINO CASILLERO MERLOT','cajas' : 210,'costo_caja':40, 'fob_tct' : 8400},
            {'detalle_pedido_factura': 775,'nombre' : 'VINO TINTO RED BLEND CASILLERO DEL DIABLO','cajas' : 350, 'costo_caja':40, 'fob_tct' : 14000},
            {'detalle_pedido_factura': 776,'nombre' : 'VINO ALMAVIVA CAB. SAUV.','cajas' : 3,'costo_caja':715, 'fob_tct' : 2145},
        ]
        
        nationalized = self.order_product_sale.get_nationalized()
        loggin('t', nationalized)
        self.assertEqual(spected_nationalized.__len__(), nationalized.__len__())
        
        for i_nat in nationalized:
            for i_spec_nat in nationalized:
                if i_nat['detalle_pedido_factura'] == i_spec_nat['detalle_pedido_factura']:
                    self.assertDictEqual(i_nat, i_spec_nat)
    

    def  test_get_sale(self):
        spected_data = {
            'items' : [
                {'detalle_pedido_factura': 773,'nombre' : 'VINO TINTO DARK RED DIABLO', 'cajas' : 528, 'nacionalizado' : 300 ,'costo_caja':70},
                {'detalle_pedido_factura': 774,'nombre' : 'VINO CASILLERO MERLOT','cajas' : 210, 'nacionalizado':210,'costo_caja':40},
                {'detalle_pedido_factura': 775,'nombre' : 'VINO TINTO RED BLEND CASILLERO DEL DIABLO','cajas' : 350, 'nacionalizado':350, 'costo_caja':40},
                {'detalle_pedido_factura': 776,'nombre' : 'VINO ALMAVIVA CAB. SAUV.','cajas' : 3, 'nacionalizado':3,'costo_caja':715},
            ],
            'sums' : {
                'cajas' : 1091,
                'nacionalizado' : 863,
                'fob_tct_inicial' : 61505,
                'fob_tct_nacionalizado' : 45545, 
                'fob_tct_saldo' : 15960,
                'tct' : 1,
            }
        }
        data = self.order_product_sale.get_sale()
        self.assertEqual(spected_data.__len__(), data.__len__())
        self.assertListEqual(spected_data['items'], data['items'])
        self.assertDictEqual(spected_data['sums'],data['sums'] )