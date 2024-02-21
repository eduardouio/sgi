from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from products.models import Product


class ProductAdmin(SimpleHistoryAdmin):
    list_display = (
        'identificacion_proveedor',
       # 'identificacion_proveedor__nombre',
        'cod_contable',
        'nombre',
        'nro_registro_sanitario',
        'grado_alcoholico',
        'capacidad_ml',
        'cantidad_x_caja',
        'costo_caja',
    )

    search_fields = (
        'cod_contable',
        'nombre',
        'grado_alcoholico',
        'capacidad_ml',
        'nro_registro_sanitario',
        'identificacion_proveedor__nombre',
    )

    list_filter = (
        'capacidad_ml',
        'pais_origen',
        'cantidad_x_caja',
        'custodia_doble',
        'estado',
    )


admin.site.register(Product, ProductAdmin)
