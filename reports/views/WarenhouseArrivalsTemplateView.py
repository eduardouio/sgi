from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


# /reportes/llegadas/bodega/local/<year>/<month>/
class WarenhouseArrivalsTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name  = 'reports/reporte-llegadas.html'

    def get(self, requets, year, month, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'empresa': settings.EMPRESA,
            'title_page': 'Llegadas Bodega Local'
        }
        return self.render_to_response(context)
