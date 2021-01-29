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

#    fieldsets = (
#        ('Información Base', {
#            'classes': ('grp-collapse grp-open',),
#            'fields' : ( 
#                    ('nro_pedido', 'regimen', 'flete_aduana'), 
#                    ('seguro_aduana', 'gasto_origen',),
#                    ('incoterm','pais_origen','ciudad_origen',),
#                    ('fecha_salida_origen','fecha_llegada_documentos',),
#                    ('fecha_arribo','dias_libres','fecha_envio_de_documentos',),
#                    ('fecha_aprovacion_dai','fecha_declaracion_inicial',),
#                    ('fecha_aforo','fecha_salida_autorizada_puerto',),
#                    ('fecha_ingreso_puerta','fecha_salida_bodega_puerto',),
#                    ('fecha_movilizacion_contenedor','fecha_ingreso_almacenera',),
#                    ('fecha_liquidacion','fecha_entrega_etiquetas_senae',),
#                    ('fecha_pegado_etiquetas','fecha_salida_almacenera',),
#                    ('fecha_llegada_cliente','fecha_cierre',),
#                    ),
#        }),
#        ('Información Complementaria', {
#            'classes': ('grp-collapse grp-closed',),
#            'fields' : (
#                ('nro_aplicacion','nro_poliza',),
#                ('nro_refrendo', 'proveedor', 'nro_bl'),
#                ('nro_matricula', 'numero_de_carga_mrn', 'naviera'),
#                ('agente_aduana', 'ruc_agente_aduana', 'punto_lledada'),
#                ('etiquetas_pegadas', 'otros', 'tipo_cambio_almacenerar70'),
#            ),
#        }),
#        ('Detalle de Impuestos', {
#            'classes': ('grp-collapse grp-closed',),
#            'fields' : (
#                        ('nro_liquidacion', 'exoneracion_arancel', 'tipo_cambio_impuestosr10'),
#                        ('fodinfa', 'fodinfa_pagado',),
#                        ('ice_especifico', 'ice_especifico_pagado',),
#                        ('ice_advalorem', 'ice_advalorem_pagado',),
#                        ('iva', 'iva_pagado', ),
#                        ),
#        }),
#        ('Archivos Adicionales', {
#             'classes': ('grp-collapse grp-closed',),
#             'fields' : (
#                 (
#                    ('url_dai_1','path_dai_1',),
#                    ('url_dai_2','path_dai_2',),
#                    ('url_dai_3','path_dai_3',),
#                    ('url_liquidacion_1','path_liquidacion_1',),
#                    ('url_liquidacion_2','path_liquidacion_2',),
#                    ('url_liquidacion_3','path_liquidacion_3',),
#                 )
#             )
#        }),
#    )    

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
