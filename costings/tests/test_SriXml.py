from django.test import TestCase
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
            }
        ]
        
        file_data = open('costings/tests/sri_data/importations.txt', 'r')
        imports = file_data.read()
        cleaned_data = self.ice_sri_xml.clean_imports(imports)
        for spected in spected_dafa:
            for returned in cleaned_data:
                if spected['impCodProdICE'] == returned['impCodProdICE']:
                    if spected['refICE'] == returned['refICE']:
                        self.assertEqual(spected, returned)
