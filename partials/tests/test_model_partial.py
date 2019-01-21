from django.test import TestCase

from logs.app_log import loggin
from partials.models.Partial import Partial


class TestModelParcial(TestCase):        

    def setUp(self):
        loggin('t', 'Iniciando testeo clase DB Partial')
        return super().setUp()

    def test_get_last_partial(self):
        spected_values = {
            '192-18' : None,
            '071-18' : 294,
            '198-18' : 265,
            '345-18' : None,
            '344-18' : 284,
            '345-18' : None,
            '313-18' : 272,
            '254-18' : 282,
        }

        for i in spected_values:
            last_partial = Partial.get_last_partial(i)
            id_partial =  last_partial.id_parcial if  last_partial else None 
            self.assertEqual(spected_values[i], id_partial)
    

    def test_get_last_closed_partial(self):
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
            last_partial = Partial.get_last_close_partial(i)
            id_partial = last_partial.id_parcial if last_partial else None
            self.assertEqual(spected_values[i], id_partial)