from django.views.generic import TemplateView
from reports.lib_src import ProductCostAnalysis
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product
from logs.app_log import loggin


class LastCostTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/last_cost.html'

    def get_context_data(self, **kwargs):
        loggin('i', 'Obteniendo ultimo listado de costos')
        context = super(LastCostTemplateView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        report = [
            ProductCostAnalysis(p.pk, 1).get()
            for p in products
        ]
        report = [_ for _ in report if _['history']]
        context['data'] = {
            'title_page': 'Ultimo Costo Inventario',
            'report': report,
        }
        return context
