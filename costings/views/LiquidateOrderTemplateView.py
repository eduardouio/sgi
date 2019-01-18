from django.views.generic import TemplateView

from lib_src.CalculateOrderCosts import CalculateOrderCosts
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from logs.app_log import loggin


class LiquidateOrderTemplateView(TemplateView):
    template_name = 'costings/liquidar_pedido.html'

    def get(self, request, nro_order , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Iniciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        status_order = True
        context = super(LiquidateOrderTemplateView, self).get_context_data(*args, **kwargs)
        complete_order = CompleteOrderInfo().get_data(nro_order=nro_order, serialized=False, request=request)
        complete_order['title_page'] = 'Revision de Gastos Iniciales {}'.format(nro_order)
        complete_order['costs'] = None

        if complete_order['status']['ledger'] == False:
            loggin('e','El pedido {} no tiene una mayor registrado'.format(nro_order))
            complete_order['status']['ledger']= True

        for status_det in complete_order['status']:
            if complete_order['status'][status_det] == False:
                status_order = False
                loggin('e', 'El pedido {} no existe o esta incompleto, cambniando de plantilla'.format(nro_order))
                self.template_name = 'errors/error_en_pedido.html'

        if complete_order['order'].regimen == '70':
            self.template_name = 'costings/seleccionar_parcial.html'

        if status_order:
            costs_order = CalculateOrderCosts(complete_order).get_costings()
            complete_order['costs'] = costs_order

        context.update({'data': complete_order})

        return self.render_to_response(context)