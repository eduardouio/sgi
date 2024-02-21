from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sgi.settings import EMPRESA
from datetime import date

from logs.app_log import loggin


# /home/
class HomeTemplateView(LoginRequiredMixin, TemplateView):
    '''Direcciona al home del proyecto'''
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Cargando inicio pantalla de inicio')
        context = self.get_context_data(**kwargs)
        today = date.today().isoformat()
        url_almagro_report = EMPRESA['url_almagro_report'].format(
            today[5:7],
            today[-2:],
            today[:4]
        )
        context['data'] = {
            'title_page': 'SGI ' + EMPRESA['nombre'],
            'url_almagro_report': url_almagro_report,
        }
        return self.render_to_response(context)
