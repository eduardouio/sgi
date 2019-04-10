from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from lib_src import CompleteOrderInfo, CompletePaidInfo
from orders.models import Order


# /pedidos/ficha/{nro_pedido}/
class CompleteOrderTemplateView(LoginRequiredMixin, TemplateView):
    ''' 
        Vista encargada de mostrar toda la informacion del pedido
    '''
    login_url = '/admin/'
    template_name = 'orders/ver_pedido.html'

    def get(self,request, nro_order, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        order_info = CompleteOrderInfo().get_data(nro_order, False)
        
        data = {
            'title_page' : 'Ficha Pedido {} R {}'
                            .format(nro_order, order_info['order'].regimen),
            'order_info' : order_info,
            'nro_order' : nro_order,
            'bg_is_closed' : order_info['order'].bg_isclosed,
        }
        
        context['data'] = data
        return self.render_to_response(context)
    

    #redirecciona al admin
    def post(self,request,*args, **kwargs):  
        return HttpResponseRedirect(
            '/admin/orders/order/?q={}'.format(
                request.POST['query']
            ))