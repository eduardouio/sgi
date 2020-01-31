from django.test import TestCase, Client
from audit.views import InvoiceListTemplateView
from logs import loggin 


class InvoiceListTemplateViewTEST(TestCase):

    def setUp(self):
        self.client = Client()
        self.invoice_list_template_view = InvoiceListTemplateView()
        return super().setUp()
    
    def test_get(self):
        response = self.client.get('auditoria/')
        loggin('t', response.get)
        self.assertEqual(response.status_code, 200)

    
    def test_get_local(self):
        self.assertTrue(self.invoice_list_template_view.get_local())
