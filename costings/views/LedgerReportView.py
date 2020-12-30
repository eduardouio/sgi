from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import (CompleteOrderInfo, CompletePartialInfo,
                     ExpensesReportSale, OrderProductSale)
from lib_src.sgi_utlils import get_host
from logs.app_log import loggin
from orders.models import Order
from partials.models import Partial


#/costos/saldo-mayor-general/
class LedgerReportView(LoginRequiredMixin, TemplateView):
    template_name = 'costings/saldo_mayor_general.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        mayor = []
    
        for nro_order in self.get_open_order():
            product_sale = OrderProductSale(nro_order).get_sale()
            expenses_sale = ExpensesReportSale(nro_order).get_sale()
            saldo_mayor = (
                float(product_sale['sums']['fob_tct_saldo']).__round__(2) +
                float(expenses_sale['por_prorratear_gi']).__round__(2) +
                float(expenses_sale['gasto_origen_prox_parcial']).__round__(2) + 
                float(expenses_sale['almacenjae_pendiente']).__round__(2) +
                float(expenses_sale['saldo_inicial_lp']).__round__(2)
                )

            mayor.append(
                {**product_sale,**expenses_sale , 
                **{'nro_order': nro_order, 'saldo_mayor':saldo_mayor}}
                )

        context['data'] = {
            'title_page': 'Saldo General de Mayor',
            'host': get_host(request),
            'mayor': mayor,
            }
        return self.render_to_response(context) 

    def get_open_order(self):
        return [
            '009-20',
            '044-20',
            '020-20',
            '023-20',
            '029-20',
            '030-20',
            '041-20',
            '046-20',
            '049-20',
            '050-20',
            '051-20',
            '036-20',
            '044-20',
            '042-20',
            '041-20',
            '032-20',
            '035-20',
            '047-20',
            '031-20',
            '034-20',
            '043-20',
            '048-20',
            '043-20',
            '052-20',
            '043-20',
            '043-20',
            '045-20',
        ]