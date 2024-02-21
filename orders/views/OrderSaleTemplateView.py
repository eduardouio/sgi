from multiprocessing import context

from django.views.generic import TemplateView

from lib_src import OrderProductSale
from orders.models import Order


class OrderSaleTemplateView(TemplateView):
    template_name = "orders/saldo_pedido.html"

    def get(self, request, *args, **kwargs):
        pass