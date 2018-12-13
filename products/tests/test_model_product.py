from django.test import TestCase
from products.models.Product import Product
from suppliers.models.Supplier import Supplier
from django.db import connection
from django.db.models.query import QuerySet
from lib_src.moocks.products import products
from suppliers.tests.test_supplier_model import create_suppliers

def create_products(test_create = False, test_is_local = True):
    if test_is_local:
        create_suppliers()
    for p in products:
        s = Supplier.get_by_ruc(p['identificacion_proveedor'])
        n = Product.objects.create(
            cod_contable = p['cod_contable'],
            identificacion_proveedor = s,
            nombre = p['nombre'],
            cod_ice = p['cod_ice'],
            capacidad_ml = p['capacidad_ml'],
            cantidad_x_caja = p['cantidad_x_caja'],
            grado_alcoholico = 12,
            costo_caja = 12.32,
            estado = 1,
            custodia_doble = 0,
            peso = 0,
            id_user = 0
        )
        if test_create:
            return n


class TestModelProduct(TestCase):
    def setUp(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Supplier)    
            schema_editor.create_model(Product)

        if Supplier._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test database'.format(table_name = Supplier._meta.db_table))
        
        if Product._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missing in test database'.format(table_name = Product._meta.db_table))
    
    def tearDown(self):
        super().tearDown()
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(Product)
            schema_editor.delete_model(Supplier)
    
    def test_create(self):
        n = create_products(True)
        self.assertIsInstance(n, Product)
        self.assertEqual(n.__str__(), 'CHAMPAGNE HENKELL BLANC DE BLANCS')
    
    def test_update(self):
        create_products()
        n = Product.objects.get(pk='00000000000000000009')
        n.nombre = 'OTHER NAME'
        n.save()
        self.assertIsInstance(n, Product)
        self.assertEqual(n.__str__(), 'OTHER NAME')
    
    def test_get_by_cod_contable(self):
        create_products()
        p = Product.get_by_cod_contable('01011010040306010750')
        self.assertEqual(p.__str__(),'VINO TRIVENTO TRIBU MALBEC')
        x = Product.get_by_cod_contable('DONTEXIST')
        self.assertEqual(x , None)
    
    def test_get_all(self):
        create_products()
        sps = Product.get_all()
        self.assertIsInstance(sps, QuerySet)
        
    def test_create_product_without_supplier(self):
        pass