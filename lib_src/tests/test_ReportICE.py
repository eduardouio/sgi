from django.test import TestCase
from lib_src import ReportICE
from logs import loggin

class ReportICETEST(TestCase):

    def setUp(self):
        self.report_ice = ReportICE(2020,1)
        return super().setUp()
    
    def test_almacenera(self):
        spected_orders = [
                            '379-19',
                            '372-19',
                            '388-19',
                            '384-19',
                            '382-19',
                            '383-19',
                            '385-19',
                            '381-19',
                            '375-19',
                            '380-19',
                            '369-19',
                            '373-19',
                            '386-19',
                            '378-19',
                            '377-19',
                            '371-19',
                            '370-19',
                            '389-19',
                            '374-19',
                            '376-19',
                            '387-19',
                            '312-19',
                            '312-19',
                            '313-19',
                            '313-19',
                            '313-19',
                            '313-19',
                        ]
        
        rows = self.report_ice.get_almacenera()
        self.assertEqual(spected_orders.__len__(), rows.__len__())
    

    def test_get_consumo(self):
        spected_data = []
        data = self.report_ice.get_consumo()
        self.assertEqual(spected_data, data)
    

    def test_get_partials(self):
        spected_data = [
            '382-19',
            '383-19',
            '340-18',
            '380-19',
            '369-19',
            '381-19',
            '375-19',
            '385-19',
            '359-19',
            ]
        data = self.report_ice.get_partials()

        self.assertEqual(spected_data.__len__(), data.__len__())