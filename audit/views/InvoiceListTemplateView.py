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

        if request.GET:
            local_invoices = invoice_utils.search_local(request.GET['q'])
            foreign_invoices = invoice_utils.search_foreign(request.GET['q'])
        else:
            local_invoices = invoice_utils.get_unapproved_local_invoices()
            foreign_invoices = invoice_utils.get_unapproved_foreign_invoices()
            
        context['data'] = {
            'title_page': 'Facturas Pendientes',
            'local_invoices': local_invoices,
            'foreign_invoices' : foreign_invoices,
        }
        return self.render_to_response(context)
        


class inicio():
    """[summary]

    Args:
        Object ([type]): [description]
    """

    def __init__(self):
        pass