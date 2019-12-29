
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from partials.models import  InfoInvoiceDetail, Partial
from logs import loggin

class OrderProductSale(object):
    '''
        Retorna los saldos de un pedido, los productos que se encuentren en 
        un parcial no son tomados como saldo
    '''
    def __init__(self):
       self.nro_order = None
       self.order = None
       self.have_partials = False
       self.type_change_trim = 1
    
    def get(self, nro_order):
        """Obtiene un resumen de los saldos de los prodcutos"""

        self.nro_order = nro_order
        self.order = Order.get_by_order(self.nro_order)
        if self.order is None:
            loggin('i', 'No se puede retorar el saldo')
            return None
        order_invoice = OrderInvoice.get_by_order(self.nro_order)
        self.type_change_trim = order_invoice.tipo_cambio
        init_sale = self.get_init_sale()
        nationalized = []
        if init_sale:
            nationalized = self.get_nationalized()
            status_general = self.get_status_general(init_sale,nationalized)
            sums = {
                'fob_tct' : 0,
                'nacionalizado_tct' : 0,
                'saldo_tct' :0,
                'porcentaje' : 0,
            }

            for item in status_general:
                sums['fob_tct'] += item['fob_tct']
                sums['nacionalizado_tct'] += item['nacionalizado_tct']
            
            sums['saldo_tct'] = sums['fob_tct'] - sums['nacionalizado_tct']
            sums['porcentaje'] = sums['saldo_tct'] / sums['fob_tct']

            return {
                'initial_sale': init_sale,
                'nationalized': nationalized,
                'status_general': status_general,
                'type_change' : self.type_change_trim,
                'sums' : sums,
            }
        loggin('e', 'No se puede retornar saldo pedido {}'.format(nro_order))
        return None
    

    def get_init_sale(self):
        """Obtiene el saldo inicial del producto"""
        init_sale = OrderInvoiceDetail.get_by_order(self.nro_order)
        if init_sale:
            return init_sale
        return None
    

    def get_nationalized(self):
        """ Obtiene lo nacionalizado"""
        if self.order.regimen == 10:
            loggin('i', 'Retornando lo nacionalizado en R10')
            return self.get_init_sale()

        loggin('i', 'Retornando Producto nacionalizado en parciales')
        all_partials = Partial.get_by_order(self.nro_order)
        nationalized = []
        if all_partials:
            for p in all_partials:
                details = InfoInvoiceDetail.get_by_partial(p.id_parcial)
                if details:
                    nationalized.append(details)

        return nationalized
    
    def get_status_general(self, init_sale, nationalized):
        """Obtiene el resumen del saldo de un producto
        
        Arguments:
            init_sale {list} -- producto factura proveedor
            nationalizes {list} -- productos parciales
        """
        sale_status = []
        for item in init_sale:
            status = {
                'detalle_pedido_factura' : item.detalle_pedido_factura,
                'nro_cajas' : item.nro_cajas,
                'producto' : item.product,
                'cod_contable' : item.cod_contable_id,
                'nacionalizado' : 0,
                'nacionalizado_tct' : 0,
                'costo_caja' : item.costo_caja,
                'costo_caja_tct' : item.costo_caja * self.type_change_trim,
                'fob_tct' : item.costo_caja * self.type_change_trim * item.nro_cajas,
                }

            for p in nationalized:
                for nat in p:
                    if (nat.detalle_pedido_factura_id == status['detalle_pedido_factura']):
                        status['nacionalizado'] += nat.nro_cajas
                        status['nacionalizado_tct'] += (nat.nro_cajas * status['costo_caja_tct'])
            
            sale_status.append(status)

        return sale_status