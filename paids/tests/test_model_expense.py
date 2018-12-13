from django.test import TestCase
from django.db import connection
from django.db.models.query import QuerySet
from orders.models.Order import Order
from orders.tests.test_model_order import create_orders
from paids.models.Expense import Expense
from suppliers.models.Supplier import Supplier
from suppliers.tests.test_supplier_model import create_suppliers
from lib_src.moocks.expenses import expenses
from datetime import  datetime


def create_expenses(test_create = False, test_is_local = True):
    if test_is_local:
        create_suppliers()
        create_orders()
    
    for x in expenses:
        o = Order.get_by_order(x['nro_pedido'])
        s = Supplier.get_by_ruc(x['identificacion_proveedor'])
        n = Expense.objects.create(
            nro_pedido = o,
            id_parcial = 0,
            identificacion_proveedor = s,
            concepto = x['concepto'],
            tipo = x['tipo'],
            valor_provisionado = x['valor_provisionado'],
            fecha = datetime.now() 
        )
        if(test_create):
            return n
    

class TestModelExpense(TestCase):
    def setUp(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Supplier)
            schema_editor.create_model(Order)
            schema_editor.create_model(Expense)
            
        if Supplier._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missig in test database'.format(table_name=Supplier._meta.db_table))

        if Order._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missig in test database'.format(table_name=Order._meta.db_table))

        if Expense._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missig in test database'.format(table_name=Expense._meta.db_table))

    def tearDown(self):
        super().tearDown()
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(Expense)
            schema_editor.delete_model(Supplier)
            schema_editor.delete_model(Order)
    
    def test_create(self):
        n = create_expenses(test_create=True)
        self.assertTrue(n, Expense)
        self.assertEqual(n.__str__(), '1 AGENTE ADUANA')
    
    def test_update(self):
        create_expenses()
        n = Expense.objects.get(pk=1)
        self.assertIsInstance(n, Expense)        
        self.assertEqual(n.__str__(), '1 AGENTE ADUANA')
    
    def test_get_by_order(self):
        create_expenses()
        exp = Expense.get_by_order('000-00')
        self.assertIsInstance(exp, QuerySet)
        data = [
                "AGENTE ADUANA",
                "DEPOSITO 2018Jun-2018Jul",
                "DEPOSITO 2018May-2018Jun",
                "DEPOSITO 2017Dic-2018Ene",
                "DEPOSITO 2017Nov-2017Dic",
                "DEPOSITO 2018Abr-2018May",
                "DEPOSITO 2018Mar-2018Abr",
                "DEPOSITO 2018Feb-2018Mar",
                "MANO DE OBRA ETIQUETADO",
                "DESCARGA",
                "ETIQUETAS FISCALES",
                "TRANSPORTE",
            ]
        for item in exp:
            if item.concepto in data:
                self.assertTrue(True)
            else:
                self.assertTrue(False)

        self.assertEqual(exp.count(), data.__len__())

    def get_by_parcial(self):
        '''Test no funciona provar con base de datos en produccion'''
        create_expenses()
        exp = Expense.get_by_parcial(1)
        self.assertIsInstance(exp, QuerySet)
        self.assertEqual(exp.count(), 4)
        data = [
            "DEPOSITO 2018Feb-2018Mar",
            "DESCARGA",
            "ETIQUETAS FISCALES",
            "TRANSPORTE",
        ]
        for item in exp:
            self.assertTrue(False)