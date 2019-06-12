from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from logs.app_log import loggin
from orders.models.Order import Order
from lib_src import CompleteOrderInfo, CostingsOrder

# /costos/pedio/{nro_pedido}
class LiquidateOrderTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/'
    template_name = 'costings/test.html'
    
    def get(self, request, nro_order , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Iniciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = self.get_context_data(*args, **kwargs)        
        cmp_order_inf = CompleteOrderInfo().get_data(nro_order=nro_order, serialized=False, request=request)
        costs_order = CostingsOrder(
            complete_order_info = cmp_order_inf
        )
            
        context['data']  = {
            'title_page' : 'Liquidación Pedido a Consumo',
        }

        return self.render_to_response(context)