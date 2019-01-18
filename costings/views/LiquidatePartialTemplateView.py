from django.views.generic import TemplateView

from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from logs.app_log import loggin


class LiquidatePartialTemplateView(TemplateView):
    template_name = "costings/revisar_gastos_parciales.html"

    def get(self, request, nro_order , ordinal_parcial , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Parciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = super(LiquidatePartialTemplateView, self).get_context_data(*args, **kwargs)
        complete_order_info = CompleteOrderInfo().get_data(nro_order)
        complete_partial_info = CompletePartialInfo()
        if complete_order_info is None or complete_order_info['partials'] is None:
            loggin(
                'i',
                'No se puede liquidar el parcial {ordinal_parcial} del pedido {nro_order}, parcial o pedido inexistente'
                .format(
                    ordinal_parcial=ordinal_parcial, 
                    nro_order=nro_order
                    )
                )
        all_partials = []
        for partial in complete_order_info['partials']:
            all_partials.append(complete_partial_info.get_data(partial['partial'].id_parcial))
        
        apportiments_expenses = ApportionmentExpenses(
            complete_order_info=complete_order_info,
            all_partials=all_partials,
            current_ordinal_partial=ordinal_parcial,
            )

        costings = apportiments_expenses.get_data()
        
        data = {
            'complete_order_info' : complete_order_info,
            'all_partials' : all_partials,
            'apportioments' : costings
        }
        
        return self.render_to_response(context)
