from orders.models import OrderInvoiceDetail, Order
from partials.models import InfoInvoiceDetail, Partial

from logs.app_log import loggin


class OrderDetailProductSale():
    """Obtiene el saldo en detalle de un pedido metodo get()"""

    def get(self, nro_order, ignore_liquidated=False):
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
            ignore_liquidated {bool} -- no se concideran parciales sin 
                                        con liqudiacion y sin cerrar
        """
        loggin('w', 'Iniciando verificacion de saldos {} pedido {}'.format(
            __name__, nro_order
        ))
        order = Order().get_by_order(nro_order)
        if order is None:
            loggin('w', 'No es posible obtener el saldo del pedido {}'.format(
                nro_order)
                )
            return None

        init_sale = self.get_init_sale(nro_order)

        if not init_sale:
            loggin('e', 'Pedido sin saldo inicial {}'.format(nro_order))
            return ({'init_sale': [], 'nationalized': [], 'sale': []})

        nationalized = self.get_nationalized(order, ignore_liquidated)

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

    def get_nationalized(self, order, ignore_liquidated):
        """busca los productos que han sido nacionalizados, la referencia
        es que el pedido o parcial tenga la liquidacion de aduana ingresada

        Arguments:
            order {Order} -- Pedido

        Returns:
            {array} -- Listado de items nacionalizados
            ||
            {boolean} -- si es verdadero solo toma en cuenta los productos de 
                        los parciales cerrados, sino toma en cunenta los 
                        productos de los parciales con liquidacion de aduana 
                        ingresada
        """
        if order.regimen == '10':
            init_sale = self.get_init_sale(order.nro_pedido) 
            if not ignore_liquidated and order.bg_isliquidated:
                detail = []
                for item in init_sale:
                    detail.append({
                        'detalle_pedido_factura': item['detalle_pedido_factura'],
                        'cod_contable': item['cod_contable'],
                        'nro_cajas': 0,
                        'costo_caja': item['costo_caja'],
                    })
            else:
                return init_sale

        nationalized = []
        partials = Partial().get_by_order(order.nro_pedido)
        for p in partials:
            if not ignore_liquidated:
                if p.bg_isclosed:
                    nationalized += list(InfoInvoiceDetail().get_by_partial(p.id_parcial))
            else:
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
                'product': OrderInvoiceDetail.get_by_id(itm['detalle_pedido_factura'])
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
