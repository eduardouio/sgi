from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from lib_src.sgi_utlils import get_host

#/costos/error/<pedido>/<ordinal_parcial>/
class ErrorTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "errors/parcial_anterior_abierto.html"

    def get(self, request, nro_order, ordinal_parcial, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page' : 'Error Parcial Abierto',
            'nro_order' : nro_order,
            'ordinal_partial' : ordinal_parcial,
            'empresa' : settings.EMPRESA,
            'host' : get_host(request),
        }
        return self.render_to_response(context)

