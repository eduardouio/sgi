from django.conf import settings
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
    loggin_url = '/'

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

            mayor.append({**product_sale,**expenses_sale , **{'nro_order': nro_order, 'saldo_mayor':saldo_mayor}})

        context['data'] = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Saldo General de Mayor',
            'host' : get_host(request),
            'mayor' : mayor,
            }
        return self.render_to_response(context) 
    
    def get_open_order(self):
        return [         
            '045-19',
            '048-19',
            '004-20',
            '040-19',
            '042-19',
            '043-19',
            '042-19',
            '043-19',
            '047-19',
            '048-19',
            '049-19',
            '040-19',
            '036-19',
            '036-19',
            '005-20',
        ]
