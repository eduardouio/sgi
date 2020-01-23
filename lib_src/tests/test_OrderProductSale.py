from django.test import TestCase

from lib_src import OrderProductSale

class testOrderProductSale(TestCase):

    def setUp(self):
        self.order_product_sale = OrderProductSale('105-19')
        return super().setUp()

    def test_get_init_sale(self):
        '''Colmprobamos el salfo inicial del pedido'''
        sale = [
            {'nombre' : 'VINO TINTO DARK RED DIABLO', 'cajas' :	528, 'costo_caja':70,},
            {'nombre' : 'VINO CASILLERO MERLOT','cajas' : 210,'costo_caja':40,},
            {'nombre' : 'VINO TINTO RED BLEND CASILLERO DEL DIABLO','cajas' : 350, 'costo_caja':40,},
            {'nombre' : 'VINO ALMAVIVA CAB. SAUV.','cajas' : 3,'costo_caja':715,},
        ]
        
        init_sale = self.order_product_sale.get_init_sale()
        system_sale = []
        self.assertEqual(init_sale.count(), sale.__len__())

        for item in init_sale:
            system_sale.append({
                'nombre' : item.product,
                'cajas' : item.nro_cajas,
                'costo_caja' : item.costo_caja,
            })
        
        self.assertListEqual(sale, system_sale)
        none_sale = OrderProductSale('dontExist').get_init_sale()
        self.assertEqual(None,none_sale)


    def test_get_nationalized(self):
        '''Retornamos todo el producto nacionalizado'''
        pass