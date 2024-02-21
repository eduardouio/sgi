import calendar
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from lib_src import ReportICE


# /reportes/ice/?year=[1-9]*4?month=[1-9]*4
class ICEReportTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/reporte_ice.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        show_error = False
        report = None
        current_year = date.today().year
        current_month = date.today().month

        if request.GET.get('year'):
            current_year = int(request.GET['year'])
            current_month = int(request.GET['month'])

        reporte_ice = ReportICE(current_year, current_month)
        report = reporte_ice.get()

        if reporte_ice.opened_orders:
            show_error = True

        context['data'] = {
            'title_page': 'Rreporte ICE {} {}'.format(
                current_year,
                calendar.month_name[current_month]),
            'report': report,
            'current_year': current_year,
            'current_month': current_month,
            'show_error': show_error,
            'orders_opened': reporte_ice.opened_orders,
        }
        return self.render_to_response(context)
