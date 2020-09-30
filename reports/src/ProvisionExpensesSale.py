from paids.models import PaidInvoiceDetail, Expense


class ProvisionExpensesSale():

    def get_all_expenses(self):
        report = []
        expenses = Expense.objects.all()
        for exp in expenses:
            pass
        return report

    def get_paids_from_expense(self):
        pass
