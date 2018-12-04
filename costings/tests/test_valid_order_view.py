from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse
from costings.views import *

class testValidOrder(TestCase):
    def test_status_page(self):
        response = self.client.get('/costos/liquidar/pedido/013-12')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Contabilizar Gastos Cierre Pedido')
    
    def test_correct_template(self):
        response = self.client.get('/costos/liquidar/pedido/013-12')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'base/base.html')
    
    def test_get_order_data(self):
        pass