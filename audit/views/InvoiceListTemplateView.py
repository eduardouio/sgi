from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from paids.models import PaidInvoice, PaidInvoiceDetail
from suppliers.models import Supplier
from orders.models import OrderInvoice, OrderInvoiceDetail, Order


#/auditoria/
class InvoiceListTemplateView(LoginRequiredMixin, TemplateView):
    '''Muestra la lista de facturas por aprobar'''
    template_name = 'audit/listado-facturas.html'


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Facturas Pendientes',
        }
        return self.render_to_response(context)
    

    def get_local_invoices(self):
        pass


    def get_international_invoices(self):
        pass