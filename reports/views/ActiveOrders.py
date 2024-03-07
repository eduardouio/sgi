from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import OrderDetailProductSale
from orders.models import Order, OrderInvoice
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
            my_order_sale = order_sale.get(
                my_ord.nro_pedido, ignore_liquidated)
            order_invoice = OrderInvoice.get_by_order(my_ord.nro_pedido)
            my_order_sale['total_sale'] = 0
            # colores de texto en reporte
            text_color = {
                'EN TRANSITO': 'text-warning',
                'EN ALMAGRO': 'text-primary',
                'CERRADO': 'text-dark',
                'SIN CONFIRMAR': 'text-danger',
                'EN BODEGAS PARA COSTEO': 'text-primary',
            }

            for item in my_order_sale['sale']:
                my_order_sale['total_sale'] += item['nro_cajas']

            if my_order_sale['total_sale']:
                status = 'EN TRANSITO'

                if order_invoice.id_factura_proveedor.startswith('SF-'):
                    status = 'SIN CONFIRMAR'
                else:
                    # VERIFICAMOS EL STATUS DEL PEDIDO POR DEFECTO ES TRANSITO
                    if my_ord.regimen == '70' and my_ord.bg_isclosed:
                        status = 'CERRADO'

                    if my_ord.regimen == '70' and my_ord.fecha_ingreso_almacenera:
                        status = 'EN ALMAGRO'

                    if my_ord.regimen == '70' and not my_ord.fecha_ingreso_almacenera:
                        status = 'EN TRANSITO'

                    if my_ord.regimen == '10' and my_ord.fecha_llegada_cliente:
                        status = 'EN BODEGAS PARA COSTEO'

                data.append({
                    'order': my_ord,
                    'invoice': order_invoice,
                    'sale': my_order_sale,
                    'monts': Expense.get_months_storage(my_ord.nro_pedido),
                    'status': status,
                    'text_color': text_color[status],
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

            if order_sale['total_sale'] == 0 and order_sale['init_sale']:
                if order.regimen == '70':
                    order.bg_isclosed = 1
                    order.save()
            else:
                if order.regimen == '70':
                    order.bg_isclosed = 0
                    order.save()
