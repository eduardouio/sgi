from django.test import TestCase
from costings.lib_src import IceSriXml
import csv


class TestIceSriXml(TestCase):

    def setUp(self) -> None:
        self.ice_sri_xml = IceSriXml()
        return super().setUp()

    def test_set_data(self):
        """
        Comprobamos que el archivo lee correctamente los datos
        """
        file_data = open('costings/tests/sri_data/sales.txt', 'r')
        text = file_data.read()
        text = text.replace(',', '')
        data = csv.reader(text.split('\n'), delimiter=';', dialect='excel')
        data = [_ if _ else 0 for _ in data]
        clean_data = []
        for row in data:
            clean_data.append(
                [item if bool(item) else 0 for item in row]
            )
        import ipdb;   ipdb.set_trace()



