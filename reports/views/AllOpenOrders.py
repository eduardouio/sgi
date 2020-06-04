from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from orders.models import Order
from lib_src import CloseOpenOrdersWithoutProduct


# /reportes/pedidos/abiertos/
class AllOpenOrders(LoginRequiredMixin, TemplateView):
    '''
    Retorna todos los pedidos abiertos en el sistema
    '''
    template_name = 'reports/pedidos-abiertos.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        open_orders = Order.get_all()
        orders = []
        for o in open_orders:
            isopen = CloseOpenOrdersWithoutProduct().check_order(o.nro_pedido)
            if not isopen:
                orders.append(o)
        context['data'] = {
            'title_page': 'Pedidos Abiertos',
            'data': orders
            }
        return self.render_to_response(context)
