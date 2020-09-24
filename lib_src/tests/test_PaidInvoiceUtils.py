from django.test import TestCase

from lib_src import InvoicesUtils
from paids.models import PaidInvoice


class InvoiceUtilsTEST(TestCase):

    def setUp(self):
        self.invoice_utils = InvoicesUtils()
        return super().setUp()

    def test_get(self):
        # busqueda por numero de factura
        id_spected_data = [262, 5887]
        per_nro_invoice = self.invoice_utils.get(nro_invoice=50)
        for i, invoice in enumerate(per_nro_invoice):
            self.assertEqual(
                invoice, PaidInvoice.get_by_id(id_spected_data[i]))

        # busqueda por numero de pedido 330-19
        id_spected_data = [
            8872,
            8970,
            8877,
            8893,
            8940,
            8894,
            7499,
            8574,
            8651,
            8654,
            9443,
            8904,
            9107,
            9427
        ]
        per_nro_order = self.invoice_utils.get(nro_order='330-19')
        self.assertEqual(id_spected_data.__len__(), per_nro_order.__len__())

        # busqueda por proveedor

        # busqueda por rangos de fechas

        # busqueda por fecha de aprobacion
