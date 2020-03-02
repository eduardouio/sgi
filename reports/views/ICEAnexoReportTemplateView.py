from django.views.generic import TemplateView
from logs import loggin
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from lib_src import AnexoICE


# /reportes/anexo-ice/<int:year>/<int:month>/
class ICEAnexoReportTemplateView(LoginRequiredMixin, TemplateView):
    '''Anexo ICE segundo formato contable'''
    login_url = '/'
    template_name = 'reports/anexo_ice.html'

    def get(self, request, year, month, *args, **kwargs):
        loggin('i', 'Iniciando reporte Anexo ICE ')
        context = self.get_context_data(**kwargs)
        anexo = AnexoICE(year, month).get()

        context['data'] = {
            'empresa': settings.EMPRESA,
            'title_page': 'Anexo ICE {} {}'.format(year, month),
            'anexo': anexo,
            'year' : year,
            'month' : self.get_meta(month),
        }
        return self.render_to_response(context)

    def get_meta(self,month):
        meses = [
            'ENERO',
            'FEBRERO',
            'MARZO',
            'ABRIL',
            'MAYO',
            'JUNIO',
            'AGOSTO',
            'SEPTIEMBRE',
            'NOVIMEBRE',
            'DICIEMBRE',
        ]
        return meses[month-1]
