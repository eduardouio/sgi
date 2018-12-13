from django.contrib import admin
from paids.models.Expense import Expense
from paids.models.RateExpense import RateExpense
from paids.models.RateIncoterm import RateIncoterm
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail


class ExpensesAdmin(admin.ModelAdmin):
    pass


class RateExpenseAdmin(admin.ModelAdmin):
    pass


class RateIncotermAdmin(admin.ModelAdmin):
    pass


class PaidInvoiceAdmin(admin.ModelAdmin):
    pass


class PaidInvoiceDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Expense, ExpensesAdmin)
admin.site.register(RateExpense, RateExpenseAdmin)
admin.site.register(RateIncoterm, RateIncotermAdmin)
admin.site.register(PaidInvoice, PaidInvoiceAdmin)
admin.site.register(PaidInvoiceDetail, PaidInvoiceDetailAdmin)



