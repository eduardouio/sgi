from django.test import TestCase
from logs.app_log import loggin
from migrationSAP.lib_src import SAPImporter


class TESTSAPImporter(TestCase):

    def test_get_orders_without_data(self):
        loggin('t', 'Iniciando pruebas del importador de SAP')
        sap_import = SAPImporter().check_orders(1987)
        self.assertListEqual(sap_import, [])

    def test_get_not_found(self):
        loggin('t', 'Iniciando pruebas del importador de SAP')
        sap_import = SAPImporter().check_orders('pedidos')
        self.assertListEqual(sap_import, [])

    def test_transform_order(self):
        loggin('t', 'comprobando pedidos del 2021')
        sap_import = SAPImporter().check_orders(2021)
        self.assertEqual('casa', sap_import)