from django.test import TestCase

from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from logs.app_log import loggin
from partials.models.Partial import Partial


class TestApportionmentExpensesP1(TestCase):
    '''
    Test de liquidacion para el primer parcial
    '''
    def setUp(self):
        loggin('t', 'Testing de liquidacion parcial 1')
        partials = Partial.get_by_order('071-18') 
        self.all_partials = []

        for p in partials:
            self.all_partials.append(CompletePartialInfo().get_data(p.id_parcial))
        
        self.result = ApportionmentExpenses(
                    complete_order_info = CompleteOrderInfo().get_data('071-18'),
                    all_partials =  self.all_partials, 
                    ordinal_current_partial =  1
                ).get_data()

        #redondeamos valores a la DB
        for cat in self.result:
            if isinstance(self.result[cat], dict):
                for i in self.result[cat]:
                    self.result[cat][i] = round(self.result[cat][i],10)

        return super().setUp()


    def test_get_fob_partial(self):
        fobs_1p = {
            'fob_inicial': 28191.000000,
            'fob_parcial': 13500.00000,
            'fob_parcial_razon_inicial': 0.4788762371,
            'fob_parcial_razon_saldo': 0.4788762371,
            'fob_saldo': 28191.000000,
            'fob_proximo_parcial': 14691.0000,
        }
        self.assertDictEqual(fobs_1p, self.result['fobs'])
    
    
    def test_get_warenhouses(self):
        warenhousing = {
            'almacenaje_parcial' : 503.00,
            'almacenaje_anterior' : 0,
            'almacenaje_aplicado' : 240.8747472613,
            'almacenaje_proximo_parcial' : 262.1252527387,
        }

        self.assertDictEqual(self.result['warenhousing'], warenhousing),


    def test_get_apportionment_expenses(self):
        total_iniciales = 4359.715087
        total_recibido = 0.0

        for item in self.result['apportionment_expenses']:
            total_recibido += item['valor_prorrateado']

        self.assertEqual(self.result['apportionment_expenses'].__len__(), 20)
        self.assertEqual(total_iniciales, round(total_recibido,6))
    
    def test_get_droped_expenses(self):
        droped_expenses = {
            'gastos_drop_parcial' : 0,
            'gastos_drop_parcial_anterior' : 0,
            'gastos_drop_parcial_aplicado' : 0,
            'gastos_drop_parcial_proximo_parcial  ' : 0,
        }
        self.assertTrue(self.result['droped_expenses'])


#test de liquidacion para el segundo parcial
#crear metodo para liquidacion de segundo parcial gastos simolares a bodega
#def get_fob_partial_2(self):
#        '''Testeo pendiente, se debe cerrar el primer parcial'''
#
#        fobs_2p = {
#            'fob_inicial': 28191.00000,
#            'fob_parcial': 6085.200000,
#            'fob_saldo': 14691.000000,
#            'fob_parcial_razon_inicial': 0.215856,
#            'fob_parcial_razon_saldo': 0.414213,
#            'fob_proximo_parcial': 8605.800000,
#        }
#        partials = Partial.get_by_order('071-18') 
#        all_partials = []
#
#        for p in partials:
#            all_partials.append(CompletePartialInfo().get_data(p.id_parcial))
#
#        result = ApportionmentExpenses(
#                    complete_order_info = CompleteOrderInfo().get_data('071-18'),
#                    all_partials =  all_partials, 
#                    ordinal_current_partial =  2
#                ).get_data()
#
#        self.assertEqual(fobs_2p['fob_saldo'], result['fobs']['fob_saldo'])