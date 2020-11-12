from orders.models import OrderInvoiceDetail, Order
from partials.models import InfoInvoice, InfoInvoiceDetail

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

        return {
            'init_sale': init_sale,
            'nationalized': nationalized,
            'sale': self.calculate_sale(init_sale, nationalized)
        }

    def get_init_sale(self, nro_order):                   
        # TODO validar que sume por producto, ya que hay pedidos con productos repetidos
        products = OrderInvoiceDetail().get_by_order(nro_order)
        if products is None:
            return None

        init_sale = []
        for p in products:
            init_sale.append({
                'cod_contable': p.cod_contable,
                'nro_cajas': p.nro_cajas,
                'costo_caja': p.costo_caja
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
        info_invoices = InfoInvoice().get_by_order(order.nro_pedido)

        for inv in info_invoices:
            nationalized.append(
                InfoInvoiceDetail().get_by_info_invoice(
                    inv.id_factura_informativa
                ))

        import ipdb; ipdb.set_trace()               
        # TODO terminar de recolectar los productos nacionalizados
        # solo quremos el saldo del produco, nada mas
        return nationalized
        

    def calculate_sale(self, init_sale, nationalized):
        return []
        sale = []
        for item in init_sale:
            sale.append({
                'cod_contable': item['cod_contable'],
                'nro_cajas': item['nro_cajas'],
                'costo_caja': item['costo_caja']
            })

        for item in sale:
            for nat in nationalized:
                if item['cod_contable'] == nat['cod_contable']:
                    item['nro_cajas'] -= nat['nro_cajas']

        return sale
