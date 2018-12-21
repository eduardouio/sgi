from django.shortcuts import render
from django.views.generic import TemplateView
from logs.app_log import loggin
from lib_src.CompleteOrderInfo import CompleteOrderInfo


class liquidateOrderTemplateView(TemplateView):
    template_name = 'costings/revisar_gastos_iniciales.html'

    def get(self, request, nro_order , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Iniciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = super(liquidateOrderTemplateView, self).get_context_data(*args, **kwargs)        
        complete_order = CompleteOrderInfo().get_data(nro_order=nro_order, serialized=False, request=request)
        context.update({'order': complete_order})
        return self.render_to_response(context)
    