from django.views.generic import View
from django.http import JsonResponse
from django.db import connection
from logs.app_log import loggin
from datetime import datetime, date


class CurrentNationalizationAPI(View):

    def get(self, request, *args, **kwargs):
        loggin('i', 'Accediendo a API de nacionalizaciones actuales')

        # Parámetros hardcodeados
        start_date = '2023-01-01'
        end_date = date.today().strftime('%Y-%m-%d')
        option = 'llegada'

        # Obtener los datos de nacionalizaciones
        report_data = self.get_report(start_date, end_date, option)

        # Transformar los datos al formato requerido
        data = self.transform_data(report_data)

        return JsonResponse(data, safe=False)

    def get_report(self, start_date=None, end_date=None, option=None):
        """Obtiene los datos de nacionalizaciones desde la vista de base de datos"""
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

    def transform_data(self, report_data):
        """Transforma los datos al formato JSON requerido"""
        data = []

        for item in report_data:
            # Determinar la fecha más relevante para usar
            date_field = self.get_relevant_date(item)

            # Crear el objeto de salida
            output_item = {
                "location": "ALMACEN SIN IMPUESTOS IMNAC",
                "code": item.get('cod_contable', '') or item.get('product', ''),
                "date": self.format_date(date_field),
                "quantity": float(item.get('unidades', 0) or 0)
            }
            data.append(output_item)

        return data

    def get_relevant_date(self, item):
        """Obtiene la fecha de llegada del cliente"""
        # Usar siempre la fecha de llegada del cliente
        return item.get('fecha_llegada_cliente')

    def format_date(self, date_value):
        """Formatea la fecha al formato ISO requerido con milisegundos y UTC"""
        if date_value is None:
            return None

        if isinstance(date_value, str):
            try:
                # Intentar parsear la fecha si es string
                date_obj = datetime.strptime(date_value, '%Y-%m-%d')
                return date_obj.strftime('%Y-%m-%dT%H:%M:%S.000Z')
            except ValueError:
                return date_value
        elif hasattr(date_value, 'strftime'):
            # Si es un objeto datetime o date
            return date_value.strftime('%Y-%m-%dT%H:%M:%S.000Z')

        return str(date_value)

