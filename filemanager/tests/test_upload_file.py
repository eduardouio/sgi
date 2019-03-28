from filemanager.views import UploadFileView
from django.test import TestCase, Client
from logs.app_log import loggin


class UploadFileViewTest(TestCase):

    def test_get(self):
        response = self.client.get('/archivos/subir/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'filemanager/frm_subir_archivos.html')
        self.assertContains(response, '')
        self.assertDictEqual(response.context_data['data'], {
            'title_page' : 'Subir Archivos',
            'host': 'http://179.49.60.158:5001',
        })
