import pdb

from django.test import TestCase

from logs.app_log import loggin
from paids.models import PaidInvoice, PaidInvoiceDetail, Expense


class PaidInvoiceDetailTEST(TestCase):

    def setUp(self):
        return super().setUp()
    

    def test_get_by_id(self):
        spected_data = [
            {'id_documento_pago':14515,'valor':40.00, 'id_gastos_nacionalizacion':18317},
            {'id_documento_pago':335,'valor':490.00, 'id_gastos_nacionalizacion':549},
            {'id_documento_pago':580,'valor':490.00, 'id_gastos_nacionalizacion':829},
            {'id_documento_pago':1492,'valor':490.00, 'id_gastos_nacionalizacion':2751},
            {'id_documento_pago':7376,'valor':110.00, 'id_gastos_nacionalizacion':8629},
        ]
        for item in spected_data:
            result = PaidInvoiceDetail.get_by_id(item['id_documento_pago'])
            self.assertEqual(item['valor'], float(result.valor))
            self.assertEqual(Expense.get_by_id_expense(item['id_gastos_nacionalizacion']), result.id_gastos_nacionalizacion )
        #no existe detalle de factura
        result = PaidInvoiceDetail.get_by_id(0)
        self.assertIsNone(result)


    def test_get_by_expense(self):
        spected_data = [
            {'id_gastos_nacionalizacion' : 0, 'result' : [] },
            {'id_gastos_nacionalizacion' : 16226, 'result' : [] },
            {'id_gastos_nacionalizacion' : 8629, 'result' : [PaidInvoiceDetail.get_by_id(6964), PaidInvoiceDetail.get_by_id(7376)]},
            {'id_gastos_nacionalizacion' : 9272, 'result' : [PaidInvoiceDetail.get_by_id(7386)]},
            {'id_gastos_nacionalizacion' : 10415, 'result' : [PaidInvoiceDetail.get_by_id(8482)]},
        ]

        for item in spected_data:
            result = PaidInvoiceDetail.get_by_expense(False, id_expense=item['id_gastos_nacionalizacion'])
            self.assertIsInstance(item['result'],list)
            self.assertEqual(item['result'], result)


    def test_get_invoices_from_expense(self):
        spected_data = [
            {'id_gastos_nacionalizacion' : 0, 'result' : []},
            {'id_gastos_nacionalizacion' : 16226, 'result' : []},
            {'id_gastos_nacionalizacion' : 8629, 'result' : [PaidInvoice.get_by_id(4286), PaidInvoice.get_by_id(4580)]},
            {'id_gastos_nacionalizacion' : 9272, 'result' : [PaidInvoice.get_by_id(4590)]},
            {'id_gastos_nacionalizacion' : 10415, 'result' : [PaidInvoice.get_by_id(5379)]},
        ]
        for item in spected_data:
            result = PaidInvoiceDetail.get_invoices_from_expense(item['id_gastos_nacionalizacion'])
            self.assertIsInstance(result, list)
            self.assertEqual(item['result'], result)
    

    def test_get_from_order(self):
        spected_data = [
            1668, 1699, 1700, 2056, 2059, 2060, 2147, 2194, 2195, 2222, 2223, 
            2294, 2494, 2606, 2607, 2650, 2750, 2865, 3039, 3098, 3296, 3347, 
            3368, 3503, 3532, 3538, 3541, 3542, 3544, 3554, 3627, 3659, 3661,
            3950, 4156, 4365, 4926, 5213, 5302, 5360, 5372, 5379, 5384, 5424,
            5668, 6066, 6579, 6598, 6626, 6917, 7215 ]

        data = PaidInvoiceDetail.get_from_order('256-18')
        keys = [id_ddp.id_documento_pago for id_ddp in data]
        self.assertListEqual(spected_data, keys)

        for invoice in data:
            loggin('t', invoice)
            self.assertTrue(invoice.id_documento_pago in spected_data)

        #no existe
        data = PaidInvoiceDetail.get_from_order('dont-exist')
        self.assertIsInstance(data, list)