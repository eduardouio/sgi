from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from lib_src import LocalWarenhouseArrivals
from logs.app_log import loggin


# /reportes/llegadas/bodega/local/<year>/<month>/
class WarenhouseArrivalsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/reporte-llegadas.html'

    def get(self, request, *args, **kwargs):        
        context = self.get_context_data(**kwargs)
        loggin('i', 'Llamando a reporte de llegadas')
        if request.GET:
            year = int(request.GET['year'])
            mont = int(request.GET['mont'])
            report = LocalWarenhouseArrivals(year, mont).get()
        else:
            report = []

        context['data'] = {
            'title_page': 'Llegadas Bodega Local',
            'report': report,
            'empty': bool(report.__len__())
        }

        return self.render_to_response(context)