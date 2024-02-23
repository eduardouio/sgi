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
            if item.fecha_vencimiento_registro:
                if item.fecha_vencimiento_registro < date.today():
                    loggin('w', f'Producto {item.nombre} con registro caducado')
                    item.estado = 0
            self.object_list.append(item)

        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Listado Productos'
        }
        return self.render_to_response(context)
