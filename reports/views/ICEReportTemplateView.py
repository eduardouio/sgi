import calendar

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from lib_src import ReportICE


# /reportes/ice/<year>/<month>/
class ICEReportTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/reporte_ice.html'

    def get(self, response, year, month, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'empresa': settings.EMPRESA,
            'title_page': 'Rreporte ICE {} {}'.format(
                year,calendar.month_name[month]
                ),
            'report' : ReportICE(year, month).get()
        }     
        return self.render_to_response(context)

