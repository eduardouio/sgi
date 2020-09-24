from orders.models import OrderInvoiceDetail, Order
from products.models import Product
from partials.models import Partial, InfoInvoice, InfoInvoiceDetail


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
        self.nro_order = nro_order
        order = Order().get_by_order(nro_order)
        init_sale = self.get_init_sale(nro_order)
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
                'cod_contable': line_item.cod_contable,
                'cajas': line_item.nro_cajas,
                'costo_caja': float(line_item.costo_caja),
            })
        return init_sale

    def get_nationalized(self, order, init_sale):
        nationalized = []
        if order.regimen == '10' and not order.bg_isclose:
            for item in init_sale:
                nationalized.append({
                    'cod_contable': item.cod_contable,
                    'cajas': 0,
                    'costo_caja': item.costo_caja
                })
            return nationalized

        if order.regimen == '10' and order.bg_isclosed:
            return init_sale

        partials = Partial().get_by_order(order.nro_pedido)
        if not partials:
            for item in init_sale:
                nationalized.append({
                    'cod_contable': item.cod_contable,
                    'cajas': 0,
                    'costo_caja': item.costo_caja
                })
            return nationalized
        
        for p in partials:
            

        #import ipdb; ipdb.set_trace()

        raise('No s retorna nada')

    def get_sale(self, init_sale, nationalized):
        sale = init_sale
        for item in sale:
            for item_nat in nationalized:
                if item['cod_contable'] == item_nat['cod_contable']:
                    sale[item]['nro_cajas'] -= item_nat['nro_cajas'] 

        return sale
