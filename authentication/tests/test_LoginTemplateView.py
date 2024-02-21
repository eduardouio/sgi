from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from authentication.views import LoginTemplateView


class TESTLoginTemplateView(TestCase):

    def setUp(self):
        self.path = '/login/'
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
        request.user = AnonymousUser()
        response = LoginTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('base/login-form.html')

    def test_auth_login_in(self):
        request = self.factory.get(self.path)
        request.user = self.user
        response = LoginTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('base/login-form.html')
        self.assertEqual(response.url, '/')

    def test_post(self):
        form_data = {
            'username': 'eduardo',
            'password': 'elian.2011'
        }
        request = self.factory.post('/login/', data=form_data)
        request.user = self.user
        self.setup_request(request)
        response = LoginTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_post_fail(self):
        form_data = {
            'username': 'error',
            'password': 'errr-pass'
        }
        request = self.factory.post('/login/', data=form_data)
        request.user = self.user
        self.setup_request(request)
        response = LoginTemplateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '?error=true')
