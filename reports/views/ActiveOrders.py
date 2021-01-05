from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import OrderDetailProductSale
from orders.models import Order
from logs.app_log import loggin
from paids.models import Expense


# reportes/activos/
class ActiveOrdersTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/reporte-pedidos-activos.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Accediendo a reportes de saldos')
        context = self.get_context_data(**kwargs)
        ignore_liquidated = False

        if request.GET:
            if request.GET.get('ignore_liquidated', 'off') == 'on':
                ignore_liquidated = True

            if request.GET.get('check_all_orders', 'off') == 'on':
                self.check_all_orders()

        orders = Order.get_open_orders()
        order_sale = OrderDetailProductSale()
        data = []

        for my_ord in orders:
            my_order_sale = order_sale.get(my_ord.nro_pedido, ignore_liquidated)
            my_order_sale['total_sale'] = 0

            for item in my_order_sale['sale']:
                my_order_sale['total_sale'] += item['nro_cajas']

            if my_order_sale['total_sale']:
                data.append({
                    'order': my_ord,
                    'sale': my_order_sale,
                    'monts': Expense.get_months_storage(my_ord.nro_pedido)
                })

        context['data'] = {
            'title_page': 'Pedidos Activos',
            'data': data,
            }
        return self.render_to_response(context)

    def check_all_orders(self):
        """comprueba todas los pedidos del sistema, cerrando los pedidos
         abiertos sin saldo y abriendo los pedidos que estén cerrados con saldo
        """
        loggin('i', 'Realizando mantenimiento de pedidos en DB')
        all_orders = Order.get_all()

        for order in all_orders:
            order_sale = OrderDetailProductSale().get(order.nro_pedido)
            order_sale['total_sale'] = 0

            for itm_sale in order_sale['sale']:
                order_sale['total_sale'] += itm_sale['nro_cajas']

            if order_sale['total_sale'] == 0:
                order.bg_isclosed = 1
            else:
                order.bg_isclosed = 0

            order.save()
