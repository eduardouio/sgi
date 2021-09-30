from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from django.db import connection
from datetime import date
from sgi.settings import EMPRESA


class CurrentNationalizationTV(TemplateView, LoginRequiredMixin):
    template_name = 'reports/current_nationalizations.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        loggin('i', 'Cargando reporte de Productos en Nacionalización')
        deep = False

        if request.GET:
            if request.GET.get('deep') == 'on':
                deep = True

        context['data'] = {
            'title_page': 'Reporte En Nacionalización',
            'enterprise': EMPRESA,
            'report': self.get_report(deep),
            'today': date.today()
        }
        return self.render_to_response(context)

    def get_report(self, show_closed):
        sql = (
            'SELECT * FROM `v_current_nationalization` WHERE'
            ' `bg_isclosed` IS NOT true'
        )
        if show_closed:
            sql = 'SELECT * FROM v_current_nationalization'

        conn = connection.cursor()
        conn.execute(sql)
        cols = [col[0] for col in conn.description]
        return [
            dict(zip(cols, row))
            for row in conn.fetchall()
        ]
