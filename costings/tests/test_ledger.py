from costings.models.Ledger import Ledger
from decimal import Decimal
from django.test import TestCase
from django.db import connection
from django.db.models.query import QuerySet
from lib_src.moocks.ledgers import ledgers

def create_ledger(test_create=False,test_is_local=True):
    ''' Create moock data from ledger'''    
    for item in ledgers:
        n = Ledger.objects.create(
            name = item['name'],
            tipo = item['tipo'],
            nro_pedido = item['nro_pedido'],
            id_parcial = item['id_parcial'],
            valor_inicial = item['valor_inicial'],
            valor_inicial_facturado = item['valor_inicial_facturado'],
            saldo_inicial_facturado = item['saldo_inicial_facturado'],
            valor_distribuido = item['valor_distribuido'],
            valor_distribuido_facturado = item['valor_distribuido_facturado'],
            saldo_distribuido_facturado = item['saldo_distribuido_facturado'],
            valor_por_distribuir = item['valor_por_distribuir']
        )
        if test_create:
            return n

class TestLedger(TestCase):
    ''' Test CRUD in model Ledger '''
    
    def setUp(self):
        with connection.schema_editor() as schema_editor:
            schema_editor.create_model(Ledger)
        
        if Ledger._meta.db_table not in connection.introspection.table_names():
            raise ValueError('Table {table_name} is missin in test database'.format(table_name=Ledger._meta.db_table))

    
    def tearDown(self):
        return super().tearDown()
        with connection.shchema_editor() as schema_editor:
            schema_editor.delete_model(Ledger)


    def test_create(self):
        n = create_ledger(test_create=True)
        self.assertIsInstance(n, Ledger)
        self.assertEqual(n.__str__(), 'mayor_almacenaje')
    

    def test_update(self):
        create_ledger()
        n = Ledger.objects.get(pk=25)
        self.assertIsInstance(n,Ledger)
        self.assertEqual(n.__str__(), 'mayor_almacenaje')
        n.name = 'mayor_modificado'
        n.save()
        self.assertIsInstance(n,Ledger)
        self.assertEqual(n.__str__(), 'mayor_modificado')
    

    def test_delete(self):
        create_ledger()
        n = Ledger.objects.get(pk=3)
        self.assertTrue(n.delete())
    

    def test_get_by_order(self):
        create_ledger()        
        data  = [
                {"name":"mayor_almacenaje","tipo":"COSTOS ALAMACENAJE","nro_pedido":"110-18","id_parcial":"4","valor_inicial":"1518.050","valor_inicial_facturado":"1518.050","saldo_inicial_facturado":"0.000","valor_distribuido":"209.328","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"1308.722"},
                {"name":"mayor_gastos_inciales","tipo":"COSTOS INICIALES","nro_pedido":"110-18","id_parcial":"4","valor_inicial":"6415.960","valor_inicial_facturado":"6415.960","saldo_inicial_facturado":"0.000","valor_distribuido":"884.716","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"5531.244"},
                {"name":"mayor_gastos_origen","tipo":"COSTOS EN ORIGEN","nro_pedido":"110-18","id_parcial":"4","valor_inicial":"0.000","valor_inicial_facturado":"0.000","saldo_inicial_facturado":"0.000","valor_distribuido":"0.000","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"0.000"},
                {"name":"mayor_parcial_expenses","tipo":"COSTOS PARCIAL","nro_pedido":"110-18","id_parcial":"4","valor_inicial":"445.990","valor_inicial_facturado":"359.990","saldo_inicial_facturado":"86.000","valor_distribuido":"445.990","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"0.000"},
                {"name":"mayor_productos","tipo":"COSTO Productos","nro_pedido":"110-18","id_parcial":"4","valor_inicial":"68168.800","valor_inicial_facturado":"68168.800","saldo_inicial_facturado":"0.000","valor_distribuido":"9400.000","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"58768.800"},
                {"name":"mayor_tributos","tipo":"Costos Tributos","nro_pedido":"110-18","id_parcial":"4","valor_inicial":"5321.707","valor_inicial_facturado":"5200.780","saldo_inicial_facturado":"120.927","valor_distribuido":"5321.707","valor_distribuido_facturado":"5200.780","saldo_distribuido_facturado":"120.927","valor_por_distribuir":"0.000"},
        ]
        
        order_ledger = Ledger.get_by_order('110-18')
        self.assertEqual(order_ledger.count(), data.__len__())
        self.assertIsInstance(order_ledger, QuerySet)
        for item,x in zip(order_ledger,data):
            self.assertEqual(item.valor_inicial, Decimal(x['valor_inicial']))
            self.assertEqual(item.name , x['name'])
            self.assertEqual(item.tipo, x['tipo'])
            self.assertEqual(item.nro_pedido, '110-18')
            self.assertEqual(item.id_parcial, 0 )
        
        order_ledger = Ledger.get_by_order('129-99')
        self.assertIsInstance(order_ledger, QuerySet)
        self.assertEqual(order_ledger.count(), 0)
    

    def test_get_by_parcial(self):
        create_ledger()
        data = [ 
            {"name":"mayor_almacenaje","tipo":"COSTOS ALAMACENAJE","nro_pedido":"000-00","id_parcial":"66","valor_inicial":"1328.000","valor_inicial_facturado":"1328.000","saldo_inicial_facturado":"0.000","valor_distribuido":"181.095","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"1146.905","id_user":"25"},
            {"name":"mayor_gastos_inciales","tipo":"COSTOS INICIALES","nro_pedido":"000-00","id_parcial":"66","valor_inicial":"4282.270","valor_inicial_facturado":"4425.630","saldo_inicial_facturado":"-143.360","valor_distribuido":"575.504","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"3706.766","id_user":"25"},
            {"name":"mayor_gastos_origen","tipo":"COSTOS EN ORIGEN","nro_pedido":"000-00","id_parcial":"66","valor_inicial":"791.860","valor_inicial_facturado":"0.000","saldo_inicial_facturado":"0.000","valor_distribuido":"107.983","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"683.877","id_user":"25"},
            {"name":"mayor_parcial_expenses","tipo":"COSTOS PARCIAL","nro_pedido":"000-00","id_parcial":"66","valor_inicial":"102.770","valor_inicial_facturado":"102.770","saldo_inicial_facturado":"0.000","valor_distribuido":"102.770","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"0.000","id_user":"25"},
            {"name":"mayor_productos","tipo":"COSTO Productos","nro_pedido":"000-00","id_parcial":"66","valor_inicial":"24200.000","valor_inicial_facturado":"24200.000","saldo_inicial_facturado":"0.000","valor_distribuido":"3300.070","valor_distribuido_facturado":"0.000","saldo_distribuido_facturado":"0.000","valor_por_distribuir":"20899.930","id_user":"25"},
            {"name":"mayor_tributos","tipo":"Costos Tributos","nro_pedido":"000-00","id_parcial":"66","valor_inicial":"2332.669","valor_inicial_facturado":"2310.023","saldo_inicial_facturado":"22.646","valor_distribuido":"2332.669","valor_distribuido_facturado":"2310.023","saldo_distribuido_facturado":"22.646","valor_por_distribuir":"0.000","id_user":"25"},
        ]

        parcial_ledger = Ledger.get_by_parcial(66)
        self.assertIsInstance(parcial_ledger, QuerySet)
        self.assertEqual(parcial_ledger.count(), data.__len__())

        for item,x in zip(parcial_ledger,data):
            self.assertEqual(item.valor_inicial, Decimal(x['valor_inicial']))
            self.assertEqual(item.name , x['name'])
            self.assertEqual(item.tipo, x['tipo'])
            self.assertEqual(item.nro_pedido, '000-00')
            self.assertEqual(item.id_parcial, 66)