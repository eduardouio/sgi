from django.test import TestCase
from logs import loggin
from costings.views import LedgerReportView

class LedgerReportViewTEST(TestCase):

    def setUp(self):
        self.ledger_report_view = LedgerReportView()
        return super().setUp()

    def test_algo(self):
        self.assertEqual(1,1)