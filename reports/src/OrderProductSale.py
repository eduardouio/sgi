from orders.models import OrderInvoiceDetail, Order
from logs.app_log import loggin
from partials.models import Partial, InfoInvoiceDetail


class OrderProductSale():
    """Obtiene el saldo del producto de un pedido
    lo divide en cuatro partes
    pedido
    saldo_inicial
    nacionalizado
    saldo_actual
    Args:
        object (string): numero de pedido a consultar
    """

    def get(self, nro_order):
        loggin('i', 'consultando saldo pedido {}'.format(nro_order))
        self.nro_order = nro_order
        order = Order().get_by_order(nro_order)
        init_sale = self.get_init_sale(nro_order)
        if init_sale is None:
            loggin('i', 'El pedido {} no tiene productos o no existe'.format(
                nro_order
            ))
            return None

        nationalized = self.get_nationalized(order, init_sale)

        return {
            'order': order,
            'init_sale': init_sale,
            'nationalized': nationalized,
            'sale': self.get_sale(init_sale, nationalized),
        }

    def get_init_sale(self, nro_order):
        init_sale = []
        order_invoice_items = OrderInvoiceDetail().get_by_order(nro_order)
        if order_invoice_items is None:
            return None

        for line_item in order_invoice_items:
            init_sale.append({
                'detalle_pedido_factura': line_item.detalle_pedido_factura,
                'cajas': line_item.nro_cajas,
                'costo_caja': float(line_item.costo_caja),
            })
        return init_sale

    def get_nationalized(self, order, init_sale):
        if order.regimen == '10' and order.bg_isclosed:
            return init_sale

        nationalized = []
        for item in init_sale:
            nationalized.append({
                'detalle_pedido_factura': item['detalle_pedido_factura'],
                'cajas': 0,
                'costo_caja': item['costo_caja']
            })

        if order.regimen == '10' and not order.bg_isclose:    
            return nationalized

        partials = Partial().get_by_order(order.nro_pedido)
        if not partials:
            for item in init_sale:
                nationalized.append({
                    'cod_contable': item['cod_contable'],
                    'cajas': 0,
                    'costo_caja': item['costo_caja']
                })
            return nationalized

        for p in partials:
            if not p.bg_isclosed:
                return nationalized
            else:
                items = InfoInvoiceDetail().get_by_partial(p.id_parcial)
                for i in items:
                    # sumar a nacionalizaciones
                    pass
        return nationalized
        
    def get_sale(self, init_sale, nationalized):
        sale = init_sale
        for (idx, item) in enumerate(sale):
            for item_nat in nationalized:
                if item['detalle_pedido_factura'] == item_nat['detalle_pedido_factura']:
                    sale[idx]['cajas'] -= item_nat['cajas']

        return sale
