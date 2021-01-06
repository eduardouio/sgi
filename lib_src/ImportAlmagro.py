"""
Importa informacion de los saldos de almagro y actualiza el sistema
de importaciones con, la importacion lo realiza desde una archivo CVS
    Matricula
    BL
"""

import csv

from logs.app_log import loggin
from orders.models import Order


class ImportAlmagro():
    # TODO realizar la importacion de la informacion desde el archivo de Almagro

    def set_data(self, data_csv):
        # TODO leer el archivo con la informacion de almagro y obtener la  
        pass
