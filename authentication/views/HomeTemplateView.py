from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sgi.settings import EMPRESA

from logs.app_log import loggin


# /home/
class HomeTemplateView(LoginRequiredMixin, TemplateView):
    '''Direcciona al home del proyecto'''
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Cargando inicio pantalla de inicio')
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'SGI ' + EMPRESA['nombre'],
        }
        return self.render_to_response(context)
