from django.test import TestCase
from costings.lib_src import LedgerOrder


class LedgerOrderTest(TestCase):

    def test_dont_exist_order(self):
        sale = LedgerOrder().get_sale('000000')
        self.assertEqual(sale, None)

        sale = LedgerOrder().get_sale('999-10')
        self.assertEqual(sale, None)

    def test_orderr70_with_partials(self):
        spected = {
            'nro_order': '309-19',
            'fob_tct': 12359.04,
            'expenses': 2805.40,
            'sale': 15164.44,
        }
        recived = LedgerOrder().get_sale('309-19')
        self.assertDictEqual(spected, recived)

    def test_order70_without_partials(self):
        spected = {
            'nro_order': '069-20',
            'fob_tct': 47824.00,
            'expenses': 9506.38,
            'sale': 57330.38,
        }
        recived = LedgerOrder().get_sale('069-20')
        self.assertDictEqual(spected, recived)

    def test_order70_euros(self):
        spected = {
            'nro_order': '318-19',
            'fob_tct': 42266.25,
            'expenses': 7623.95,
            'sale': 49890.20,
        }
        recived = LedgerOrder().get_sale('318-19')
        self.assertDictEqual(spected, recived)

    def test_order70_euros_wit_partials(self):
        spected = {
            'nro_order': '148-19',
            'fob_tct': 44520.00,
            'expenses': 7429.75, # Se fuerza el total por reliq de ice
            'sale': 51949.75,
        }
        recived = LedgerOrder().get_sale('148-19')
        self.assertDictEqual(spected, recived)

    def test_order10_witouth_invoice(self):
        spected = {
            'nro_order': '193-20',
            'fob_tct': 0,
            'expenses': 92.81, # Se fuerza el total por reloq de ice
            'sale': 92.81,
        }
        recived = LedgerOrder().get_sale('193-20')
        self.assertDictEqual(spected, recived)
