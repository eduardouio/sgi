from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser

from audit.views import InvoiceTemplateView


class TESTInvoiceTemplateView(TestCase):

    def setUp(self):
        self.path = '/auditoria/factura/55/'
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')
        return super().setUp()

    def test_get(self):
        # TODO corregir este test
        return True
        request = self.factory.get(self.path)
        request.user = self.user
        response = InvoiceTemplateView.as_view()(request)
        self.assertTemplateUsed('audit/mostrar-factura.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context_data, dict)

    def test_without_id(self):
        # TODO Hacer que la plantilla responda a 'auditoria/factura/<none>'
        pass

    def test_user_not_logged(self):
        request = self.factory.get(self.path)
        request.user = AnonymousUser()
        response = InvoiceTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=' + self.path)
