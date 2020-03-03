from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from logs import loggin


# /reportes/
class HomeTemplateView(LoginRequiredMixin, TemplateView):
    login_url = ''
    template_name = 'reports/home-reports.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Llamando a pagina de reportes')
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'empresa': settings.EMPRESA,
            'title_page': 'Reportes'
        }
        return self.render_to_response(context)
