from django.test import TestCase
from lib_src.CompletePaidInfo import CompletePaidinfo
from logs.app_log import loggin

class TestCompletePaidInfo(TestCase):

    def setup_databases(self, **kwargs):
        loggin('t', 'iniciando testing')
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass


    def test_get_data(self):                
        dp = CompletePaidinfo(1164)
        data = dp.get_data()
        supplier = data['supplier']
        invoice = data['invoice']
        details = data['details']

        self.assertEqual('ALMACENERA DEL AGRO S A', supplier.nombre)
        self.assertEqual('32988', invoice.nro_factura)
        self.assertEqual(10, details.__len__())            

        for i in details:
            self.assertEqual('ETIQUETADO ESPACIO ALMAGRO', i['expense'].concepto)
            loggin('t', i['expense'].ordinal_parcial)
        self.assertEqual(75.00, float(data['value']))
        self.assertEqual(53.62, float(data['cross_value']))
        self.assertEqual(21.38, float(data['sale']))
    
    
    def test_get_serialized_data(self):
        dp = CompletePaidinfo(1164)
        data = dp.get_data(serialized=True)
        self.assertIsInstance(data, dict)