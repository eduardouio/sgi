from django.test import TestCase
import ipdb
from costings.lib_src import IceSriXml


class TestIceSriXml(TestCase):

    def setUp(self) -> None:
        self.ice_sri_xml = IceSriXml()
        return super().setUp()

    def test_clean_sales(self):
        file_data = open('costings/tests/sri_data/sales.txt', 'r')
        sales = file_data.read()
        clean_data = self.ice_sri_xml.clean_data(sales)
        self.assertEqual(clean_data[6][5], 6)
        self.assertEqual(clean_data[8][1], 1200)
        self.assertEqual(clean_data[26][2], 3114)
        self.assertEqual(clean_data[14][7], 210)
        self.assertEqual(clean_data[26][1], 59261)
        self.assertEqual(clean_data[0][1], 'C0992716428001')
        self.assertEqual(clean_data[1][0],
                         '3031-53-001425-013-000750-66-108-000037'
        )

    def test_clean_devs(self):
        file_data = open('costings/tests/sri_data/returns.txt', 'r')
        sales = file_data.read()
        clean_data = self.ice_sri_xml.clean_data(sales)
        self.assertEqual(clean_data[8][5], 3862)
        self.assertEqual(clean_data[4][3], 240)
        self.assertEqual(clean_data[4][4], 0)
        self.assertEqual(clean_data[3][4], 170)
        self.assertEqual(clean_data[0][2], 'C0992870230001')
        self.assertEqual(clean_data[1][0],
                         '3031-53-001425-013-000750-66-108-000037'
        )

    def test_imports(self):
        spected_dafa = [
            {
                'impCodProdICE': '3031-53-036359-013-000750-66-209-000146',
                'refICE': '055-2021-10-00078585',
                'impFDesadICE': '21/09/2021',
                'paisICE': '209',
                'impCantICE': '2400'
            },
            {
                'impCodProdICE': '3031-53-036357-013-000750-66-209-000146',
                'refICE': '055-2021-10-00785851',
                'impFDesadICE': '21/09/2021',
                'paisICE': '209',
                'impCantICE': '2400',
            },
            {
                'impCodProdICE': '3031-53-001425-013-000750-66-108-000037',
                'refICE': '055-2021-10-00801478',
                'impFDesadICE': '28/09/2021',
                'paisICE': '108',
                'impCantICE': '1800',
            },
            {
                'impCodProdICE': '3031-56-002075-013-000750-66-211-000024',
                'refICE': '055-2021-10-00801495',
                'impFDesadICE': '28/09/2021',
                'paisICE': '211',
                'impCantICE': '1200',
            },
            {
                'impCodProdICE': '3031-56-002075-013-000750-66-211-000024',
                'refICE': '028-2021-70-00778062',
                'impFDesadICE': '13/09/2021',
                'paisICE': '211',
                'impCantICE': '1200',
            },
            {
                'impCodProdICE': '3031-56-002076-013-000750-66-211-000026',
                'refICE': '028-2021-70-00778062',
                'impFDesadICE': '13/09/2021',
                'paisICE': '211',
                'impCantICE': '3000',
            },
        ]

        file_data = open('costings/tests/sri_data/importations.txt', 'r')
        imports = file_data.read()
        cleaned_data = self.ice_sri_xml.clean_imports(imports)

        for spected in spected_dafa:
            for returned in cleaned_data:
                if spected['impCodProdICE'] == returned['impCodProdICE']:
                    if spected['refICE'] == returned['refICE']:
                        self.assertEqual(spected, returned)

    def test_report(self):
        spected_sales = [
            {
                'codProdICE': '3031-53-001425-013-000750-66-108-000037',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '0992870230001',
                'tipoVentaICE': '1',
                'ventaICE': '120',
                'devICE': '0',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3031-53-001425-013-000750-66-108-000037',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '1704477536001',
                'tipoVentaICE': '1',
                'ventaICE': '2',
                'devICE': '0',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3031-53-001425-013-000750-66-108-000037',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'C',
                'idCliente': '1704670726',
                'tipoVentaICE': '1',
                'ventaICE': '12',
                'devICE': '0',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3031-53-001425-013-000750-66-108-000037',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '1790016919001',
                'tipoVentaICE': '1',
                'ventaICE': '300',
                'devICE': '60',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3031-53-001425-013-000750-66-108-000037',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '1792288916001',
                'tipoVentaICE': '1',
                'ventaICE': '72',
                'devICE': '0',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3053-84-026708-013-000200-66-213-000144',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '1790016919001',
                'tipoVentaICE': '1',
                'ventaICE': '480',
                'devICE': '240',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3031-53-009849-031-001000-66-101-000027',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '0992716428001',
                'tipoVentaICE': '1',
                'ventaICE': '0',
                'devICE': '2400',
                'cantProdBajaICE': '0'
            },
            {
                'codProdICE': '3031-56-002075-013-000750-66-211-000024',
                'gramoAzucar': '0.00',
                'tipoIdCliente': 'R',
                'idCliente': '1792049598001',
                'tipoVentaICE': '1',
                'ventaICE': '0',
                'devICE': '170',
                'cantProdBajaICE': '0'
            },
        ]

        spected_imports = [
            {
                'impCodProdICE': '3031-53-036360-013-000750-66-209-000146',
                'refICE': '055-2021-10-00785851',
                'impFDesadICE': '21/09/2021',
                'paisICE': '209',
                'impCantICE': '2400',
            },
            {
                'impCodProdICE': '3031-53-036359-013-000750-66-209-000146',
                'refICE': '055-2021-10-00078585',
                'impFDesadICE': '21/09/2021',
                'paisICE': '209',
                'impCantICE': '2400',
            },
            {
                'impCodProdICE': '3031-53-036357-013-000750-66-209-000146',
                'refICE': '055-2021-10-00785851',
                'impFDesadICE': '21/09/2021',
                'paisICE': '209',
                'impCantICE': '2400',
            },
            {
                'impCodProdICE': '3031-53-001425-013-000750-66-108-000037',
                'refICE': '055-2021-10-00801478',
                'impFDesadICE': '28/09/2021',
                'paisICE': '108',
                'impCantICE': '1800',
            },
            {
                'impCodProdICE': '3031-56-002075-013-000750-66-211-000024',
                'refICE': '055-2021-10-00801495',
                'impFDesadICE': '28/09/2021',
                'paisICE': '211',
                'impCantICE': '1200',
            },
            {
                'impCodProdICE': '3031-56-025188-013-000750-66-211-000024',
                'refICE': '055-2021-10-00801495',
                'impFDesadICE': '28/09/2021',
                'paisICE': '211',
                'impCantICE': '2400',
            },
        ]

        sales = open('costings/tests/sri_data/sales.txt', 'r')
        devs = open('costings/tests/sri_data/returns.txt', 'r')
        imports = open('costings/tests/sri_data/importations.txt', 'r')

        sales = sales.read()
        devs = devs.read()
        imports = imports.read()

        sales = self.ice_sri_xml.clean_data(sales)
        devs = self.ice_sri_xml.clean_data(devs)
        imports = self.ice_sri_xml.clean_imports(imports)
        report = self.ice_sri_xml.get_report(
            '2021', '11', sales, devs, imports
        )

        for spected in spected_sales:
            for returned in report['sales']:
                if spected['codProdICE'] == returned['codProdICE']:
                    if spected['idCliente'] == returned['idCliente']:
                        self.assertEqual(spected, returned)

        for spected in spected_imports:
            for returned in report['importations']:
                if spected['impCodProdICE'] == returned['impCodProdICE']:
                    if spected['refICE'] == returned['refICE']:
                        self.assertEqual(spected, returned)

    def test_xml_report(self):
        sales = open('costings/tests/sri_data/sales.txt', 'r')
        devs = open('costings/tests/sri_data/returns.txt', 'r')
        imports = open('costings/tests/sri_data/importations.txt', 'r')

        sales = sales.read()
        devs = devs.read()
        imports = imports.read()

        sales = self.ice_sri_xml.clean_data(sales)
        devs = self.ice_sri_xml.clean_data(devs)
        imports = self.ice_sri_xml.clean_imports(imports)
        report = self.ice_sri_xml.get_report(
            '2021', '11', sales, devs, imports
        )
        
        xml_report = self.ice_sri_xml.get_xml_report(report)
        
        import ipdb; ipdb.set_trace()
