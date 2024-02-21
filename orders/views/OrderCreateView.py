from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from logs.app_log import loggin
from orders.models import Order
from orders.forms import OrderFormModel


# pedidos/crear/
class OrderCreateView(CreateView, LoginRequiredMixin):
    model = Order
    form_class = OrderFormModel
    success_url = '/pedidos/ver/{}/?created=true'
    template_name = "orders/form-pedido.html"

    def get_context_data(self, **kwargs):
        loggin('i', 'Mostramos formulatio para la creacion de un pedido')
        context = super().get_context_data( **kwargs)
        context['data'] = {
            'title_page': 'Nuevo Pedido',
            'new_id': Order.get_new_id_order(),
        }
        return context
