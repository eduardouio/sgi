from django.views.generic import TemplateView
from logs import loggin
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


# /reportes/anexo-ice/<int:year>/<int:month>/
class ICEAnexoReportTemplateView(LoginRequiredMixin, TemplateView):
    '''Anexo ICE segundo formato contable'''
    login_url = '/'
    template_name = 'reports/anexo_ice.html'

    def get(self, request, year, month, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data']= {
            'empresa' : settings.EMPRESA,
            'title_page' : 'Anexo ICE {} {}'.format(year, month)
        }
        return self.render_to_response(context)
