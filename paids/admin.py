from django.contrib import admin
from .models import Expenses, RateExpense, RateIncoterm, PaidInvoice, PaidInvoiceDetail

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


admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(RateExpense, RateExpenseAdmin)
admin.site.register(RateIncoterm, RateIncotermAdmin)
admin.site.register(PaidInvoice, PaidInvoiceAdmin)
admin.site.register(PaidInvoiceDetail, PaidInvoiceDetailAdmin)



