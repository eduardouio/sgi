from django.contrib import admin
from suppliers.models.Supplier import Supplier

class SupplierAdmin(admin.ModelAdmin):
    pass

admin.site.register(Supplier, SupplierAdmin)