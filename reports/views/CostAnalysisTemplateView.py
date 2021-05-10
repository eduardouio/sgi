from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# /costos/analisis/<pk-product>
class CostAnalysisTemplateView(LoginRequiredMixin, TemplateView):
    """Encargado de analizar los costos historicos para un producto
    """
    template_name = 'reports/costs_analysis.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Análsis de Costos'
        }
        return self.render_to_response(context)
