from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from paids.models.Expense import Expense
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail
from paids.models.RateExpense import RateExpense
from paids.models.RateIncoterm import RateIncoterm


class ExpensesAdmin(SimpleHistoryAdmin):
    list_display = (
    'id_gastos_nacionalizacion',
    'nro_pedido',
    'id_parcial',
    'concepto',
    'tipo',
    'valor_provisionado',
    'fecha',
    'fecha_fin',
    'bg_closed',
    )

    search_fields = (
    'id_gastos_nacionalizacion',
    'concepto',
    'tipo',
    'valor_provisionado',
    'fecha',
    )
    
    list_filter = (
        'nro_pedido',
        'id_parcial',
        'concepto',
        'tipo',
    )
    


class RateExpenseAdmin(SimpleHistoryAdmin):
    list_display = (
        'id_tarifa_gastos',
        'regimen',
        'tipo_gasto',
        'concepto',
        'valor',
        'estado',
        'pais_origen',
        'porcentaje',
        'comentarios',
        'date_create',
    )

    search_fields = (
        'id_tarifa_gastos',
        'regimen',
        'tipo_gasto',
        'concepto',
        'valor',
        'estado',
        'pais_origen',
        'porcentaje',
        'comentarios',
        'date_create',
    )

    list_filter = (
        'regimen',
        'tipo_gasto',
        'estado',
    ) 




class RateIncotermAdmin(SimpleHistoryAdmin):    
    list_display = (
        'id_incoterm',
        'tipo',
        'pais',
        'incoterms',
        'ciudad',
        'tarifa',
        'comentarios',
        'date_create',
    )
    search_fields = (
        'tipo',
        'pais',
        'incoterms',
    )
    list_filter = (
        'tipo',
        'pais',
        'incoterms',
    )


class PaidInvoiceDetailInline(admin.TabularInline):
    model = PaidInvoiceDetail


class PaidInvoiceAdmin(SimpleHistoryAdmin):
    list_display = (
        'identificacion_proveedor',
        'nro_factura',
        'fecha_emision',
        'valor',
        'tipo',
        'date_create',
        'bg_closed',
        'comentarios',
    )

    search_fields = (
        'nro_factura',
        'fecha_emision',
        'valor',
        'tipo',
    )

    list_filter = (
        'identificacion_proveedor',
        'tipo',
    )   

    inlines = [ PaidInvoiceDetailInline, ]


admin.site.register(Expense, ExpensesAdmin)
admin.site.register(RateExpense, RateExpenseAdmin)
admin.site.register(RateIncoterm, RateIncotermAdmin)
admin.site.register(PaidInvoice, PaidInvoiceAdmin)
