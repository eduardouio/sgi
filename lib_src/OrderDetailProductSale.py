from orders.models import OrderInvoiceDetail, Order
from partials.models import InfoInvoice, InfoInvoiceDetail, Partial

from logs.app_log import loggin


class OrderDetailProductSale():
    """Obtiene el saldo en detalle de un pedido metodo get()"""

    def get(self, nro_order):
        """Obtiene el detalle de productos del pedido
        el detalle contiene saldo y nacionalizaciones

        return   {
            init_sale = {
                {cod_contable, nro_cajas, costo_caja, tipo_cambio},
            },
            nationalized = {
                {cod_contable, nro_cajas, costo_caja, tipo_cambio},
            },
            sale = {
                {cod_contable, nro_cajas, costo_caja, tipo_cambio},
            }

        }

        Arguments:
            nro_order {str} -- nro de pedido a consultar
        """
        loggin('w', 'Iniciando verificacion de saldos {}'.format(__name__))
        order = Order().get_by_order(nro_order)
        if order is None:
            loggin('w', 'No es posible obtener el saldo del pedido {}'.format(
                nro_order)
                )
            return None

        init_sale = self.get_init_sale(nro_order)
        nationalized = self.get_nationalized(order)

        data = {
            'init_sale': init_sale,
            'nationalized': nationalized,
            'sale': self.calculate_sale(init_sale, nationalized)
        }
        return data

    def get_init_sale(self, nro_order):
        products = OrderInvoiceDetail().get_by_order(nro_order)
        if products is None:
            return None

        init_sale = []
        for p in products:
            init_sale.append({
                'detalle_pedido_factura': p.detalle_pedido_factura,
                'cod_contable': p.cod_contable_id,
                'nro_cajas': int(p.nro_cajas),
                'costo_caja': float(p.costo_caja)
            })

        return init_sale

    def get_nationalized(self, order):
        """busca los productos que han sido nacionalizados, la referencia
        es que el pedido o parcial tenga la liquidacion de aduana ingresada

        Arguments:
            order {Order} -- Pedido

        Returns:
            {array} -- Listado de items nacionalizados
            ||
            {boolean} -- Retorna verdadero si todo esta nacionalizado
        """
        if order.bg_isliquidated and order.regimen == '10':
            loggin('i', 'Retornamos el saldo inial del pedido')
            return self.get_init_sale(order.nro_pedido)

        nationalized = []
        partials = Partial().get_by_order(order.nro_pedido)
        for p in partials:
            if p.bg_isliquidated:
                nationalized += list(InfoInvoiceDetail().get_by_partial(p.id_parcial))

        all_products = [{
                'detalle_pedido_factura': item.detalle_pedido_factura_id,
                'cod_contable': item.detalle_pedido_factura.cod_contable_id,
                'nro_cajas': int(item.nro_cajas),
                'costo_caja': float(item.costo_caja)
            } for item in nationalized]

        return self.unify_items(all_products)

    def calculate_sale(self, init_sale, nationalized):
        sale = []
        for itm in init_sale:
            sale.append({
                'detalle_pedido_factura': itm['detalle_pedido_factura'],
                'cod_contable': itm['cod_contable'],
                'nro_cajas': itm['nro_cajas'],
                'costo_caja': itm['costo_caja'],
            })
        for item in sale:
            for nat in nationalized:
                if item['detalle_pedido_factura'] == nat['detalle_pedido_factura']:
                    item['nro_cajas'] -= nat['nro_cajas']
        return sale

    def unify_items(self, products):
        """group items for detalle_pedido_factura and sum boxes value

        Args:
            products (list): list of dict products
        """
        index = set([itm['detalle_pedido_factura'] for itm in products])
        result = []
        for idx in index:
            product = {
                'detalle_pedido_factura': idx,
                'cod_contable': '',
                'nro_cajas': 0,
                'costo_caja': 0.0
            }
            for item in products:
                if idx == item['detalle_pedido_factura']:
                    product['cod_contable'] = item['cod_contable']
                    product['costo_caja'] = item['costo_caja']
                    product['nro_cajas'] += item['nro_cajas']

            result.append(product)

        return result
