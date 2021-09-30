"""
Genera el anexo xml del ICe a partir de los valores de reportados desde excell
"""
from django.conf import settings
from logs.app_log import loggin
import xml.etree.ElementTree as ET


class IceSriXml(object):

    def __init__(self):
        self.sales = None
        self.returns = None
        self.report = None
        self.xml_report = None
        self.importations = None
        self.year = None
        self.month = None
        self.bg_error = False
        self.message_erros = ''

    def set_data(self, sales, returns, importations, year, month):
        loggin('i', 'Llamada a generador reporte Sri')
        if sales.__len__() == 0:
            loggin("e", "No existen datos para trabajar en el reporte")
            return None

        if returns.__len__() == 0:
            loggin("w", "El reporte se genera sin devoluciones")

        sales = sales.split("\n")
        sales = [s.split("\t") for s in sales]

        returns = returns.split("\n")
        returns = [r.split("\t") for r in returns]

        importations = importations.split("\n")
        self.importations = [i.split("\t") for i in importations]

        self.year = year
        self.month = month
        self.sales = self.check_data(sales)
        self.returns = self.check_data(returns)

    def check_data(self, data):
        """Comprueba los totales de la información con las sumas de cada
        columna y fila de los arreglos

        Args:
            type (lisr): indica la categoria a la que se debe hacer referencia
            sales o returns (devoluciones)
        """
        headers = data[0]
        del(headers[-1])
        total_result_x = [f.strip().replace(',', '') for f in data[-1]]
        total_result_x = [int(f)
                              for i, f in enumerate(total_result_x) if i > 0]
        del(total_result_x[-1])
        del(data[0])
        del(data[-1])
        total_result_y = [int(x[-1]) for x in data]

        rows = []
        cleaned_data = []
        cols = [0 for r in range(data[0].__len__() - 2)]
        for idx, row in enumerate(data):
            cleaned_row = []
            total_row = 0

            for idy, col in enumerate(row):
                if idy > 0:
                    col = col.strip()
                    col = 0 if col == '' else int(col)
                    if idy < row.__len__() - 1:
                        total_row += col
                        cols[idy-1] += col

                cleaned_row.append(col)

            rows.append(total_row)
            del(cleaned_row[-1])
            cleaned_data.append(cleaned_row)

        if total_result_x == cols and total_result_y == rows:
            loggin('i', 'Informacion Validada Correctamente')
            return {
                'headers': headers,
                'data': cleaned_data,
                'rows': rows,
                'cols': cols
            }

        loggin('e', 'Los datos no coinciden')
        self.bg_error = True
        self.message_erros = ('Los valores ingresados no coinciden favor '
                'verificar el reporte, las sumas de las columnas o filas'
                ' no corresponde'
        )

        return []

    def gerate_report(self):
        loggin('i', 'Comenzamos la construccion del reporte')
        xml_report = {
                'headers': {
                    'TipoIDInformante': 'R',
                    'IdInformante': settings.EMPRESA['ruc'],
                    'razonSocial': settings.EMPRESA['nombre'],
                    'Anio': self.year,
                    'Mes': self.month,
                    'actImport': '01',
                    'codigoOperativo': 'ICE',
                },
                'ventas': [],
                'importaciones': []
        }

        for row in self.sales['data']:
            arr = {
                'cod_ice': row[0],
                'ventas': [{'id': x, 'cant': y}
                           for x, y in zip(['0992716428001', '0992870230001', '1792049598001', '1792288916001'], row[1:])],
                'devoluciones': 0
            }

            xml_report['ventas'].append(arr)

        
        import ipdb;ipdb.set_trace()
        xml_report['importaciones'] = self.__get_imports()

        final_report = []
        for vta in xml_report['ventas']:
            if vta['ventas']:
                for line in xml_report['ventventas']:
                    final_report.append({
                        'codProdICE': vta['cod_ice'],
                        'gramoAzucar': '0.00',
                        'tipoIdCliente': 'R' if len(line['id']) == 13 else 'C',
                        'idCliente': line['id'],
                        'tipoVentaICE': 1,
                        'ventaICE': line['cant'],
                        'devICE': self.__consolidate_devs(vta, line),
                        'cantProdBajaICE': 0
                    })
            else:
                for line in vta['devoluciones']:
                    final_report.append({
                        'codProdICE': vta['cod_ice'],
                        'gramoAzucar': '0.00',
                        'tipoIdCliente': 'R' if len(line['id']) == 13 else 'C',
                        'idCliente': line['id'],
                        'tipoVentaICE': 1,
                        'ventaICE': 0,
                        'devICE': line['cant'],
                        'cantProdBajaICE': 0
                    })

        xml_report['ventas'] = final_report
        self.xml_report = xml_report

    def __consolidate_devs(self, ventas, line):
        if ventas['devoluciones'] is None:
            return 0

        for item in ventas['devoluciones']:
            if item['id'] == line['id']:
                return item['cant']

        return 0

    def get_xml(self):
        # cargamos la cabecera del report
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

    def __get_devs(self, cod_ice):
        for row in self.returns['data']:
            if row[0] == cod_ice:
                return [{'id': x, 'cant': y}
                        for x, y in zip(self.returns['headers'][1:], row[1:])
                        ]

    def __get_imports(self):
        importations = []
        for row in self.importations:
            item = {
                'impCodProdICE': row[0],
                'refICE': '-'.join([row[-4], row[-3], row[-2], row[-1]]),
                'impFDesadICE': row[1].replace('-', '/'),
                'paisICE': row[0][29:32],
                'impCantICE': row[3]
            }

            cods = [i['impCodProdICE'] for i in importations]
            # es un codigo ice duplicado, verificamos si es de la misma dai
            if item['impCodProdICE'] in cods:
                for i in importations:
                    old = i.copy()
                    new = item.copy()
                    del(old['impCantICE'])
                    del(new['impCantICE'])

                    if old == new:
                        i['impCantICE'] = str(
                            int(i['impCantICE']) + int(item['impCantICE'])
                        )
            else:
                importations.append(item)

        return importations
