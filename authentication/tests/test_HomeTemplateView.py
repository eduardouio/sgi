from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser

from authentication.views import HomeTemplateView
from sgi.settings import EMPRESA


class TESTHomeTemplateView(TestCase):

    def setUp(self):
        self.path = '/home/'
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')
        return super().setUp()

    def test_get(self):
        request = self.factory.get(self.path)
        request.user = self.user
        response = HomeTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context_data['data'], dict)
        self.assertEqual(
            'SGI ' + EMPRESA['nombre'],
            response.context_data['data']['title_page']
        )
        self.assertTemplateUsed('base/home.htm')

    def test_user_not_logged(self):
        request = self.factory.get(self.path)
        request.user = AnonymousUser()
        response = HomeTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=' + self.path)
