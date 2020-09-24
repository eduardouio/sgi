import pdb

from django.contrib.auth.models import User
from django.test import Client, TestCase

from audit.views import InvoiceListTemplateView
from logs import loggin


class InvoiceListTemplateViewTEST(TestCase):

    def setUp(self):
        self.client = Client()
        self.invoice_list_template_view = InvoiceListTemplateView()
        self.user = User.objects.get(username='eduardo')
        self.client.login(username='eduardo', password='elian.2011')
        return super().setUp()

    def test_get(self):
        response = self.client.get('/auditoria/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'audit/listado-facturas.html')

    def test_get_local(self):
        self.assertEqual([],self.invoice_list_template_view.get_local())