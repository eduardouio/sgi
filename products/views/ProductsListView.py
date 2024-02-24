"""
    Listado completo de productos activos
"""

from django.views.generic import ListView
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from datetime import date
from django.http import HttpResponse


# /productos/
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/lista-productos.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Mostrando lista de productos')
        self.object_list = []
        for item in self.get_queryset():
            estado = 'Activo' if item.estado == 1 else 'Inactivo'
            if item.fecha_vencimiento_registro:
                if item.fecha_vencimiento_registro < date.today():
                    loggin(
                        'w', f'Producto {item.nombre} con registro caducado')
                    estado = 'Caducado'

                elif item.fecha_vencimiento_registro.year == date.today().year:
                    if item.fecha_vencimiento_registro.month - date.today().month < 3:
                        estado = 'Por Caducar'

            self.object_list.append({
                'cod_contable': item.cod_contable,
                'nombre': item.nombre,
                'estado': estado,
                'identificacion_proveedor': item.identificacion_proveedor.nombre,
                'cantidad_x_caja': item.cantidad_x_caja,
                'nro_registro_sanitario': item.nro_registro_sanitario,
                'fecha_vencimiento_registro': item.fecha_vencimiento_registro,
                'cod_ice': item.cod_ice,

            })

        order_estado = ['Por Caducar', 'Caducado', 'Activo', 'Inactivo']
        self.object_list = sorted(
            self.object_list, key=lambda k: order_estado.index(k['estado'])
        )
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Listado Productos'
        }
        return self.render_to_response(context)
