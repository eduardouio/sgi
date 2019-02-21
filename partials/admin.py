from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from partials.models import (Apportionment, ApportionmentDetail, InfoInvoice,
                             InfoInvoiceDetail, Partial)


class PartialAdmin(SimpleHistoryAdmin):
    list_display = (
        'nro_pedido',
        'nro_refrendo',
        'fecha_llegada_cliente',
        'bg_isliquidated',
        'bg_isclosed',
        'agente_aduana',
    )

    list_filter=(
        'nro_pedido',
        'bg_isliquidated',
        'bg_isclosed',
        'agente_aduana',
    )

    search_fields = (
        'bg_isliquidated',
        'bg_isclosed',
        'agente_aduana',
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

class InfoInvoiceDetailAdmin(admin.ModelAdmin):
    pass

class InfoInvoiceAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_parcial',
        'nro_factura_informativa',
        'identificacion_proveedor',
        'fecha_emision',
        'flete_aduana',
        'seguro_aduana',
        'valor',
        'gasto_origen',
        'moneda',
        'nro_refrendo',
    )

    search_fields = (
        'nro_refrendo',
        'nro_factura_informativa',
    )

    list_filter = (
        'id_parcial',
    )

    inlines = [ InfoInvoiceDetailInline]


admin.site.register(Partial, PartialAdmin)
admin.site.register(Apportionment, ApportionmentAdmin)
admin.site.register(InfoInvoice, InfoInvoiceAdmin)
admin.site.register(InfoInvoiceDetail, InfoInvoiceDetailAdmin)
