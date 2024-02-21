from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from authentication.views import LogoutRedirectView


class TESTLogoutRedirect(TestCase):

    def setUp(self):
        self.path = '/logout/'
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')
        return super().setUp()

    def setup_request(self, request):
        s_middleware = SessionMiddleware()
        s_middleware.process_request(request)
        request.session.save()

        m_middleware = MessageMiddleware()
        m_middleware.process_request(request)
        request.session['algo'] = 'algo'
        request.session.save()

    def test_get(self):
        request = self.factory.get(self.path)
        request.user = self.user
        self.setup_request(request)
        response = LogoutRedirectView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_user_not_logged(self):
        request = self.factory.get(self.path)
        request.user = AnonymousUser()
        response = LogoutRedirectView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/login/?next=/logout/')
