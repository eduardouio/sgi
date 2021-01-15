"""
Importa informacion de los saldos de almagro y actualiza el sistema
de importaciones con, la importacion lo realiza desde una archivo CVS
    Matricula
    BL
este fichero recibe el contendido del archivo, no el archivo
"""
from logs.app_log import loggin
from datetime import date
import re


class ImportAlmagro():

    def set_data(self, data):
        # TODO leer el archivo con la informacion de ala
        loggin('i', 'importando desde archivo de almagro {}'.format(__name__))
        tmp_res = []
        orders = []

        for row in data:
            tmp_res.append({
                'nro_pedido': row[13].replace('/', '-'),
                'nro_matricula': row[11],
                'nro_bl': row[14],
                'fecha_ingreso_almacenera': self.__convert_date(row[16]),
            })
        uniques_orders = set([item['nro_pedido'] for item in tmp_res])
        for item in uniques_orders:
            for res in tmp_res:
                if item == res['nro_pedido']:
                    if len(res['nro_pedido']) > 6:
                        pattern = re.compile(r'\d{3}-\d{2}')
                        lines = pattern.findall(res['nro_pedido'])
                        for lineitem in lines:
                            res['nro_pedido'] = lineitem
                            orders.append(res)
                    else:
                        orders.append(res)
                    break

        return orders

    def __convert_date(self, date_string):
        """Recinde fechas en formato 18/oct/2019

            date_string (str): fecha de reporte SAP
        """
        sections = date_string.split('/')
        base = [
            {'mont': 'Jan', 'val':  1},
            {'mont': 'Feb', 'val':  2},
            {'mont': 'Mar', 'val':  3},
            {'mont': 'Apr', 'val':  4},
            {'mont': 'May', 'val':  5},
            {'mont': 'Jun', 'val':  6},
            {'mont': 'Jul', 'val':  7},
            {'mont': 'Aug', 'val':  8},
            {'mont': 'Sep', 'val':  9},
            {'mont': 'Oct', 'val':  10},
            {'mont': 'Nov', 'val':  11},
            {'mont': 'Dec', 'val':  12},
            {'mont': 'Ene', 'val':  1},
            {'mont': 'Abr', 'val':  4},
            {'mont': 'Ago', 'val':  8},
            {'mont': 'Dic', 'val':  12},
        ]
        for item in base:
            if item['mont'].lower() == sections[1].lower():
                sections[1] = item['val']
                return date(int(sections[2]), sections[1], int(sections[0]))
