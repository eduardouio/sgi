from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from django.db import connection
from datetime import date


class CurrentNationalizationTV(TemplateView, LoginRequiredMixin):
    template_name = 'reports/current_nationalizations.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        loggin('i', 'Cargando reporte de Productos en Nacionalización')
        is_filtered = False
        report = None
        params = {
            'liquidacion': 'Todos',
            'etiquetas': 'Por Etiquetas Fiscales',
            'pegado': 'Etiquetas Pegadas',
            'aforo': 'Por Aforo',
            'salida': 'Por Salida Autorizada',
            'llegada': 'Por Llegada a Bodega',
        }

        if request.GET:
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')
            option = request.GET.get('option')
            is_filtered = True
            report = self.get_report(start_date, end_date, option)
        else:
            report = self.get_report()

        context['data'] = {
            'title_page': 'Reporte En Nacionalización',
            'report': report,
            'today': date.today(),
            'is_filtered': is_filtered,
            'params': params
        }
        return self.render_to_response(context)

    def get_report(self, start_date=None, end_date=None, option=None):
        params = {
            'liquidacion': 'fecha_liquidacion',
            'etiquetas': 'fecha_entrega_etiquetas_senae',
            'pegado': 'fecha_pegado_etiquetas',
            'aforo': 'fecha_aforo',
            'salida': 'fecha_salida_autorizada',
            'llegada': 'fecha_llegada_cliente',
        }

        if start_date is None:
            sql = (
                'SELECT * FROM `v_current_nationalization` WHERE'
                ' `bg_isclosed` IS NOT true order by fecha_liquidacion DESC'
            )
        else:
            sql = (
                "SELECT * FROM `v_current_nationalization` "
                "where {} >= '{}' "
                "and fecha_liquidacion <= '{}' "
                " order by {} DESC"
            ).format(params[option], start_date, end_date, params[option])

        conn = connection.cursor()
        conn.execute(sql)
        cols = [col[0] for col in conn.description]
        return [
            dict(zip(cols, row))
            for row in conn.fetchall()
        ]
