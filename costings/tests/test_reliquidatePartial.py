from django.test import TestCase
from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from lib_src.ReliquidatePartial import ReliquidatePartial
from logs.app_log import loggin
from lib_src.ReliquidatePartial import ReliquidatePartial



class TestReliquidatePartial07118P1(TestCase):

    def setUp(self):
        loggin('t', 'iniciando test de clase Reliquidacion parcial')
        complete_order_info = CompleteOrderInfo().get_data('071-18')
        all_partials = []
        for partial in complete_order_info['partials']:
            all_partials.append(CompletePartialInfo().get_data(partial.id_parcial))
        
        approtionment_expenses  = ApportionmentExpenses(
            complete_order_info = complete_order_info,
            all_partials = all_partials,
            ordinal_current_partial = 1,
        ).get_data()

        returned_data = ReliquidatePartial(
            complete_order_info = complete_order_info,
            apportionment_expenses = approtionment_expenses,
            all_partials = all_partials,
            ordinal_current_partial = 1
        ).get_data()

        return super().setUp()


    def test_taxes(self):
        pass
    

    def test_sums(self):
        pass