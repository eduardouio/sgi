from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product


# /productos/ver/{id_producto}
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/ver-producto.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['data'] = {
            'title_page': 'Producto | {}'.format(self.object),
        }
        return self.render_to_response(context)
