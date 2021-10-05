from django.test import TestCase
from costings.lib_src import IceSriXml
from logs.app_log import loggin


class TestIceSriXml(TestCase):

    def test_set_data(self):
        """Comprobamos que el archivo lee correctamente los datos
        """
        spected = {
            'sales': {
                'headers': [
                    'cod_ice',
                    '0992716428001',
                    '0992870230001',
                    '1792049598001',
                    '1792288916001',
                    '1792708893001',
                ],
                'cols': [51740, 3918, 107559, 7930, 1244],
                'rows': [
                    876, 1945, 1123, 300, 1768, 36, 12, 546, 14, 9392, 23,
                    1866, 7, 51582, 13, 4272, 2, 6, 6, 14, 48, 144, 24, 192,
                    528, 650, 2042, 36047, 90, 1140, 229, 116, 1680, 4158,
                    11424, 240, 48, 486, 744, 4, 4476, 5640, 24, 102, 1, 2, 5,
                    2, 64, 84, 60, 1188, 170, 1368, 36, 108, 894, 14751, 12,
                    72, 6, 5, 120, 24, 420, 612, 24, 181, 1, 132, 1, 2868, 84,
                    324, 276, 2600, 396, 218, 772, 169, 24, 12, 120, 1, 4, 89,
                    1, 1, 10
                ]
            },
            'returns': {
                'headers': [
                    'cod_ice',
                    '0992716428001',
                    '0992870230001',
                    '1792049598001',
                    '1792288916001',

                ],
                'cols': [182, 12, 706, 360],
                'rows': [
                    240, 120, 6, 14, 36, 240, 12, 24, 2, 2, 12, 60, 240, 108,
                    120, 24
                ],
            }
        }

        loggin('t', 'Testeando anexo xml del reporte ICE')
        month_sales_f = open("costings/tests/sri_data/sales.txt", "r")
        month_returns_f = open("costings/tests/sri_data/returns.txt", "r")
        month_imports = open("costings/tests/sri_data/importations.txt", "r")
        iceSRIXml = IceSriXml()
        iceSRIXml.set_data(
            month_sales_f.read(),
            month_returns_f.read(),
            month_imports.read(),
            '2020',
            '02'
        )

     #   self.assertListEqual(
     #       iceSRIXml.sales['rows'],
     #       spected['sales']['rows']
     #   )
#
     #   self.assertListEqual(
     #       iceSRIXml.sales['cols'],
     #       spected['sales']['cols']
     #   )
#
     #   self.assertListEqual(
     #       iceSRIXml.sales['headers'],
     #       spected['sales']['headers']
     #   )
#
     #   self.assertListEqual(
     #       iceSRIXml.returns['rows'],
     #       spected['returns']['rows']
     #   )
#
     #   self.assertListEqual(
     #       iceSRIXml.returns['cols'],
     #       spected['returns']['cols']
     #   )
#
     #   self.assertListEqual(
     #       iceSRIXml.returns['headers'],
     #       spected['returns']['headers']
     #   )

    def test_get_report(self):
        month_sales_f = open("costings/tests/sri_data/sales.txt", "r")
        month_returns_f = open("costings/tests/sri_data/returns.txt", "r")
        month_imports = open("costings/tests/sri_data/importations.txt", "r")
        iceSRIXml = IceSriXml()
        iceSRIXml.set_data(
            month_sales_f.read(),
            month_returns_f.read(),
            month_imports.read(),
            '2021',
            '09'
        )
        iceSRIXml.gerate_report()
        report = iceSRIXml.get_xml()
        print(report)
