import pdb
from decimal import Decimal

from django.db import connection
from django.db.models import QuerySet
from paids.models import PaidInvoice
from django.test import TestCase

from logs import loggin
from paids.models import PaidInvoice


class PaidInvoiceTEST(TestCase):

    def setUp(self):
        self.paid_invoice = PaidInvoice()
        return super().setUp()
    
    def test_get_by_id(self):
        spected_data = {
            'id_documento_pago' : 69,
            'nro_factura' : '002-001-29994',
            'valor' : Decimal(165),
            'tipo' : 'SERVICIO',
            'identificacion_proveedor_id': '0990304262001',
        }
        data = self.paid_invoice.get_by_id(69)
        for k in spected_data:
            self.assertEqual(spected_data[k],data.__dict__[k])

        data = self.paid_invoice.get_by_id(0)
        self.assertEqual(None, data)

    
    def test_get_autorizedby_audit(self):
        ''' 
        update documento_pago set bg_audit = 1 where fecha_emision < '2019-12-31'
        '''
        with connection.cursor() as cursor:
            cursor.execute("update documento_pago set bg_audit = 1 "
            "where fecha_emision < '2019-12-31'")
        
        spected_rows = 8875
        data = self.paid_invoice.get_autorized_by_audit()
        self.assertIsInstance(data, QuerySet)
        self.assertEqual(spected_rows, data.count())
    
    
    def test_get_deny_by_audit(self):   
        spected_rows = 284
        data = self.paid_invoice.get_deny_by_audit()
        self.assertIsInstance(data, QuerySet)
        self.assertEqual(data.count(), spected_rows)
