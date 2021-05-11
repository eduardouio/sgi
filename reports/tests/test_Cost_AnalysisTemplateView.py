from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from reports.views import CostAnalysisTemplateView


class TESTCostAnalysisTemplateView(TestCase):

    def setUp(self):
        self.path = '/reportes/analisis-costos/'
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')

    def test_get(self):
        request = self.factory.get(self.path)
        request.user = self.user
        response = CostAnalysisTemplateView.as_view()(request)

        self.assertEqual(response.context_data['data']['product'], None)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('reports/costs_analysis.html')

    def test_get_with_products(self):
        request = self.factory.get(
            self.path + '?products=02012130020202010750'
        )
        request.user = self.user
        response = CostAnalysisTemplateView.as_view()(request)
        self.assertEqual(
            response.context_data['data']['product'].nombre,
            'WHISKY SOMETHING SPECIAL'
        )
        self.assertTemplateUsed('reports/costs_analysis.html')
        self.assertIsInstance(response.context_data['data']['report'], list)

    def test_user_logged_in(self):
        request = self.factory.get(self.path)
        request.user = AnonymousUser()
        response = CostAnalysisTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
