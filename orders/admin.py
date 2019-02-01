from django.contrib import admin
from orders.models.Order import Order
from orders.models.OrderInvoice import OrderInvoice
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html


class OrderAdmin(admin.ModelAdmin):
    empty_value_display = '-Sin Valor-'
    list_display = (
        'proveedor',
        'nro_pedido',
        'incoterm',
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
        return format_html('<a href="/costos/pedido/{name_link}">{name_link}</a>'.format(name_link=obj.nro_pedido))    

    search_fields = [
        'nro_pedido',
        'regimen',
        'proveedor',
        'pais_origen',
        'ciudad_origen',
        'fecha_arribo',
        'incoterm',
        'matricula',
        ]
    
    list_filter = (
        'proveedor',
        'pais_origen',
        'ciudad_origen',
        'incoterm',
    )
    
    fields = (
        ('nro_pedido','pais_origen','ciudad_origen'),
        ('regimen', 'incoterm', 'proveedor'),
        ('dias_libres', 'fecha_salida_origen', 'fecha_arribo'),
        ('naviera', 'punto_lledada', 'nro_refrendo',),
        ('nro_bl','nro_matricula','numero_de_carga_mrn'),
        ('flete_aduana','seguro_aduana','gasto_origen', 'otros'),
        ('fecha_salida_bodega_puerto', 'fecha_ingreso_almacenera','fecha_salida_almacenera','fecha_liquidacion'),
        ('fecha_declaracion_inicial','fecha_ingreso_puerta','fecha_movilizacion_contenedor'),
        ('fecha_entrega_etiquetas_senae',
        'fecha_pegado_etiquetas',
        'fecha_aforo_fisico',
        'fecha_llegada_documentos'),
        'fecha_salida_autorizada_puerto',
        'fecha_aprovacion_dai',
        'fecha_llegada_cliente',
        'comentarios',
        'observaciones',
        'nro_liquidacion',
        'fodinfa_pagado',
        'ice_advalorem_pagado',
        'ice_especifico_pagado',
        'arancel_especifico_pagar_pagado',
        'arancel_advalorem_pagar_pagado',
        'base_arancel_advalorem',
        'base_arancel_especifico',
        'base_ice_especifico',
        'base_ice_advalorem',
        'porcentaje_ice_advalorem',
        'base_etiquetas',
        'notas_cierre',
        
        'url_dai_1',
        'url_dai_2',
        'url_dai_3',
        'path_dai_1',
        'path_dai_2',
        'path_dai_3',


        'agente_aduana',
        'ruc_agente_aduana',
        'etiquetas_pegadas',
        'bg_have_tasa_control',
        'bg_isliquidated',
        'bg_isclosed',
        'bg_haveexpenses',
        'have_etiquetas_fiscales',
        'id_user',
        'date_create',
        'last_update',
    )

class OrderInvoiceDetailInline(admin.TabularInline):
    fields = (
        'id_pedido_factura',
        'cod_contable',
        'nro_cajas',
        'costo_caja',
        'peso',
    )
    model = OrderInvoiceDetail

class OrderInvoiceAdmin(admin.ModelAdmin):
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
    )

    inlines = [ OrderInvoiceDetailInline ]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderInvoice, OrderInvoiceAdmin)