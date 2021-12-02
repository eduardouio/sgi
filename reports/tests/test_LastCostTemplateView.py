from django.test import TestCase, RequestFactory
from reports.views import LastCostTemplateView
from django.contrib.auth.models import User, AnonymousUser


class TESTLastCostTemplateView(TestCase):

    def setUp(self) -> None:
        self.path = '/reportes/ultimo-costo'
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')
        return super().setUp()

    def test_get_context_data(self):
        requets = self.factory.get(self.path)
        requets.user = self.user
        response = LastCostTemplateView.as_view()(requets)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('reports/last_cost.html')
        self.assertEqual(
            response.context_data['data']['title_page'],
            'Ultimo Costo Inventario'
        )
        self.assertEqual(
            response.context_data['data']['report'].__len__(),
            197
        )

    def test_annonymous_user(self):
        requets = self.factory.get(self.path)
        requets.user = AnonymousUser()
        response = LastCostTemplateView.as_view()(requets)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/reportes/ultimo-costo')
