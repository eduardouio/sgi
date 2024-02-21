from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from logs.app_log import loggin
from products.forms import ProductFormModel
from products.models import Product


# /producto/modificar/<pk>/
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductFormModel
    success_url = '/productos/ver/{}/?edit=true'
    template_name = 'products/form-producto.html'

    def get(self, request, pk, *args, **kwargs):
        loggin('i', 'Solicitando formulario edicion')
        self.object = self.get_object(**kwargs)
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Editar Producto {}'.format(
                self.object.nombre)
        }
        return self.render_to_response(context)

    def form_valid(self, form):
        product = form.save(commit=False)
        if not product.date_create:
            product.date_create = datetime.today()

        if not product.last_update:
            product.last_update = datetime.today()

        product.save()
        loggin('i', 'Producto {} actualizado'.format(product.nombre))
        return HttpResponseRedirect(self.success_url.format(
            self.request.path.split('/')[3]
        ))

    def form_invalid(self, form):
        loggin('e', 'No se puede actualizar el producto')
        context = self.get_context_data(form=form)
        context['data'] = {
            'title_page': 'Error en formulario'
        }
        return self.render_to_response(context)


