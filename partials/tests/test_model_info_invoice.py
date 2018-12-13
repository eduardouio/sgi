from datetime import datetime
from django.test import TestCase
from django.db import connection
from django.db.models import QuerySet
from lib_src.moocks.infoinvoices import infoinvoices
from partials.models.Partial import Partial
from suppliers.models.Supplier import Supplier
from orders.models.Order import Order
from orders.tests.test_model_order import create_orders
from suppliers.tests.test_supplier_model import create_suppliers
from partials.tests.test_model_partial import create_partials
from partials.models.InfoInvoice import InfoInvoice

def create_infoinvoices(test_create = True, test_is_local = True):
    if test_is_local:
        create_orders()
        create_suppliers()
        create_partials(test_is_local=False)
    
    for item in infoinvoices:
        p = Partial.objects.get(pk=item['id_parcial'])
        s = Supplier.get_by_ruc(item['identificacion_proveedor'])

        n = InfoInvoice.objects.create(
            id_parcial = p,
            nro_factura_informativa = item['nro_factura_informativa'],
            identificacion_proveedor = s,
            fecha_emision = datetime.now(),
            flete_aduana = item['flete_aduana'],
            seguro_aduana = item['seguro_aduana'],
            valor = 1919,
            moneda = item['moneda'],
            tipo_cambio = item['tipo_cambio'],
            bg_isclosed = 0,
            gasto_origen = item['gasto_origen'],
            id_user = item['id_user'],
            bg_gst_origen_por_factura = 0,
        )
        if test_create:
            return n


class TestInfoInvoice(TestCase):
    
    def setUp(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Order)
            schema_editor.create_model(Supplier)
            schema_editor.create_model(Partial)
            schema_editor.create_model(InfoInvoice)

        if Supplier._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test model'.format(table_name=Supplier._meta.db_table))

        if Order._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test model'.format(table_name=Order._meta.db_table))

        if Partial._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test model'.format(table_name=Partial._meta.db_table))

        if InfoInvoice._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test model'.format(table_name=InfoInvoice._meta.db_table))

    def tearDown(self):
        return super().tearDown()
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(InfoInvoice)
            schema_editor.delete_model(Partial)
            schema_editor.delete_model(Order)
    
    def test_create(self):
        n = create_infoinvoices(test_create=True)
        self.assertIsInstance(n, InfoInvoice)
        self.assertEqual(n.__str__(), '2015333')
    
    def test_update(self):
        create_infoinvoices()
        n = InfoInvoice.objects.get(pk=1)
        n.gasto_origen = 999
        n.save()
        self.assertEqual(n.gasto_origen, 999)
    
    def test_get_by_order(self):
        create_infoinvoices()
        n = InfoInvoice.get_by_order('007-18')
        self.assertEqual(2, n.__len__())
        for x in n:
            self.assertIsInstance(x, QuerySet)