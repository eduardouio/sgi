from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from lib_src import CompletePaidInvoice

from lib_src.sgi_utlils import get_host

#/audotoria/factura/<id_invoice>/
class InvoiceTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'audit/mostrar-factura.html'

    def get(self, request, id_invoice, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Factura {}'.format(id_invoice),
            'host' : get_host(request),
            'request' : request,
            'invoice' : CompletePaidInvoice.get(id_invoice)
        }  
        return self.render_to_response(context)