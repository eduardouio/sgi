from django.test import TestCase

from lib_src.Reliquidate import Reliquidate
from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from partials.models.Partial import Partial 
from logs.app_log import loggin


class TestReliquidateOrder(TestCase):
    '''
    Clase de testeo creada para probar la liquidacion de un pedido R10
    '''


    def setUp(self):
        loggin('t', 'iniciando testeo de reliquidacion de pedido')

        partials = Partial.get_by_order('071-18') 
        self.all_partials = []

        for p in partials:
            self.all_partials.append(CompletePartialInfo().get_data(p.id_parcial))
        
        self.apportionment = ApportionmentExpenses(
                    complete_order_info = CompleteOrderInfo().get_data('071-18'),
                    all_partials =  self.all_partials, 
                    ordinal_current_partial =  1
                ).get_data()
            
        self.spected_values = Reliquidate(nro_order = '192-18')

        return super().setUp()
    
    def get_taxes(self):
        self.assertTrue(True)



class TestReliquidatePartial(TestCase):
    '''
        Clase de test de reliquidacion de parcial
    '''
    pass
    