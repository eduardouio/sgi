from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from lib_src.ProductsCosts import CostingsProduct
from logs.app_log import loggin
from orders.models.Order import Order
from partials.models.Partial import Partial


class LiquidatePartialTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "costings/liquidar_parcial.html"
    login_url = '/admin/'

    def get(self, request, nro_order , ordinal_parcial , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Parciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = super(LiquidatePartialTemplateView, self).get_context_data(*args, **kwargs)

        if self.check_order_and_partial_exist(nro_order, ordinal_parcial) == False:
            self.template_name = 'errors/404.html'

            context['data'] = {
                'title_page' : 'Parcial No Econtrado',
                'msg' : 'El parcial que busca no existe',
            }

            return self.render_to_response(context)

        complete_order_info = CompleteOrderInfo().get_data(nro_order)
        all_partials = []

        for partial in complete_order_info['partials']:
            all_partials.append(CompletePartialInfo().get_data(
                                                partial.id_parcial,
                                                False,
                                                complete_order_info['order_invoice']['order_invoice'].tipo_cambio
                                                ))
        #se envia a realizar el prorrateo(costeo de producto)
        apportiments_expenses = ApportionmentExpenses(
            complete_order_info=complete_order_info,
            all_partials=all_partials,
            ordinal_current_partial=ordinal_parcial,
            ).get_apportionments()
        
        producto_costs = CostingsPartial(
                complete_order_info = complete_order_info, 
                all_partials = all_partials,
                apportionment_expenses = apportiments_expenses,
                ordinal_current_partial = all_partials[(int(ordinal_parcial) - 1)]
                ).get_costs()


        context['data'] = {
            'title_page' : 'Liquidacion Parcial %s'%ordinal_parcial,
            'nro_order' : nro_order,
            'ordinal_partial' : int(ordinal_parcial),
            'total_parcials' : all_partials.__len__(),
            'current_partial' : all_partials[int(ordinal_parcial) - 1 ],
            'complete_order_info' : complete_order_info,
            'all_partials' : all_partials,
            'apportioments' : apportiments_expenses,
            'costings' : producto_costs,
        }
        
        return self.render_to_response(context)
    

    def check_order_and_partial_exist(self, nro_order, ordinal_parcial):
        order = Order.get_by_order(nro_order)
        if order is None:
            loggin('e', 'El pedido {} no existe, error en plantilla'.format(nro_order))
            return False
        
        all_partials = Partial.get_by_order(nro_order)

        if all_partials.count() == 0:
            loggin('e', 'El parcial {}, del pedido {} no existe'.format(ordinal_parcial, nro_order))
            return False
        
        for x, p in enumerate(all_partials):
            if x+1 == int(ordinal_parcial):
                return True

        loggin(
            'e', 
            'El numero ordinal del parcial {} , no existe en el pedido {}'
            .format(ordinal_parcial, nro_order)
            )

        return False
