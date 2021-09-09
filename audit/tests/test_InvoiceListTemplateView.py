from audit.views import InvoiceListTemplateView
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase


class InvoiceListTemplateViewTEST(TestCase):

    def setUp(self):
        self.path = '/auditoria/'
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')
        return super().setUp()

    def test_get(self):
        request = self.factory.get(self.path)
        request.user = self.user
        response = InvoiceListTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('audit/listado-facturas.html')
        self.assertIsInstance(response.context_data['data'], dict)

    def test_user_not_logged(self):
        request = self.factory.get(self.path)
        request.user = AnonymousUser()
        response = InvoiceListTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=' + self.path)