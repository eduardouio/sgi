from django.test import TestCase
from costings.lib_src import LoadFileReport


class TestLoadFileReport(TestCase):

    def test_read(self):
        lfr = LoadFileReport()
        file = open('costings/test/sri_data/ice.xls', 'r')
        ipdb
        self.assertEqual('', None)