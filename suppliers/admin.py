from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from suppliers.models.Supplier import Supplier


class SupplierAdmin(SimpleHistoryAdmin):
    list_display = (
        'nombre',
        'tipo_provedor',
        'moneda_transaccion',
        'categoria',
        'comentarios',
        'id_user',
        'date_create',
    )

    search_fields = (
        'nombre',
        'tipo_provedor',
        'moneda_transaccion',
        'categoria',
    )

    list_filter = (
        'nombre',
        'tipo_provedor',
        'moneda_transaccion',
        'categoria',
    )

admin.site.register(Supplier, SupplierAdmin)
