from django.test import Client, TestCase

from reports.views import ICEReportTemplateView


class ICEReportTemplateViewTEST(TestCase):

    def setUp(self):
        self.report = ICEReportTemplateView()
        self.client = Client()
        return super().setUp()

    def test_get(self):
        response = self.client.get('/reportes/ice/2020/1')
        # self.assertTemplateUsed(response, 'reports/reporte_ice.html')
        self.assertEqual(200, response.status_code)
