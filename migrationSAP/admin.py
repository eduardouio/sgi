from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Migrations, MigrationsDetail


class MigrationsDetailAdmin(admin.TabularInline):
    model = MigrationsDetail


class MigrationsAdmin(SimpleHistoryAdmin):
    list_display = (
        'nro_pedido',
        'moneda',
        'tipo_cambio',
        'proveedor',
        'identificacion_proveedor',
        'regimen',
        'incoterm',
    )

    search_fields = [
        'nro_pedido',
        'moneda',
        'tipo_cambio',
        'proveedor',
        'identificacion_proveedor',
        'regimen',
        'incoterm',
    ]

    inlines = [MigrationsDetailAdmin]


admin.site.register(Migrations, MigrationsAdmin)
