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
                '340-18',
'247-18',
'001-19',
'019-19',
'020-19',
'029-19',
'031-19',
'011-19',
'026-19',
'027-19',
'028-19',
'033-19',
'032-19',
'012-19',
'013-19',
'105-19',
'104-19',
'131-19',
'136-19',
'147-19',
'110-19',
'146-19',
'158-19',
'181-19',
'192-19',
'178-19',
'176-19',
'179-19',
'189-19',
'319-19',
'211-19',
'220-19',
'286-19',
'209-19',
'214-19',
'112-19',
'224-19',
'149-19',
'188-19',
'190-19',
'326-19',
'226-19',
'222-19',
'217-19',
'320-19',
'261-19',
'253-19',
'297-19',
'265-19',
'263-19',
'260-19',
'268-19',
'248-19',
'254-19',
'325-19',
'251-19',
'323-19',
'324-19',
'256-19',
'328-19',
'216-19',
'317-19',
'314-19',
'332-19',
'148-19',
'331-19',
'333-19',
'259-19',
'311-19',
'309-19',
'334-19',
'308-19',
'310-19',
'267-19',
'327-19',
'335-19',
'357-19',
'356-19',
'358-19',
'276-19',
'257-19',
'355-19',
'279-19',
'281-19',
'316-19',
'258-19',
'353-19',
'315-19',
'318-19',
'278-19',
'352-19',
'306-19',
'330-19',
'363-19',
'362-19',
'364-19',
'390-19',
'359-19',
                ]

