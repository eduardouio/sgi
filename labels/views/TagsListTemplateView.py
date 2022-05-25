from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from lib_src.sgi_utlils import get_host
from orders.models import Order


# /importaciones/pedidos-etiquetas/
class TagsListTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'labels/lista-pedidos-etiquetas.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        orders = []
        show_error = False

        if request.GET:
            nro_order = request.GET.get('nro_order')
            show_error = request.GET.get('show_error')

            if nro_order:
                nro_order.replace('/', '-')
                orders = Order.objects.filter(
                    nro_pedido__startswith=nro_order
                )
                
        context['data'] = {
            'title_page': 'Etiquetas de Consumo',
            'host': get_host(request),
            'orders': orders,
            'show_error': show_error,
        }

        return self.render_to_response(context)
