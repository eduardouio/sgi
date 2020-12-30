from django.views.generic import TemplateView
from lib_src import ExpensesWithSale


#/reportes/provisiones/
class ExpensesReportTemplateView(TemplateView):
    template_name = 'reports/report-expenses.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        expenses = ExpensesWithSale().get_all_expeneses_with_sale()
        context['data'] = {
            'title_page': 'Reporte de Provisiones Pendientes',
            'expenses': expenses
        }
        return self.render_to_response(context=context)