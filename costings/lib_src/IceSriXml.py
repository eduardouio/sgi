"""
Genera el anexo xml del ICe a partir de los valores de reportados desde excell
"""
import re
from django.conf import settings
import ipdb
from logs.app_log import loggin
import xml.etree.ElementTree as ET
import csv


class IceSriXml(object):
    
    def get_xml_report(self, base_report):
        # TODO verificar que el reporte sea valido
        root = ET.Element('ice')
        for k, v in self.xml_report['headers'].items():
            header = ET.SubElement(root, k)
            header.text = v

        # cargamos las ventas en el reporte
        ventas = ET.SubElement(root, 'ventas')
        for line in self.xml_report['ventas']:
            vta = ET.SubElement(ventas, 'vta')
            for k, v in line.items():
                el = ET.SubElement(vta, k)
                el.text = str(v)

        # cargamos las importaciones
        importaciones = ET.SubElement(root, 'importaciones')

        for line in self.xml_report['importaciones']:
            imp = ET.SubElement(importaciones, 'imp')
            for k, v in line.items():
                el = ET.SubElement(imp, k)
                el.text = v

        return ET.tostring(root).decode()

    def get_report(self, year, month, sales, devs, imports):
        loggin('i', 'Se inicia generacion del reporte')
        base_report = {
            'headers': {
                'TipoIDInformante': 'R',
                'IdInformante': settings.EMPRESA['ruc'],
                'razonSocial': settings.EMPRESA['nombre'],
                'Anio': year,
                'Mes': month,
                'actImport': '01',
                'codigoOperativo': 'ICE',
            },
            'sales': [],
            'importations': []
        }

        head_sales = sales[0]
        for vta in sales[1:-1]:
            for k, venta in enumerate(vta[1:-1], start=1):
                type_client = 'R' if head_sales[k].__len__() == 14 else 'C'

                if venta > 0:
                    base_report['sales'].append({
                        'codProdICE': vta[0],
                        'gramoAzucar': '0.00',
                        'tipoIdCliente': type_client,
                        'idCliente': head_sales[k][1:],
                        'tipoVentaICE': '1',
                        'ventaICE': str(venta),
                        'devICE': '0',
                        'cantProdBajaICE': '0',
                    })

        head_devs = devs[0]
        delete_keys = []
        additionals_devs = []

        for idx, dev in enumerate(devs[1:-1]):
            for k, cant in enumerate(dev[1:-1], start=1):
                type_client = 'R' if head_devs[k].__len__() == 14 else 'C'
                if cant > 0:
                    for sale in base_report['sales']:
                        if sale['codProdICE'] == dev[0] and sale['idCliente'] == head_devs[k][1:]:
                            sale['devICE'] = str(cant)
                            delete_keys.append(idx)

        for k, dev in enumerate(devs[1:-1]):
            if k not in delete_keys:
                additionals_devs.append(dev)

        for dev in additionals_devs:
            for k, cant in enumerate(dev[1:-1], start=1):
                type_client = 'R' if head_devs[k].__len__() == 14 else 'C'
                if cant > 0:
                    base_report['sales'].append({
                        'codProdICE': dev[0],
                        'gramoAzucar': '0.00',
                        'tipoIdCliente': type_client,
                        'idCliente': head_devs[k][1:],
                        'tipoVentaICE': '1',
                        'ventaICE': '0',
                        'devICE': str(cant),
                        'cantProdBajaICE': '0',
                    })

        base_report['importations'] = imports
        return base_report

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
            ref_ice = '-'.join([row[-4], row[-3], row[-2], row[-1]])
            keys = [i['impCodProdICE'] for i in report]

            if row[2] in keys:
                for itm in report:
                    if itm['impCodProdICE'] == row[2] and itm['refICE'] == ref_ice:
                        itm['impCantICE'] = str(
                            int(itm['impCantICE']) + int(row[6])
                        )
            else:
                report.append({
                    'impCodProdICE': row[2],
                    'refICE': ref_ice,
                    'impFDesadICE': row[3].replace('-', '/'),
                    'paisICE': row[2][-10:-7],
                    'impCantICE': row[6]
                })

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
