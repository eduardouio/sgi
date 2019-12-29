from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import (CompleteOrderInfo, CompletePartialInfo,
                     ExpensesReportSale, OrderProductSale)
from lib_src.sgi_utlils import get_host
from logs.app_log import loggin
from orders.models import Order
from partials.models import Partial


#/costos/saldo-mayor/<nro_order>/
class LedgerReportView(LoginRequiredMixin, TemplateView):
    template_name = 'costings/saldo_mayor.html'
    loggin_url = '/'

    def get(self, request, nro_order, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        order_product_sale = OrderProductSale()
        context['data'] = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Saldo Mayor Pedido {}'.format(nro_order),
            'nro_order' : nro_order,
            'host' : get_host(request),
            'saldo_producto' : order_product_sale.get(nro_order),
            'saldo_gastos' : ExpensesReportSale().get(nro_order), 
            }

        return self.render_to_response(context) 
