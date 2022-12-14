from django.test import TestCase
from costings.lib_src import LedgerOrder

class TEST_LedgerOrder(TestCase):

    def setUp(self):
        self.ledger_order = LedgerOrder()

    def test_sale(self):
        spected_data = {
            'product': {
                'initial_sale': 62544.75,
                'downloaded': 44458.50,
                'sale': 18086.25,
            },
            'expenses':{
                'initial_sale': 35232.025,
                'downloaded':   30752.89,
                'sale': 4479.14,
                'justified': 35200.02,
            },
        }
        ledger_report = self.ledger_order.get_sale('272-21')
        self.assertEqual(spected_data['product'], ledger_report['product'])
        self.assertEqual(spected_data['expenses'],ledger_report['expenses'])

    def test_order_does_exist(self):
        pass