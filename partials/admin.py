from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from partials.models import (Apportionment, ApportionmentDetail, InfoInvoice,
                             InfoInvoiceDetail, Partial)


class PartialAdmin(SimpleHistoryAdmin):
    list_display = (
        'nro_pedido',
        'nro_pedido__proveedor',
        'nro_liquidacion'
        'fecha_llegada_cliente',
        'fecha_salida_autorizada_almagro',
        'bg_isliquidated',
        'bg_isclosed',
    )

    list_filter = (
        'nro_pedido',
        'bg_isliquidated',
        'bg_isclosed',
    )

    search_fields = (
        'nro_pedido',
        'fecha_llegada_cliente',
        'nro_liquidacion'
        'bg_isliquidated',
        'bg_isclosed',
    )


class ApportionmentDetailInline(admin.TabularInline):
    model = ApportionmentDetail

    fields = (
        'id_prorrateo',
        'id_gastos_nacionalizacion',
        'tipo',
        'concepto',
        'valor_prorrateado',
        'valor_provisionado',
    )


class ApportionmentAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_parcial',
        'id_parcial___nro_pedido',
        'id_parcual___fecha_llegada_cliente',
        'porcentaje_parcial',
        'fob_inicial',
        'fob_parcial',
        'prorrateo_flete_aduana',
        'prorrateo_seguro_aduana',
    )

    list_filter = (
        'id_parcial',
    )

    inlines = [ApportionmentDetailInline]


class InfoInvoiceDetailInline(admin.TabularInline):
    model = InfoInvoiceDetail


class InfoInvoiceAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_parcial',
        'id_parcial__nro_pedido',
        'nro_factura_informativa',
        'nro_refrendo',
        'fecha_emision',
        'flete_aduana',
        'seguro_aduana',
        'valor',
    )

    search_fields = (
        'nro_refrendo',
        'nro_factura_informativa',
        'id_parcial__nro_pedido',
        'id_factura_informativa',
    )

    list_filter = (
        'id_parcial__nro_pedido',
    )

    inlines = [InfoInvoiceDetailInline]

admin.site.register(Partial, PartialAdmin)
admin.site.register(Apportionment, ApportionmentAdmin)
admin.site.register(InfoInvoice, InfoInvoiceAdmin)
