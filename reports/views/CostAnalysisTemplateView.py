from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from reports.forms import FormProductSeach
from reports.lib_src import ProductCostAnalysis


# /costos/analisis/<pk-product>/
class CostAnalysisTemplateView(LoginRequiredMixin, TemplateView):
    """Encargado de analizar los costos historicos para un producto
    """
    template_name = 'reports/costs_analysis.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Ingresamos a analisis de costos')
        context = self.get_context_data(**kwargs)
        form = FormProductSeach()
        product = report = None

        if request.GET:
            cod_contable = request.GET.get('products')
            form.fields['products'].initial = cod_contable
            cost_analysis = ProductCostAnalysis(cod_contable)
            cost_data = cost_analysis.get()
            product = cost_data['product']
            report = cost_data['history']
       
        context['data'] = {
            'title_page': 'Análsis de Costos',
            'form': form,
            'product': product,
            'report': report,
        }
       
        return self.render_to_response(context)
