from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from lib_src.sgi_utlils import get_host
from costings.lib_src import LedgerOrder
from logs.app_log import loggin
from orders.models import Order


# /costos/saldo-mayor-general/
class LedgerReportView(LoginRequiredMixin, TemplateView):
    template_name = 'costings/saldo_mayor_general.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        show_form = True

        context['data'] = {
            'title_page': 'Saldo Mayor, Ingrese Pedidos',
            'host': get_host(request),
            'mayor': [],
            'show_form': show_form
            }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        loggin('i', 'Retornando saldo general de mayores')
        context = self.get_context_data(**kwargs)

        orders = request.POST['pedidos'].split('\n')
        orders = [o[:6].replace('/', '-') for o in orders]
        report = []
        for order in orders:
            order_sale = LedgerOrder().get_sale(order)
            if order_sale is not None:
                report.append(order_sale)

        context['data'] = {
            'title_page': 'Reporte Saldo Mayor por Pedidos',
            'host': get_host(request),
            'report': report,
            'show_form': False
        }

        return self.render_to_response(context)
