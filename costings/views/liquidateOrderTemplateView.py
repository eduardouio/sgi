from django.shortcuts import render
from django.views.generic import TemplateView
from logs.app_log import loggin
from lib_src.CompleteOrderInfo import CompleteOrderInfo


class liquidateOrderTemplateView(TemplateView):
    template_name = 'costings/revisar_gastos.html'

    def get(self, request, nro_order , *args, **kwargs):
        context = super(liquidateOrderTemplateView, self).get_context_data(*args, **kwargs)        
        complete_order = CompleteOrderInfo().get_data(nro_order)
        print(complete_order)
        context.update({'order': complete_order})
        return self.render_to_response(context)
    