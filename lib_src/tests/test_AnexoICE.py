from django.test import TestCase
from lib_src import AnexoICE


class AnexoICETEST(TestCase):

    def setUp(self):
        self.anexo_ice = AnexoICE(2020,2)
        return super().setUp()

    def test_get_report(self):
        self.anexo_ice.get()

