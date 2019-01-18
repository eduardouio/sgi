from django.test import TestCase

from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from logs.app_log import loggin


class TestApportionmentExpenses(TestCase):

    def test_ok(self):
        loggin('t', 'Iniciando Test de Prorrateos Parcial')
        self.assertTrue(True)