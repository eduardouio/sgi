from django.contrib import admin
from .models import Order, OrderInvoice, OrderInvoiceDetail

class OrderAdmin(admin.ModelAdmin):
    pass


class OrderInvoiceAdmin(admin.ModelAdmin):
    pass


class OrderInvoiceDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderInvoice, OrderInvoiceAdmin)
admin.site.register(OrderInvoiceDetail, OrderInvoiceDetailAdmin)