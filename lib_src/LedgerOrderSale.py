"""
Calcula el saldo del mayor de un pedido, dividiendolos en tres partes
Saldo producto
Gastos iniciales
Almacenajes en parciales
Saldo de gastos de Origen para pedidos FOB
"""
from logs.app_log import loggin


class LedgerOrderSale():

    def get(self, nro_order):
        """[summary]

        Args:
            nro_order ([type]): [description]
        """