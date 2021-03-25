from costings.views import ICEXmlFormView
import os

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client


class ICEXmlFormViewTEST(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.get(username='eduardo')
        self.client = Client()

    def test_get(self):
        request = self.factory.get('/costos/ice-xml/')
        request.user = AnonymousUser()
        response = ICEXmlFormView.as_view()(request)

        # comprobamos que un usuario no autorizado ingrese
        self.assertEqual(response.status_code, 302)

        # comprobamos para usuario registrado
        request.user = self.user
        response = ICEXmlFormView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('costings/ice-xml.html', response.template_name[0])

    def test_post(self):
        path = os.path.abspath('.')
        file_upload = open(
            path + '/media/docs/ejemplo_reporte.xls',
            'r',
            encoding='iso-8859-1'
        )
        self.client.login(username='eduardo', password='elian.2011')
        response  = self.client.post('/costos/ice-xml/', {'file': file_upload})

        import ipdb;ipdb.set_trace()
