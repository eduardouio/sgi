from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TESTAllOrders(APITestCase):

    def setUp(self):
        self.path = '/api/orders/all/'
        self.user = User.objects.get(username='eduardo')
        return super().setUp()

    def test_get(self):
        self.client.login(username='eduardo', password='elian.2011')
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_user_not_loggin(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 403)
