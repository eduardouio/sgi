from datetime import datetime
from django.test import TestCase
from django.db.models import QuerySet
from django.db import connection
from lib_src.moocks.partials import partials
from orders.models.Order import Order
from orders.tests.test_model_order import create_orders
from partials.models.Partial import Partial


def create_partials(test_create = False, test_is_local=True):
    if test_is_local:
        create_orders()

    for n in partials:
        o = Order.get_by_order(n['nro_pedido'])
        n = Partial.objects.create(
                nro_pedido = o,
                tipo_cambio = n['tipo_cambio'],
                fecha_nacionalizacion = datetime.now(),
                bg_isclosed = 0,
                fecha_salida_almacenera = datetime.now(),
                proximo_almacenaje_desde = datetime.now(),
                otros = 0,
                exoneracion_arancel = 100,
                bg_have_etiquetas_fiscales = 0,
                bg_isliquidated = 0
        )

        if test_create:
            return n


class TestModelParcial(TestCase):
    
    def setUp(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Order)
            schema_editor.create_model(Partial)
        
        if Order._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test database'.format(table_bame=Order._meta.db_table))

        if Partial._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test database'.format(table_bame=Partial._meta.db_table))

    
    def tearDown(self):
        return super().tearDown()
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(Partial)
            schema_editor.delete_model(Order)


    def test_create(self):
        n = create_partials(test_create= True)
        self.assertIsInstance(n, Partial)
        self.assertEqual(n.id_parcial, 1)

    def test_update(self):
        create_partials()
        n  = Partial.objects.get(pk = 2)
        self.assertEqual(2, n.id_parcial)
        self.assertIsInstance(n,Partial)
        n.tipo_cambio = 100
        n.save()
        self.assertEqual(n.tipo_cambio, 100)

    def test_get_by_order(self):
        create_partials()
        n = Partial.get_by_order(nro_order = '030-18')
        self.assertIsInstance(n,QuerySet)
        self.assertEqual(1, n.count())