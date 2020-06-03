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
            '001-19',
'001-20',
'002-20',
'003-20',
'004-20',
'005-20',
'006-20',
'007-20',
'008-20',
'009-20',
'010-20',
'011-19',
'011-20',
'012-19',
'012-20',
'013-19',
'013-20',
'014-20',
'015-20',
'016-20',
'017-20',
'018-20',
'019-19',
'019-20',
'020-19',
'020-20',
'021-20',
'022-20',
'023-20',
'024-20',
'025-20',
'026-19',
'026-20',
'027-19',
'027-20',
'028-19',
'028-20',
'029-19',
'029-20',
'030-20',
'031-19',
'031-20',
'032-19',
'032-20',
'033-19',
'033-20',
'034-20',
'035-20',
'036-20',
'037-20',
'038-20',
'039-20',
'040-20',
'041-20',
'042-20',
'043-20',
'044-20',
'045-20',
'046-20',
'047-20',
'048-20',
'049-20',
'050-20',
'051-20',
'052-20',
'053-20',
'054-20',
'055-20',
'056-20',
'057-20',
'058-20',
'059-20',
'060-20',
'061-20',
'062-20',
'063-20',
'064-20',
'065-20',
'066-20',
'067-20',
'068-20',
'069-20',
'070-20',
'071-20',
'072-20',
'073-20',
'074-20',
'075-20',
'076-20',
'077-20',
'078-20',
'079-20',
'080-20',
'081-20',
'082-20',
'083-20',
'084-20',
'085-20',
'086-20',
'088-20',
'089-20',
'104-19',
'105-19',
'110-19',
'131-19',
'136-19',
'146-19',
'147-19',
'148-19',
'149-19',
'158-19',
'176-19',
'178-19',
'179-19',
'181-19',
'188-19',
'189-19',
'190-19',
'192-19',
'209-19',
'211-19',
'214-19',
'216-19',
'217-19',
'220-19',
'222-19',
'224-19',
'226-19',
'247-18',
'248-19',
'251-19',
'253-19',
'254-19',
'256-19',
'257-19',
'258-19',
'259-19',
'260-19',
'261-19',
'263-19',
'265-19',
'267-19',
'268-19',
'276-19',
'278-19',
'279-19',
'281-19',
'286-19',
'297-19',
'306-19',
'308-19',
'309-19',
'310-19',
'311-19',
'312-19',
'313-19',
'314-19',
'315-19',
'316-19',
'317-19',
'318-19',
'319-19',
'320-19',
'323-19',
'324-19',
'325-19',
'326-19',
'327-19',
'328-19',
'329-19',
'331-19',
'332-19',
'333-19',
'334-19',
'335-19',
'352-19',
'353-19',
'354-19',
'355-19',
'356-19',
'357-19',
'358-19',
'362-19',
'363-19',
'364-19',
'370-19',
'371-19',
'372-19',
'374-19',
'376-19',
'377-19',
'378-19',
'386-19',
'387-19',
'388-19',
'390-19',
        ]



