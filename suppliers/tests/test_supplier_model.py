from django.db import connection
from django.test import TestCase
from lib_src.moocks.suppliers import suppliers
from suppliers.models.Supplier import Supplier
from django.db.models.query import QuerySet

def create_suppliers():
    for item in suppliers:
        n = Supplier.objects.create(**item)


class TestSupplier(TestCase):
    def setUp(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Supplier)

            if Supplier._meta.db_table not in connection.introspection.table_names():
                raise ValueError('Table {table_name} is missing in test database'.format(
                    table_name=Supplier._meta.db_table))

    def tearDown(self):
        super().tearDown()
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(Supplier)

    def test_create(self):
        for supplier in suppliers:
            n = Supplier.objects.create(**supplier)
            return self.assertIsInstance(n, Supplier)

    def test_update(self):
        create_suppliers()
        n = Supplier.objects.get(pk='0027552073371')
        self.assertIsInstance(n, Supplier)
        self.assertEqual(n.nombre, 'MARNIER LAPOSTOLLE')
        n.nombre = 'OTHER NAME'
        n.save()
        self.assertEqual(n.nombre, 'OTHER NAME')
    
    def test_get__by_ruc(self):
        create_suppliers()
        n = Supplier.get_by_ruc('0027552073371')        
        self.assertEqual( n.__str__(), 'MARNIER LAPOSTOLLE')
        x= Supplier.get_by_ruc('DOESNTEXIST')        
        self.assertEqual( x, None)
    
    def test_get_all(self):
        create_suppliers()
        n = Supplier.get_all()
        self.assertIsInstance(n, QuerySet)