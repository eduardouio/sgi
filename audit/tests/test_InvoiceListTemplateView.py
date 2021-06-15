from django.test import Client, TestCase


class InvoiceListTemplateViewTEST(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.login(username='eduardo', password='elian.2011')
        return super().setUp()

    def test_get(self):
        response = self.client.get('/auditoria/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.template_name[0], 'audit/listado-facturas.html'
        )

    def test_getanonymus(self):
        client = Client()
        response = client.get('/auditoria/')
        self.assertEqual(response.status_code, 302)