"""
Realiza la consulta de los productos los costos de compra cantidades 
y tipo de cambio, el reporte es por productos
"""

from products.models import Product
from django.db import connection
from logs.app_log import loggin


class ProductCostAnalysis():

    def __init__(self, cod_contable, deep=0):
        """Retorna el historico de costos de un pedido 

        Args:
            cod_contable (str): cod contable de producto
        """
        self.product = Product.get_by_cod_contable(cod_contable)
        self.deep = 0 if deep == 0 else deep

    def get(self):
        # loggin('i', 'Analizando producto {}'.format(self.product))
        if self.product is None:
            return None

        return {
            'product': self.product,
            'history': self.get_history()
        }

    def get_history(self):
        conn = connection.cursor()
        sql = '''
                select * from
                    (   select * from v_costs_analysis 
                        WHERE  cod_contable  = '{}' 
                        order by fecha_llegada_cliente desc, nro_pedido
                    ) var1  order by fecha_llegada_cliente asc, nro_pedido
                '''.format(
            self.product.cod_contable
        )

        if self.deep:
            sql = '''
                select * from
                    (   select * from v_costs_analysis
                        WHERE  cod_contable  = '{}'
                        order by fecha_llegada_cliente desc, nro_pedido limit {}
                    ) var1  order by fecha_llegada_cliente asc, nro_pedido
            '''.format(self.product.cod_contable,  self.deep)

        conn.execute(sql)
        cols = [col[0] for col in conn.description]
        return [
            dict(zip(cols, row))
            for row in conn.fetchall()
        ]
