"""
Realiza la consulta de los productos los costos de compra cantidades 
y tipo de cambio, el reporte es por productos
"""

from products.models import Product
from django.db import connection


class ProductCostAnalysis():

    def __init__(self, cod_contable, deep=0):
        """Retorna el historico de costos de un pedido 

        Args:
            cod_contable (str): cod contable de producto
        """
        self.product = Product.get_by_cod_contable(cod_contable)
        self.deep = '' if deep == 0 else 'limit ' + str(deep)

    def get(self):
        if self.product is None:
            return None

        return {
            'product': self.product,
            'history': self.get_history()
        }

    def get_history(self):
        conn = connection.cursor()
        sql = '''
            SELECT * from v_costs_analysis where cod_contable = {}
            order by fecha_llegada_cliente desc {}
            '''.format(
            self.product.cod_contable,  self.deep
        )
        conn.execute(sql)
        cols = [col[0] for col in conn.description]
        return [
            dict(zip(cols, row))
            for row in conn.fetchall()
        ]
