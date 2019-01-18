from django.test import TestCase

from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from logs.app_log import loggin
from partials.models.Partial import Partial


class TestApportionmentExpenses(TestCase):
    '''
    Los test de esta clase se los realiza usando la documentacionde del pedido
    071/18 al momento con 3 parciales cerrados y saldo activo en el sistema
    '''

    def test_get_fob_partial_1(self):
        loggin('t', 'Testenado Fobs del primer parcial')
        fobs_1p = {
            'fob_inicial': 28191.000000,
            'fob_parcial': 13500.00000,
            'fob_parcial_razon_inicial': 0.478876,
            'fob_parcial_razon_saldo': 0.478876,
            'fob_saldo': 14691.000000,
            'fob_proximo_parcial': 14691.000000,
        }
        partials = Partial.get_by_order('071-18') 
        all_partials = []

        for p in partials:
            all_partials.append(CompletePartialInfo().get_data(p.id_parcial))

        result = ApportionmentExpenses(
                    complete_order_info = CompleteOrderInfo().get_data('071-18'),
                    all_partials =  all_partials, 
                    ordinal_current_partial =  1
                ).get_data()

        self.assertDictEqual(fobs_1p, result['fobs'])
    

    def test_get_fob_partial_2(self):
        loggin('t', 'Testenado Fobs del segundo parcial')
        fobs_2p = {
            'fob_inicial': 28191.000000,
            'fob_parcial': 6085.200000,
            'fob_parcial_razon_inicial': 0.215856,
            'fob_parcial_razon_saldo': 00.414213,
            'fob_saldo': 14691.000000,
            'fob_proximo_parcial': 8605.800000,
        }
        partials = Partial.get_by_order('071-18') 
        all_partials = []

        for p in partials:
            all_partials.append(CompletePartialInfo().get_data(p.id_parcial))

        result = ApportionmentExpenses(
                    complete_order_info = CompleteOrderInfo().get_data('071-18'),
                    all_partials =  all_partials, 
                    ordinal_current_partial =  2
                ).get_data()

        self.assertEqual(fobs_2p['fob_inicial'], result['fobs']['fob_inicial'])
        self.assertEqual(fobs_2p['fob_parcial'], result['fobs']['fob_parcial'])
        self.assertEqual(fobs_2p['fob_parcial_razon_inicial'], result['fobs']['fob_parcial_razon_inicial'])
        self.assertEqual(fobs_2p['fob_saldo'], result['fobs']['fob_saldo'])
        self.assertEqual(fobs_2p['fob_parcial_razon_saldo'], result['fobs']['fob_parcial_razon_saldo'])
