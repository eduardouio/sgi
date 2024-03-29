from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import CompletePaidInvoice
from logs.app_log import loggin


# /auditoria/factura/<id_invoice>/
class InvoiceTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'audit/mostrar-factura.html'

    def get(self, request, id_invoice, *args, **kwargs):
        loggin('i', 'Moctrando factura para auditoria')
        context = self.get_context_data(**kwargs)
        complete_paid_invoice = CompletePaidInvoice()
        invoice = complete_paid_invoice.get(id_invoice)
        if invoice is None:
            self.template_name = 'errors/404.html'
            context['data'] = {
                'title_page': 'Factura no encontrada',
                'msg': 'La factura {} no existe'.format(id_invoice),
            }
            return self.render_to_response(context)

        context['data'] = {
            'title_page': 'Factura {} [{}]'.format(
                invoice['invoice'].nro_factura, id_invoice
            ),
            'invoice': invoice,
        }

        return self.render_to_response(context)
