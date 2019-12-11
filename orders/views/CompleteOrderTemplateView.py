from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.conf import settings


from lib_src import CompleteOrderInfo, CompletePaidInfo
from orders.models import Order
from logs.app_log import loggin


# /pedidos/ficha/{nro_pedido}/
class CompleteOrderTemplateView(LoginRequiredMixin, TemplateView):
    ''' 
        Vista encargada de mostrar toda la informacion del pedido
    '''
    login_url = '/admin/'
    template_name = 'orders/ver_pedido.html'

    def get(self,request, nro_order, *args, **kwargs):
        loggin('i', 'Mostrando ficha completa del pedido', request)
        context = self.get_context_data(**kwargs)
        order_info = CompleteOrderInfo().get_data(nro_order, False)
        data = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Ficha Pedido {} R {}'
                            .format(nro_order, order_info['order'].regimen),
            'order_info' : order_info,
            'nro_order' : nro_order,
            'bg_is_closed' : order_info['order'].bg_isclosed,
        }
        
        context['data'] = data
        return self.render_to_response(context)