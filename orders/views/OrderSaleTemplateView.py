from django.shortcuts import render_to_response
from multiprocessing import context

from django.views.generic import TemplateView
from xdg.Locale import update

from lib_src.OrderSale import OrderSale
from orders.models.Order import Order


class OrderSaleTemplateView(TemplateView):
    template_name = "orders/saldo_pedido.html"

    def get(self, request, *args, **kwargs):
        
        context = self.get_context_data(**kwargs)
        orders = Order.get_open_orders()
        sales_summary = []

        for o in orders:
            sales_summary.append(OrderSale().get_all_data(o.nro_pedido))


        data = {
            'title_page': 'Saldo General de Pedidos 📂',
            'sales' : sales_summary,
        }
        
        context.update({'data':data})
        return self.render_to_response(context)