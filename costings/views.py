from django.shortcuts import render
from django.views.generic import TemplateView

class validOrderTemplateView(TemplateView):
    template_name = 'costings/revisar_gastos.html'

    def get(self, request, *args, **kwargs):
        context = super(validOrderTemplateView, self).get_context_data(*args, **kwargs)
        return self.render_to_response(context)