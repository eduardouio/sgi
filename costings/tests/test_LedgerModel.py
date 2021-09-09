from django.test import TestCase
from costings.models import Ledger


class TESTLedger(TestCase):

    def test_check_fields(self):
        fields_spected = [
            'id_mayor',
            'tipo',
            'nro_pedido',
            'nro_pedido_id',
            'id_parcial',
            'costo_inicial_producto',
            'costo_producto',
            'descargas',
            'saldo_producto',
            'precio_entrega',
            'mayor_sap',
            'provisiones_sap',
            'mayor_sgi',
            'provisiones_sgi',
            'facturas_sgi',
            'reliquidacion_ice',
            'bg_mayor',
            'last_update',
            'id_user',
            'date_create',
        ]

        ledger = Ledger.objects.first()
        fields = [_ for _ in ledger.__dict__][1:]
        self.assertListEqual(fields_spected, fields)
