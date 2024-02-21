from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from logs.app_log import loggin
from products.forms import ProductFormModel
from products.models import Product


# /productos/crear/
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductFormModel
    success_url = '/productos/ver/{}/?created=true'
    template_name = 'products/form-producto.html'

    def get_context_data(self, **kwargs):
        loggin('i', 'Registrando nuevo Producto')
        context = super().get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Nuevo Producto',
            'new_id': Product.get_new_id_producto(),
        }
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        if not product.date_create:
            product.date_create = datetime.today()

        if not product.last_update:
            product.last_update = datetime.today()

        product.save()
        loggin('i', 'Producto {} actualizado'.format(product.nombre))
        return HttpResponseRedirect(self.success_url.format(
            product.cod_contable
        ))

    def form_invalid(self, form):
        loggin('e', 'No se puede crear el producto')
        context = self.get_context_data(form=form)
        context['data'] = {
            'title_page': 'Error en formulario'
        }
        return self.render_to_response(context)
