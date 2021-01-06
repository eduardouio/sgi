from calendar import monthrange
from datetime import date

from logs import loggin
from orders.models import Order, OrderInvoiceDetail
from partials.models import InfoInvoiceDetail, Partial


class LocalWarenhouseArrivals(object):
    ''' Listado de pedidos llegados a la bodega local'''

    def __init__(self, year, month):
        ''' Parametros de rago de obtencion de pedidos, si el mes es cero
            se consultan todos los del anio, sino se especifica la fecha
            del mes completo
            (int)year : Anio del reporte
            (int)month : mes del reporte
        '''
        if month == 0:
            self.date_start = date(year, 1, 1)
            self.date_end = date(year, 12, 31)
        else:
            mont_range = monthrange(year, month)
            self.date_start = date(year, month, 1)
            self.date_end = date(year, month, mont_range[1])
        loggin('i', 'Accediento a reporte de llegadas a Alamgro')

    def get(self):
        '''retorna reporte completo de llegadas a las bodegas'''
        report = []
        for item in self.get_orders():
            report.append({
                'id': item.detalle_pedido_factura,
                'idf': item.id_pedido_factura_id, 
                'nro_pedido': item.id_pedido_factura.nro_pedido,
                'id_parcial': 0,
                'proveedor': item.id_pedido_factura.identificacion_proveedor,
                'nro_refrendo': item.id_pedido_factura.nro_pedido.nro_refrendo,
                #'cod_contable': item.cod_contable_id,
                'producto': item.cod_contable.nombre,
                #'cod_ice': item.cod_contable.cod_ice,
                'capacidad_ml': int(item.capacidad_ml),
                #'grado_al': item.grado_alcoholico,
                'nro_cajas': item.nro_cajas,
                'unidades': item.nro_cajas * item.cod_contable.cantidad_x_caja,
                #'ex_aduana': item.ex_aduana_unitario,
                #'costo': item.costo_caja_final / item.cod_contable.cantidad_x_caja,
                #'costo_total' : item.costo_total,
                'llegada': item.id_pedido_factura.nro_pedido.fecha_llegada_cliente,
            })

        for item in self.get_partials():
            report.append({
                'id': item.id_factura_informativa_detalle,
                'idf': item.id_factura_informativa_id,
                'nro_pedido': item.id_factura_informativa.id_parcial.nro_pedido,
                'id_parcial': item.id_factura_informativa.id_parcial_id,
                'proveedor': item.detalle_pedido_factura.id_pedido_factura.identificacion_proveedor,
                'nro_refrendo': item.id_factura_informativa.nro_refrendo,
                #'cod_contable': item.detalle_pedido_factura.cod_contable.cod_contable,
                'producto': item.product,
                #'cod_ice': item.detalle_pedido_factura.cod_contable.cod_ice,
                'capacidad_ml': int(item.capacidad_ml),
                #'grado_al': round(float(item.grado_alcoholico),2),
                'nro_cajas': int(item.nro_cajas),
                'unidades': int(item.unidades),
                #'ex_aduana_unitario': item.ex_aduana_unitario,
                #'costo': item.costo_caja_final / item.detalle_pedido_factura.cod_contable.cantidad_x_caja,
                #'costo_total' : item.costo_total,
                'llegada': item.id_factura_informativa.id_parcial.fecha_llegada_cliente,
            })

        return report

    def get_orders(self):
        ''' lista de pedidos R10 llegados a las bodeDesarrolladogas '''
        orders_arrivals = Order.objects.filter(
            regimen='10',
            fecha_llegada_cliente__range=(self.date_start, self.date_end)
        ).order_by('fecha_llegada_cliente')
        products = []
        for order in orders_arrivals:
            details = OrderInvoiceDetail.get_by_order(order.nro_pedido)
            if not isinstance(details, list):
                products.extend(list(details))

        return products

    def get_partials(self):
        ''' Lista de parciales llegados a las bodegas '''
        partial_arrivals = Partial.objects.filter(
            fecha_llegada_cliente__range=(self.date_start, self.date_end)
        ).order_by('fecha_llegada_cliente')
        products = []
        for partial in partial_arrivals:
            details = InfoInvoiceDetail.get_by_partial(partial.id_parcial)
            if details:
                products.extend(list(details))

        return products
