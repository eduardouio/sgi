from orders.models import OrderInvoiceDetail, Order
from partials.models import InfoInvoiceDetail, Partial

from logs.app_log import loggin


class OrderDetailProductSale():
    """Obtiene el saldo en detalle de un pedido metodo get()"""
    def get(self, nro_order, ignore_liquidated=False):
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
        sale = self.calculate_sale(init_sale, nationalized)

        sale_boxes = sum([s['nro_cajas'] for s in sale])
        if not sale_boxes:
            order.bg_closed = 1
            order.save()
        data = {
            'init_sale': init_sale,
            'nationalized': nationalized,
            'sale': sale
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
