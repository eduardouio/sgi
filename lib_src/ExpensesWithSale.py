"""
    Obtiene todos los gastos que tienen sprofaldo en la base de datos,
    todos los gastos con saldo se mmuestran generando un reporte de pendientes
    TODO Incluir la fecha de llegada del pructo Almagro, Vinesa, no importa si es pedido o parcial o hacia almagro
    TODO Tomar en cuenta la fecha de llegada a almagro para alertas 4 d'ias normar 5-8 amarillo mas de 8 rojo
"""

from partials.models import Partial
from orders.models import Order
from datetime import date
from django.db import connection



class ExpensesWithSale(object):

    def get_all_expeneses_with_sale(self):
        """Retorna una lista completa con los gastos de
        nacionalizacion sin cerrar
        """
        cursor = connection.cursor()
        cursor.execute(""" SELECT *
                            FROM v_sgi_provisiones_pagos
                            WHERE saldo != 0 order by tipo, concepto, fecha""")
        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        for expense in result:
            expense.update(self.__get_dates(expense))

        return result

    def __get_dates(self, expense):
        """Obtiene las fehcas de llegada a Almagro, o a Vinesa, dependiente
        si es consumo o Parcial

        Args:
            id_expense (int): id de gasto nacionalizacion
        """
        result = {
            'regimen': None,
            'pedido': None,
            'fecha_ingreso_almacenera': None,
            'fecha_llegada_cliente': None
        }

        if expense['id_parcial'] == 0:
            order = Order.get_by_order(expense['nro_pedido'])
            result['fecha_llegada_cliente'] = order.fecha_llegada_cliente
        else:
            partial = Partial.get_by_id(expense['id_parcial'])
            order = partial.nro_pedido
            result['fecha_llegada_cliente'] = partial.fecha_llegada_cliente

        result['regimen'] = order.regimen
        result['pedido'] = order.nro_pedido
        result['fecha_ingreso_almacenera'] = order.fecha_ingreso_almacenera

        return result
