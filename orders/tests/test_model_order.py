from django.test import TestCase
from orders.models.Order import Order
from datetime import datetime
from django.db.models.query import QuerySet
from lib_src.populate_test_database import populate_all

class TestModelOrder(TestCase):
    
    def setUp(self):

        return super().setUp()
    
    def tearDown(self):
        
        return super().tearDown()
    
    def test_create_orders(self):
    