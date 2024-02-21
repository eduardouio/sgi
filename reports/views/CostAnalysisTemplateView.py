from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from reports.forms import FormProductSeach
from reports.lib_src import ProductCostAnalysis
from products.models import Product


# /costos/analisis/<pk-product>/
class CostAnalysisTemplateView(LoginRequiredMixin, TemplateView):
    """Encargado de analizar los costos historicos para un producto
    """
    template_name = 'reports/costs_analysis.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Ingresamos a analisis de costos')
        context = self.get_context_data(**kwargs)
        form = FormProductSeach()
        product = stats = None
        report = []
        averages = {}

        if request.GET:
            cod_contable = request.GET.get('products')
            my_product = Product.get_by_cod_contable(cod_contable)

            if my_product is None:
                loggin('e', 'No se encontro el producto')
                context['data'] = {
                    'show_error': True,
                    'title_page': 'Análsis de Costos - 404',
                    'form': form,
                    'json_report': [],
                }
                return self.render_to_response(context)

            deep = request.GET.get('deep')
            form.fields['products'].initial = cod_contable
            form.fields['deep'].initial = deep
            cost_analysis = ProductCostAnalysis(cod_contable, int(deep))
            cost_data = cost_analysis.get()
            product = cost_data['product']
            report = cost_data['history']
            stats = {
                'dias_transito': [x['dias_transito'] for x in report],
                'unidades': [x['unidades'] for x in report],
                'costo_unidad': [x['costo_unidad'] for x in report],
                'fob': [x['fob'] for x in report],
                'cif': [x['cif'] for x in report],
                'ex_aduana_unitario': [x['ex_aduana_unitario'] for x in report],
                'total_ice': [x['total_ice'] for x in report],
                'tributos': [x['tributos'] for x in report],
                'costo_sap': [x['costo_sap'] for x in report],
                'indirectos': [x['indirectos'] for x in report],
                'costo_botella': [x['costo_botella'] for x in report],
                'fodinfa': [x['fodinfa'] for x in report],
                'arancel_advalorem': [x['arancel_advalorem'] for x in report],
                'arancel_especifico': [x['arancel_especifico'] for x in report],
            }

            for s in stats:
                try:
                    averages[s] = sum(stats[s])/len(stats[s])
                except ZeroDivisionError:
                    averages[s] = 0.0

        json_report = []

        for item in report:
            line_item = dict(zip(
                item.keys(),  [str(item[key]) for key in item.keys()]
            ))
            json_report.append(line_item)

        context['data'] = {
            'title_page': 'Análsis de Costos',
            'form': form,
            'product': product,
            'report': report,
            'json_report': json_report,
            'stats': stats,
            'averages': averages,
        }

        return self.render_to_response(context)
