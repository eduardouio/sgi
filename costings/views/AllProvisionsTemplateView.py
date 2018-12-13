from orders.models.Order import Order
from partials.models.Partial import Partial
from paids.models.Expense import Expense
from django.views.generic import TemplateView
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail

class AllProvisionsTemplateView(TemplateView):
    template_name = 'costings/table_report.html'

    def get(self, request, *args, **kwargs):
        context = super(AllProvisionsTemplateView, self).get_context_data(*args, **kwargs)       
        provisions = Expense.get_all_open_provisions()
        
        for p in provisions:
            p.invoiced = 00
            paids  = PaidInvoiceDetail.get_by_expense(p)
            for x in paids:
                p.invoiced += x.valor
        
            p.sale = (p.valor_provisionado - p.invoiced)


        context.update({'provisions': provisions })
        return self.render_to_response(context)
