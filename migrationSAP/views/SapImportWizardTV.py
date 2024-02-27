from django.views.generic import TemplateView
from migrationSAP.lib_src import SAPImporter
from datetime import date
from django.conf import settings
from migrationSAP.lib_src.Model import Model

import json


# /sap/importar-pedidos/
class SapImportWizardTV(TemplateView):
    template_name = 'sap/importar-pedidos-sap.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # sap_importer = SAPImporter()
        # imported = sap_importer.check_orders((date.today()).year)
        imported = []
        data = None
        if request.GET.get('scan'):
            data = Model(settings.EMPRESA['empresa'], (date.today()).year).get_data()
            data = json.dumps(data, ensure_ascii=False)
        today = date.today()

        context['data'] = {
            'title_page': 'Importar Pedido SAP',
            'imported': imported,
            'year': today.year,
            'current_status': 'load',
            'data': data if data else '',
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        today = date.today()
        context = self.get_context_data(**kwargs)
        data = request.POST.get('pedidos')
        sap_importer = SAPImporter().check_orders(data)

        context['data'] = {
            'title_page': 'Importar Pedido SAP',
            'imported': sap_importer,
            'year': today.year,
            'current_status': 'results',
        }

        return self.render_to_response(context)
