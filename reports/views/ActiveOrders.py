from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import OrderDetailProductSale
from orders.models import Order, OrderInvoiceDetail
from logs.app_log import loggin


#reportes/activos/
class ActiveOrdersTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/reporte-pedidos-activos.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        orders = Order.get_all()
        order_sale = OrderDetailProductSale()
        data = []

        for my_ord in orders:
            my_order_sale = order_sale.get(my_ord.nro_pedido, True)
            my_order_sale['total_sale'] = 0

            for item in my_order_sale['sale']:
                my_order_sale['total_sale'] += item['nro_cajas']

            if my_order_sale['total_sale']:
                data.append({
                    'order': my_ord,
                    'sale': my_order_sale
                })

            if my_order_sale['total_sale'] == 0 and my_ord.bg_isclosed == 0:
                loggin('i', 'Se cierra el pedido {} por no saldo'.format(
                    my_ord.nro_pedido)
                )
                my_ord.bg_isclosed = 1
                my_ord.save()

        context['data'] = {
            'title_page': 'Pedidos Activos',
            'data': data,
            }
        return self.render_to_response(context)
