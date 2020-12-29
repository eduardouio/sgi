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
            '012-20',
            '024-20',
            '034-20',
            '040-20',
            '046-20',
            '050-20',
            '057-20',
            '058-20',
            '059-20',
            '060-20',
            '062-20',
            '065-20',
            '066-20',
            '067-20',
            '069-20',
            '070-20',
            '072-20',
            '075-20',
            '076-20',
'077-20', 
'078-20', 
'080-20', 
'081-20', 
'083-20', 
'091-20', 
'092-20', 
'093-20',
'094-20',
'095-20',
'096-20',
'097-20',
'098-20',
'099-20',
'100-20',
'101-20',
'102-20',
'103-20',
'105-19',
'105-20',
'106-20',
'107-20',
'108-20',
'109-20',
'118-20',
#'119-20',
'128-20',
'129-20',
'147-19',
'148-19',
'149-19',
'156-20',
'161-20',
'162-20',
'163-20',
'164-20',
'165-20',
'166-20',
'172-20',
'173-20',
'174-20',
'176-19',
'176-20',
'178-19',
'179-19',
'182-20',
'183-20',
'184-20',
'185-20',
'186-20',
'187-20',
'188-19',
'188-20',
'189-19',
'190-19',
'190-20',
'191-20',
'192-19',
'192-20',
'193-20',
'194-20',
'195-20',
'196-20',
'197-20',
'198-20',
'199-20',
'200-20',
'201-20',
'202-20',
'203-20',
'204-20',
'205-20',
'206-20',
'207-20',
'208-20',
'209-20',
'210-20',
'211-19',
'211-20',
'212-20',
'213-20',
'214-20',
'215-20',
'216-19',
'216-20',
'217-19',
'217-20',
'218-20',
'254-19',
'257-19',
'258-19',
'259-19',
'267-19',
'279-19',
'281-19',
'286-19',
'297-19',
'306-19',
'309-19',
'311-19',
'312-19',
'313-19',
'314-19',
'315-19',
'316-19',
'317-19',
'318-19',
'320-19',
'323-19',
'324-19',
'325-19',
'328-19',
'331-19',
'332-19',
'334-19',
'352-19',
'354-19',
'355-19',
'362-19',
'363-19',
'364-19',
'372-19',
'390-19',

        ]