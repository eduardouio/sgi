from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from lib_src import InvoicesUtils


# /auditoria/
class InvoiceListTemplateView(LoginRequiredMixin, TemplateView):
    '''Muestra la lista de facturas por aprobar'''
    template_name = 'audit/listado-facturas.html'

    # /auditoria/
    def get(self, request, *args, **kwargs):
        invoice_utils = InvoicesUtils()
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'empresa': settings.EMPRESA,
            'title_page': 'Facturas Pendientes',
            'local_invoices': invoice_utils.get_unapproved_invoices(),
        }
        return self.render_to_response(context)
