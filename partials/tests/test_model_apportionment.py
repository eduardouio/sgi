from django.test import TestCase

from logs.app_log import loggin
from partials.models.Apportionment import Apportionment


class TestModelApportionment(TestCase):        

    def setUp(self):
        loggin('t', 'Iniciando testeo clase Prorrateos Apportionment')
        return super().setUp()

    def test_get_last_partial(self):
        spected_values = {
            '192-18' : None,
            '071-18' : 221,
            '198-18' : None,
            '345-18' : None,
            '344-18' : None,
            '345-18' : None,
            '313-18' : 272,
            '254-18' : 203,
        }

        for i in spected_values:
            last_prorrateo = Apportionment.get_last_apportionment(i)
            id_partial = last_prorrateo.id_parcial_id if last_prorrateo else None
            self.assertEqual(spected_values[i], id_partial)