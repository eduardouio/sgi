from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import (ApportionmentExpenses, CompleteOrderInfo,
                     CompletePartialInfo, CostingsPartial)
from logs.app_log import loggin
from orders.models.Order import Order
from partials.models.Partial import Partial


class LiquidatePartialTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'costings/liquidar_parcial.html'
    login_url = '/admin/'

    def get(self, request, nro_order , ordinal_parcial , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Parciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = self.get_context_data(**kwargs)
        self.ordinal_partial = ordinal_parcial

        if not self.check_order_and_partial_exist(nro_order, ordinal_parcial):
            self.template_name = 'errors/404.html'
            context['data'] = {
                'title_page' : 'Parcial No Econtrado',
                'msg' : 'El parcial que busca no existe',
            }
            return self.render_to_response(context)

        complete_order_info = CompleteOrderInfo().get_data(nro_order)
        all_partials = []

        for partial in complete_order_info['partials']:
            all_partials.append(
                CompletePartialInfo().get_data(
                            partial.id_parcial,
                            False,
                            complete_order_info['order_invoice']['order_invoice']
                            .tipo_cambio
                            )
                )
        
        apportiments_expenses = ApportionmentExpenses(
            complete_order_info=complete_order_info,
            all_partials=all_partials,
            ordinal_current_partial=ordinal_parcial,
            ).get_apportionments()
        
        producto_costs = CostingsPartial(
                complete_order_info = complete_order_info, 
                all_partials = all_partials,
                apportionment_expenses = apportiments_expenses,
                ordinal_current_partial = all_partials[(int(ordinal_parcial)-1)]
                ).get_costs()
        
        context['data'] = {
            'title_page' : 'Liquidacion Parcial %s'%ordinal_parcial,
            'nro_order' : nro_order,
            'ordinal_partial' : int(ordinal_parcial),
            'total_parcials' : all_partials.__len__(),
            'current_partial' : all_partials[(int(ordinal_parcial) - 1)],
            'current_partial_pos' : int(ordinal_parcial) - 1,
            'complete_order_info' : complete_order_info,
            'all_partials' : all_partials,
            'apportioments' : apportiments_expenses,
            'costings' : producto_costs,
            'request' : request
        }

        context['data'].update(self.checkStatusValues(
                    complete_order_info, 
                    all_partials,
                    producto_costs
        ))
        
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
    

    def checkStatusValues(self, order_info, all_partials, product_costs):
        ''' realiza el calculo de facturas provisiones y producto '''
        status_values = {
            'facturas_sgi' : order_info['total_invoiced'],
            'provisiones_sgi': order_info['total_provisions'],
            'reliquidacion_ice' : product_costs['ice_reliquidado'],
            'total_expenses' : order_info['total_expenses'],
            'saldo_producto' : order_info['order_invoice']['totals']['value'],
        }
        #solo se toman los datos hasta el actual parcial
        for k,p in enumerate(all_partials):
            if (k < int(self.ordinal_partial)):
                status_values['facturas_sgi'] += p['total_invoiced']
                status_values['provisiones_sgi'] += p['total_provisions']
                status_values['total_expenses'] += p['total_expenses']
                status_values['saldo_producto'] -= p['info_invoice']['totals']['value']            

        return status_values