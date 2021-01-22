"""
    Formulario de edicion de producto
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from logs.app_log import loggin
from products.models import Product


# /producto/modificar/<pk>/
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('__all__')
    success_url = '/producto/<pk>/'
    template_name = 'products/editar-producto.html'

    def get(self, request, pk, *args, **kwargs):
        loggin('i', 'Solicitando formulario edicion')
        self.object = self.get_object(**kwargs)
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Editar Producto {}'.format(
                self.object.nombre)
        }
        return self.render_to_response(context)


# TODO Corregir modelo de producto para que se conecte con id_producto
