from django.conf import settings
from django.views.generic import TemplateView
from orders.models import OrderInvoice, OrderInvoiceDetail

from logs import loggin

#/auditoria/factura-exterior/<id>/
class ProductInvoiceTemplateView(TemplateView):
    template_name = 'audit/mostrar-factura-productos.html'

    def get(self, request, id_invoice, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        invoice = OrderInvoice.get_by_id(id_invoice)
        if invoice is None:
            self.template_name = 'errors/404.html'
            context['data'] = {
                'empresa' : settings.EMPRESA,
                'title_page' : 'Factura no encontrada',
                'msg' : 'La factura {} no existe'.format(id_invoice),
            }
            return self.render_to_response(context)
        invoice_items = OrderInvoiceDetail.get_by_id_order_invoice(id_invoice)

        context['data'] = {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Factura del Exterior',
            'invoice' : invoice,
            'invoice_items': invoice_items,
            'status' : self.get_status(invoice, invoice_items),
        }

        return self.render_to_response(context)

    def get_status(self, invoice, invoice_items):
        status = {
            'is_complete' : False,
            'value' : invoice.valor,
            'justified':0,
            'tc_trimestral' : invoice.tipo_cambio,
        }

        return status
