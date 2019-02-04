from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from products.models.Product import Product

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



admin.site.register(Product, ProductAdmin)
