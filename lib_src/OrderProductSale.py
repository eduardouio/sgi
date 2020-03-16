
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from partials.models import  InfoInvoiceDetail, Partial
from logs import loggin


class OrderProductSale(object):
    '''
        Retorna los saldos de un pedido, los productos que se encuentren en
        un parcial no son tomados como saldo
    '''
    def __init__(self, nro_order):
        self.nro_order = nro_order
        self.have_partials = False
        self.type_change_trim = 1
        self.order = Order.get_by_order(self.nro_order)       
        if self.order is None:
            loggin('i', 'No se puede retorar el saldo')
            return None
        self.order_invoice = OrderInvoice.get_by_order(self.nro_order)
        self.type_change_trim = self.order_invoice.tipo_cambio

    def get_sale(self):
        """Obtiene un resumen de los saldos de los prodcutos"""
        init_sale = self.get_init_sale()
        if init_sale is None:
            loggin('e', 'No se puede retornar saldo {}'.format(self.nro_order))
            return None
        nationalized = self.get_nationalized()
        items = []
        sums = {
            'cajas': 0,
            'tct': self.type_change_trim,
            'fob_tct_nacionalizado': 0,
            'fob_tct_inicial': 0,
            'nacionalizado': 0,
        }
        for item in init_sale:
            sums['cajas'] += item['cajas']
            sums['fob_tct_inicial'] += item['costo_caja'] * item['cajas']
            item['nacionalizado'] = 0
            items.append(item)
        for item in items:
            for item_nat in nationalized:
                if (item['detalle_pedido_factura']
                    == item_nat['detalle_pedido_factura']):
                    sums['fob_tct_nacionalizado'] += (
                        item_nat['costo_caja'] * item_nat['cajas']
                        )
                    item['nacionalizado'] += item_nat['cajas']
                    sums['nacionalizado'] += item_nat['cajas']
        sums['fob_tct_saldo'] = (
            sums['fob_tct_inicial'] - sums['fob_tct_nacionalizado']
            )
        return {
            'items': items,
            'sums': sums,
        }

    def get_init_sale(self):
        """Obtiene el saldo inicial del producto"""
        init_sale = OrderInvoiceDetail.get_by_order(self.nro_order)
        if init_sale is None:
            return None

        init_sale_product = []
        for item in init_sale:
            init_sale_product.append({
                'detalle_pedido_factura': item.detalle_pedido_factura,
                'nombre': item.product,
                'cajas': item.nro_cajas,
                'costo_caja': item.costo_caja * self.type_change_trim,
            })
        return init_sale_product

    def get_nationalized(self):
        """ Obtiene lo nacionalizado"""
        if self.order.regimen == 10:
            loggin('i', 'Retornando lo nacionalizado en R10')
            return self.get_init_sale()
        all_partials = Partial.get_by_order(self.nro_order)
        nationalized = []
        id_items = []

        if all_partials:
            for p in all_partials:
                if bool(p.bg_isclosed) == True:
                    details = InfoInvoiceDetail.get_by_partial(p.id_parcial)
                    if details:
                        for det in details:
                            nationalized.append({
                            'detalle_pedido_factura': det.detalle_pedido_factura_id,
                            'nombre': det.detalle_pedido_factura.product,
                            'cajas': det.nro_cajas,
                            'costo_caja': det.costo_caja * self.type_change_trim
                            })
                            id_items.append(det.detalle_pedido_factura_id)
        id_items = list(set(id_items))
        items_nationalized = []

        for id_item in id_items:
            items_nationalized.append({
                'detalle_pedido_factura': id_item,
                'nombre': None,
                'cajas': 0,
                'costo_caja': 0,
                'fob_tct': 0,
            })

        for item in items_nationalized:
            for idx in nationalized:
                if item['detalle_pedido_factura'] == idx['detalle_pedido_factura']:
                    item['cajas'] += idx['cajas']
                    item['nombre'] = idx['nombre']
                    item['costo_caja'] = idx['costo_caja'] * self.type_change_trim
                    item['fob_tct'] += idx['costo_caja'] 

        return items_nationalized
