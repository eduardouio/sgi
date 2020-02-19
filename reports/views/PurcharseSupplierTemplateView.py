from django.views.generic import TemplateView
from django.conf import settings
from logs import loggin
from lib_src import PurcharsesProductSupplier

# /reportes/compras/id_proveedor/
class PurcharseSupplierTemplateView(TemplateView):
    template_name = 'reports/reporte-compras.html'

    def get(self, request, id_supplier, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        purcharses = PurcharsesProductSupplier()        
    
        context['data'] = {
             'empresa': settings.EMPRESA,
            'title_page': 'Reporte de Compras',
            'report' : purcharses.get_purcharses('P9999999999993')
        }

        return self.render_to_response(context)