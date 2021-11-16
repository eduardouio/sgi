"""
Genera el anexo xml del ICe a partir de los valores de reportados desde excell
"""
from django.conf import settings
from django.http import response
from logs.app_log import loggin
import xml.etree.ElementTree as ET
import csv


class IceSriXml(object):

    def __init__(self):
        self.xml_report = None
        self.dict_report = None

    def clean_data(self, data):
        loggin('i', 'Se inicia limpieza de datos de ventas')
        data = data.replace(',', '')
        data = csv.reader(data.split('\n'), delimiter=';', dialect='excel')
        data = [_ if _ else 0 for _ in data]
        cleaned_data = []
        for row in data:
            cleaned_data.append(
                [self.__get_number(itm.strip()) if bool(itm) else 0 
                 for itm in row]
            )

        if self.__check_sums(cleaned_data):
            return cleaned_data

        return False

    def clean_imports(self, imports):
        loggin('i', 'Se inicia limpieza de datos de importaciones')
        imports = imports.replace(',', '')
        imports = csv.reader(imports.split('\n'), delimiter=';', dialect='excel')
        imports = [_ if _ else 0 for _ in imports]
        report = []

        for row in imports:
            report.append({
                'impCodProdICE': row[2],
                'refICE': '-'.join([
                    row[-4],
                    row[-3],
                    row[-2],
                    row[-1],
                    ]),
                'impFDesadICE': row[3].replace('-', '/'),
                'paisICE': row[2][-10:-7],
                'impCantICE': row[6]
            })

        # Eliminamos los duplicados
        cods_ice = [i['impCodProdICE'] for i in report]
        seen = list(set(cods_ice))
        # buscamos los duplicados y hacer que se unifiquen en una sola fila
        for cod in cods_ice:
            if cod not in seen:
                report.remove(cod)   
            
        

        import ipdb;ipdb.set_trace()
        return report

    def __get_number(self, number):
        try:
            return int(number)
        except ValueError:
            return number

    def __check_sums(self, data):
        rows_sums = [_[-1] for _ in data]

        for key, row in enumerate(data[1:-1], start=1):

            sum_row = sum([_ for _ in row[1:-1]])
            if sum_row != rows_sums[key]:
                loggin('e', 'Error en la suma de la fila {}'.format(key))
                return False

        return True
