from django.views.generic import DetailView
from products.models import Product

# /productos/ver/{id_producto}
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/ver_producto.html'

    def get(self, request , *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)