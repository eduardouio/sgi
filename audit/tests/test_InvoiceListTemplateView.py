import pdb

from django.test import Client, TestCase

from audit.views import InvoiceListTemplateView
from django.contrib.a
from logs import loggin


class InvoiceListTemplateViewTEST(TestCase):

    def setUp(self):
        self.client = Client()
        self.invoice_list_template_view = InvoiceListTemplateView()
        return super().setUp()

    def test_get(self):
        response = self.client.get('auditoria/')
        pdb.set_trace()
        loggin('t', response.get)
        self.assertEqual(response.status_code, 200)

    def test_get_local(self):
        pass
