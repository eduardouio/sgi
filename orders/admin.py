from django.contrib import admin
from django.utils.html import format_html
from simple_history.admin import SimpleHistoryAdmin

from orders.models import Order, OrderInvoice, OrderInvoiceDetail


class OrderAdmin(SimpleHistoryAdmin):
    empty_value_display = ''
    list_display = (
        'proveedor',
        'nro_pedido',
        'incoterm',
        'regimen',
        'flete_aduana',
        'seguro_aduana',
        'nro_aplicacion',
        'nro_poliza',
        'incoterm',
        'pais_origen',
        'ciudad_origen',
        'fecha_arribo',
        'liquidar',
    )
    readonly_fields = [
        'nro_liquidacion', 'exoneracion_arancel',
        'fodinfa', 'fodinfa_pagado',
        'ice_especifico', 'ice_especifico_pagado',
        'ice_advalorem', 'ice_advalorem_pagado',
        'iva', 'iva_pagado', 
        ]

    def liquidar(self, obj):

        return format_html(
                '<a href="/pedidos/ficha/{name_link}/" class="grp-button grp-default">📁 <small>Ficha</small></a>'
                .format(name_link=obj.nro_pedido)
                )

    search_fields = [
        'nro_pedido',
        'regimen',
        'proveedor',
        'pais_origen',
        'ciudad_origen',
        'fecha_arribo',
        'incoterm',
        'nro_matricula',
        ]

    list_filter = (
        'proveedor',
        'pais_origen',
        'ciudad_origen',
        'incoterm',
    )


class OrderInvoiceDetailInline(admin.TabularInline):
    model = OrderInvoiceDetail


class OrderInvoiceAdmin(SimpleHistoryAdmin):
    list_display = (
        'identificacion_proveedor',
        'nro_pedido',
        'id_factura_proveedor',
        'fecha_emision',
        'valor',
        'moneda',
        'tipo_cambio',
        'vencimiento_pago',
        'date_create',
    )

    search_fields = (
        'proveedor',
        'fecha_emision',
        'id_factura_proveedor',
    )

    list_filter = (
        'identificacion_proveedor',
        'moneda',
        'nro_pedido__nro_refrendo',
    )

    inlines = [OrderInvoiceDetailInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderInvoice, OrderInvoiceAdmin)
