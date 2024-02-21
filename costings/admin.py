from django.contrib import admin
from costings.models.Ledger import Ledger


class LedgerAdmin(admin.ModelAdmin):
    list_display = (
        'tipo',
        'nro_pedido',
        'id_parcial',
        'costo_inicial_producto',
        'costo_producto',
        'descargas',
        'saldo_producto',
        'precio_entrega',
        'mayor_sap',
        'provisiones_sap',
        'mayor_sgi',
    )

    search_fields = [
        'tipo',
        'id_parcial',
        'nro_pedido__nro_pedido',
    ]


admin.site.register(Ledger, LedgerAdmin)
