from django.test import TestCase
from lib_src import ExpensesWithSale


class ExpensesWithSaleTEST(TestCase):

    def test_all_expenses(self):
        ExpensesSale = ExpensesWithSale()
        expenses = ExpensesSale.get_all_expeneses_with_sale()
        self.assertEqual(1463, expenses.__len__())
        self.assertIsInstance(expenses, list)