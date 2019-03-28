from django.views.generic import ListView
from orders.models import Order

class OrdersListView(ListView):
    model = Order
    template_name = 'costings/lista_pedidos.html'
    
    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())