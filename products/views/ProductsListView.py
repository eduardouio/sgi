"""
Listado completo de productos activos
"""

from django.views.generic import ListView
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from django.http import Http404


# /productos/
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/lista-productos.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset(**kwargs)
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Listado Productos'
        }
        return self.render_to_response(context)
