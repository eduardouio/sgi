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
        updated = False
        created = False

        if request.GET.get('edit') == 'true':
            updated = True

        if request.GET.get('created') == 'true':
            created = True

        context['data'] = {
            'title_page': 'Producto | {}'.format(self.object),
            'updated': updated,
            'created' : created
        }
        return self.render_to_response(context)
