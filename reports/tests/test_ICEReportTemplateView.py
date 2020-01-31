from django.test import TestCase, Client
from reports.views import ICEReportTemplateView
import pdb

class ICEReportTemplateViewTEST(TestCase):

    def setUp(self):
        self.report = ICEReportTemplateView()
        self.client = Client()
        return super().setUp()
    
    def test_get(self):
        reponse = self.client.get('/reportes/ice/2020/01')
        pdb.set_trace()
        self.assertEqual('reports/reporte_ice.html', reponse.template_name)
        self.assertEqual(200, reponse.status_code)