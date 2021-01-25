from django.views.generic import TemplateView
from migrationSAP.lib_src import SAPImporter
from datetime import date


# /sap/importar-pedidos/
class SapImportWizardTV(TemplateView):
    template_name = 'sap/importar-pedidos-sap.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        sap_importer = SAPImporter()
        imported = sap_importer.check_orders((date.today()).year)

        context['data'] = {
            'title_page': 'Importar Pedido SAP',
            'imported': imported,
        }
        return self.render_to_response(context)
