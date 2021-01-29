import calendar
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from lib_src import ReportICE
from orders.models import Order
from partials.models import Partial


# /reportes/ice/<year>/<month>/
class ICEReportTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/reporte_ice.html'

    def get(self, response,  *args, **kwargs):
        context = self.get_context_data(**kwargs)
        report = None

        if response.GET.get('year'):
            current_year = int(response.GET['year'])
            current_month = int(response.GET['month'])
        else:
            current_year = date.today().year
            current_month = date.today().month

        reporte_ice = ReportICE(current_year, current_month)
        quiery_orders_10 = reporte_ice.get_consumo(query=True)
        query_partials = reporte_ice.get_partials(query=True)
        orders_10 = [o for o in Order.objects.raw(quiery_orders_10)]
        partials = [p for p in Partial.objects.raw(query_partials)]
        show_error = False
        orders_open = [o for o in orders_10 if o.bg_isclosed != 1]
        partials_open = [p for p in partials if p.bg_isclosed != 1]

        if orders_open or partials_open:
            show_error = True
        else:
            report = reporte_ice.get()
            
        context['data'] = {
            'title_page': 'Rreporte ICE {} {}'.format(
                current_year, 
                calendar.month_name[current_month]),
            'report': report,
            'current_year': current_year,
            'current_month': current_month,
            'show_error': show_error,
            'partials_open': partials_open,
            'orders_open': orders_open
        }
        return self.render_to_response(context)
