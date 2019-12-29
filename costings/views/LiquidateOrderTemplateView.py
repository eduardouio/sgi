from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from lib_src import CompleteOrderInfo, CostingsOrder
from lib_src.sgi_utlils import get_host
from logs.app_log import loggin
from orders.models.Order import Order


# /costos/pedio/{nro_pedido}
class LiquidateOrderTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/'
    template_name = 'costings/liquidar_pedido.html'
    
    def get(self, request, nro_order , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Iniciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = self.get_context_data(*args, **kwargs)        
        cmp_order_inf = CompleteOrderInfo().get_data(nro_order=nro_order)
        costs_order = CostingsOrder(
            complete_order_info = cmp_order_inf)
        costs = costs_order.get_costs()
        ice_reliquidado = {
            'expense' : 'ICE ADVALOREM RELIQUIDADO',
            'provision' : float(costs['ice_reliquidado']),
            'invoiced_value' : 0,
            'legder' : 0,
        }
        context['data']  = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Liquidación Pedido {} Consumo'.format(nro_order),
            'nro_order' : nro_order,
            'complete_order_info' : cmp_order_inf,
            'costings' : costs,
            'request' : request,
            'ice_reliquidado' : ice_reliquidado,
            'host' : get_host(request)
        }
        context['data'].update(self.__check_status_values(
            cmp_order_inf, costs))

        return self.render_to_response(context)

    def __check_status_values(self, order_info, product_costs):
        ''' realiza el calculo de facturas provisiones y producto '''
        status_values = {
            'facturas_sgi' : order_info['total_invoiced'],
            'provisiones_sgi': order_info['total_provisions'],
            'reliquidacion_ice' : product_costs['ice_reliquidado'],
            'total_expenses' : order_info['total_expenses'],
            'saldo_producto' : order_info['order_invoice']['totals']['value_tct'],
        }
        return status_values
