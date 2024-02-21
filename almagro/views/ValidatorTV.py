import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView
from orders.models import Order
from logs.app_log import loggin
from datetime import date


# /almagro/analisis/
class ValidatorTV(LoginRequiredMixin, TemplateView):
    template_name = 'almagro/analisis.html'

    def get(self, request, *args, **kwargs):
        if not request.session.get('almagro'):
            loggin('e', 'Llamafa a analisis sin informacion')
            return HttpResponseRedirect('/almagro/importar/')

        loggin('i', 'llamado a analisis con informacion')
        orders = json.loads(request.session['almagro'])

        if orders.__len__() == 0:
            loggin('i', 'archivo sin pedidos')
            del(request.session['almagro'])
            return HttpResponseRedirect('/almagro/importar/?invalid=True')

        crude_data = [
            {'almagro': order, 'sgi': Order.get_by_order(order['nro_pedido'])}
            for order in orders
        ]

        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Importar Almagro',
            'data_result': self.validator(crude_data),
            'almagro': request.session['almagro'],
        }

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        confirmed_orders = [o[4:] for o in request.POST if o.startswith('ord_')]
        options = [opt for opt in request.POST if opt.startswith('opt_')]
        orders = json.loads(request.session['almagro'])
        for item in orders:
            if item['nro_pedido'] in confirmed_orders:
                loggin('i', 'Pedido {} encontrado para importar'.format(
                    item['nro_pedido'])
                )

                order = Order.get_by_order(item['nro_pedido'])

                if 'opt_empty_only' in options:
                    loggin('i', 'Solamente se importan los campos vacios')
                    date_array = item['fecha_ingreso_almacenera'].split('-')
                    arrived = date(
                        int(date_array[0]),
                        int(date_array[1]),
                        int(date_array[2]),
                    )
                    order.nro_matricula = item['nro_matricula'] if not bool(order.nro_matricula) else order.nro_matricula
                    order.nro_bl = item['nro_bl'] if not bool(order.nro_bl) else order.nro_bl
                    order.fecha_ingreso_almacenera = arrived if not bool(order.fecha_ingreso_almacenera) else order.fecha_ingreso_almacenera

                if 'opt_bl' in options and 'opt_empty_only' not in options:
                    loggin('i', 'si importa BL')
                    order.nro_bl = item['nro_bl']

                if 'opt_matricula' in options and 'opt_empty_only' not in options:
                    loggin('i', 'si importa Matricula')
                    order.nro_matricula = item['nro_matricula']

                if 'opt_fecha' in options and 'opt_empty_only' not in options:
                    loggin('i', 'si importa Fecha ingreso Almagro')
                    date_array = item['fecha_ingreso_almacenera'].split('-')
                    arrived = date(
                        int(date_array[0]),
                        int(date_array[1]),
                        int(date_array[2]),
                    )
                    order.fecha_ingreso_almacenera = arrived
                order.save()
                loggin('i', 'pedido {} guardado'.format(item['nro_pedido']))

        del(request.session['almagro'])
        return HttpResponseRedirect('/almagro/ok/')

    def validator(self, crude_data):
        validated_data = []
        for row in crude_data:
            my_date = row['almagro']['fecha_ingreso_almacenera'].split('-')
            row['almagro']['fecha_ingreso_almacenera'] = date(
                int(my_date[0]),
                int(my_date[1]),
                int(my_date[2]),
            )
            sgi_data = {
                'nro_pedido': row['sgi'].nro_pedido,
                'nro_matricula': row['sgi'].nro_matricula,
                'nro_bl': row['sgi'].nro_bl,
                'fecha_ingreso_almacenera': row['sgi'].fecha_ingreso_almacenera
            }

            if not row['almagro'] == sgi_data:
                validated_data.append(row)

        return validated_data


# /almagro/success/
class SuccessTV(LoginRequiredMixin, TemplateView):
    template_name = 'almagro/success.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'importacion realizada correctamente')
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Accion Ejecutada correctamente'
        }
        return self.render_to_response(context)
