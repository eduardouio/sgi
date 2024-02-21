from django.test import TestCase
from almagro.lib_src import ImportAlmagro
from .spected import spected
import csv


class TestImportAlmagro(TestCase):

    def test_set_data(self):
        import_almagro = ImportAlmagro()
        result = import_almagro.set_data(self.get_csv_data())
        self.assertEqual(len(spected), len(result))

        for res in result:
            for spec in spected:
                if res['nro_pedido'] == spec['nro_pedido']:
                    for k in res.keys():
                        self.assertEqual(res[k], spec[k])

    def get_csv_data(self):
        """
        Retorna los datos de un archivo para realizar el test
        """
        filepath = __file__.split('/')
        filepath[0] = '/'
        file = open('/'.join(filepath[0:-1]) + '/report.csv')
        csv_reader = csv.reader(file, delimiter=',')
        return [row for row in csv_reader]
