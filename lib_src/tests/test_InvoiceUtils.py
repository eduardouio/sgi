import pdb

from django.test import TestCase
from lib_src import InvoicesUtils


class InvoiceUtilsTEST(TestCase):

    def setUp(self):
        return super().setUp()

    def test_unapproved_invoices(self):
        spected_data = 284
        data = InvoicesUtils().get_unapproved_invoices()
        self.assertIsInstance(data, list)
        self.assertEqual(spected_data, data.__len__())

    def test_approved_invoices(self):
        spected_data = 8875
        data = InvoicesUtils().get_approved_invoices()
        self.assertIsInstance(data, list)
        self.assertEqual(spected_data, data.__len__())
