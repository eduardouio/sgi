from django.contrib import admin
from orders.models.Order import Order
from orders.models.OrderInvoice import OrderInvoice
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html
from django.conf import settings

class OrderAdmin(admin.ModelAdmin):
    empty_value_display = '-Sin Valor-'
    list_display = (
        'nro_pedido',
        'incoterm',
        'proveedor',
        'regimen',
        'flete_aduana',
        'seguro_aduana',
        'incoterm',
        'pais_origen',
        'ciudad_origen',
        'fecha_arribo',
        'liquidar',   
    )

    def liquidar(self, obj):
        return format_html('<a href="{base_url}costos/pedido/{name_link}">{name_link}</a>'.format(base_url= settings.BASE_URL,name_link=obj.nro_pedido))    

    search_fields = [
        'nro_pedido',
        'regimen',
        'proveedor',
        'pais_origen',
        'ciudad_origen',
        'fecha_arribo',
        'incoterm',
        ]
    
    fields = (
        'nro_pedido', 'incoterm',
        'regimen','pais_origen',
        'flete_aduana', 'seguro_aduana',
        'ciudad_origen','fecha_arribo',
        'fecha_salida_bodega_puerto','fecha_ingreso_almacenera',
        'dias_libres','fecha_salida_almacenera',
        'comentarios', 'observaciones',
        'tipo_cambio_impuestosr10', 'tipo_cambio_almacenerar70',
        'nro_refrendo'
    )


class OrderInvoiceAdmin(admin.ModelAdmin):
    pass


class OrderInvoiceDetailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderInvoice, OrderInvoiceAdmin)
admin.site.register(OrderInvoiceDetail, OrderInvoiceDetailAdmin)