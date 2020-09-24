from django.test import TestCase
from logs import loggin
from lib_src import ExpensesReportSale

class ExpensesReportSaleTEST(TestCase):

    def setUp(self):
        self.expenses_report_sale = ExpensesReportSale('105-19')
        return super().setUp()
    
    def test_get_init_expenses(self):
        spected_data = {
            'saldo_inicial_gi' : 5991.25,
            'valor_prorrateado_gi' : 4436.57,
            'por_prorratear_gi' : 1554.68,
        }
        data = self.expenses_report_sale.get_init_expenses()
        self.assertDictEqual(spected_data, data)
    

    def test_get_last_apportionment(self):
        spected_data = {
            'almacenjae_pendiente' : 713.14,
            'fob_prox_parcial' : 15960,
            'gasto_origen_prox_parcial' : 0,
        }

        data = self.expenses_report_sale.get_last_apportionment()
        self.assertDictEqual(spected_data, data)


    def test_get_last_partial_expenses(self):
        spected_data = {
            'saldo_inicial_lp' : 330,
            'id_parcial' : 688,
        }
        self.expenses_report_sale.get_last_apportionment()
        data = self.expenses_report_sale.get_last_partial_expenses()
        self.assertDictEqual(spected_data, data)
    

    def test_get_expenses(self):
        spected_data = {
            'saldo_inicial_gi' : 5991.25,
            'valor_prorrateado_gi' : 4436.57,
            'por_prorratear_gi' : 1554.68,
            'almacenjae_pendiente' : 713.14,
            'fob_prox_parcial' : 15960.0,
            'gasto_origen_prox_parcial' : 0.0,
            'saldo_inicial_lp' : 330.0,
            'id_parcial' : 688,
        }
        data = self.expenses_report_sale.get_sale()
        self.assertEqual(spected_data['saldo_inicial_gi'], data['saldo_inicial_gi'])
        self.assertEqual(spected_data['valor_prorrateado_gi'], data['valor_prorrateado_gi'])
        self.assertEqual(spected_data['por_prorratear_gi'], data['por_prorratear_gi'])
        self.assertEqual(spected_data['almacenjae_pendiente'], data['almacenjae_pendiente'])
        self.assertEqual(spected_data['fob_prox_parcial'], data['fob_prox_parcial'])
        self.assertEqual(spected_data['gasto_origen_prox_parcial'], data['gasto_origen_prox_parcial'])
        self.assertEqual(spected_data['saldo_inicial_lp'], data['saldo_inicial_lp'])
        self.assertEqual(spected_data['id_parcial'], data['id_parcial'])