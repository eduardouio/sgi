from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from products.models import Product

class ProductAdmin(SimpleHistoryAdmin):
    list_display = (
        'identificacion_proveedor',
        'cod_contable',
        'nombre',
        'grado_alcoholico',
        'capacidad_ml',
        'cantidad_x_caja',
        'costo_caja',
        'custodia_doble',
        'peso',
        'estado',
    )

    search_fields = (
        'cod_contable',
        'nombre',
        'grado_alcoholico',
        'capacidad_ml',
    )

    list_filter = (
        'capacidad_ml',
        'pais_origen',
        'cantidad_x_caja',
        'custodia_doble',
        'estado',
    )

#    fieldsets = (
#        (None, {
#            'classes': ('grp-collapse grp-open',),
#            "fields": (
#                ('identificacion_proveedor', 'cod_contable',),
#                ('nombre', 'cod_ice',),
#                ('capacidad_ml','cantidad_x_caja',),
#                ('costo_caja','estado',),
#                ('custodia_doble','peso',),
#                ('pais_origen','comentarios',),
#            ),
#        }),
#        ('Registro Sanitario', {
#            'classes': ('grp-collapse grp-closed',),
#            'fields' : (
#                ('registro_sanitario', 'estado_registro',),
#                ('fecha_emision_registro', 'fecha_vencimiento_registro',),
#                ('grado_alcoholico'),
#            )
#        })
#    )
#    

admin.site.register(Product, ProductAdmin)