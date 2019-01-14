from django.shortcuts import render_to_response
from multiprocessing import context

from django.views.generic import TemplateView
from xdg.Locale import update

from lib_src.OrderSale import OrderSale
from orders.models.Order import Order


class OrderSaleTemplateView(TemplateView):
    template_name = "orders/saldo_pedido.html"

    def get(self, request, nro_order, *args, **kwargs):
        order = Order.get_by_order(nro_order)
        context = self.get_context_data(**kwargs)

        if order is None:
            data = {
                'title_page': 'Pedido No encontrado',
            }
            context.update({'data': data})
            return self.render_to_response(context)
        
        data = OrderSale().get_all_data(nro_order)
        data['title_page'] = 'Saldo Pedido {}'.format(nro_order)
        context.update({'data':data})
        return self.render_to_response(context)