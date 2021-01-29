import calendar

from logs.app_log import loggin
from orders.models import Order, OrderInvoiceDetail
from partials.models import InfoInvoiceDetail, Partial


class ReportICE(object):

    def __init__(self, year, month):
        """Obtencion de datos del reporte ICE

    Arguments:
        year {string} -- Anio del reporte
        mounth {string} -- Mes del Reporte
    """
        limits = calendar.monthrange(year, month)
        self.year = str(year)
        self.month = str(month) if month > 9 else '0{}'.format(str(month))
        self.day_e = str(limits[1]) if limits[1] > 9 else '0{}'.format(
            str(limits[1]))

    def get(self):
        return {
            'almacenera': self.get_almacenera(),
            'consumo': self.get_consumo(),
            'parciales': self.get_partials(),
        }

    def get_almacenera(self):
        """lista de productos llegados a Almagro"""
        raw_query = ('SELECT * from pedido where fecha_ingreso_almacenera'
                     ' BETWEEN "{year}-{month}-{day_b}" AND "{year}-{month}-{day_e}"'
                     ' order by fecha_ingreso_almacenera'.
                     format(year=str(self.year), month=str(self.month),
                            day_b='01', day_e=self.day_e
                            ))

        return self.get_orders_items(raw_query)

    def get_consumo(self, query=False):
        """ Lista de productos de consumo llegados a bodega """
        raw_query = ('SELECT * from pedido where fecha_llegada_cliente'
                     ' BETWEEN "{year}-{month}-{day_b}" AND "{year}-{month}-{day_e}"'
                     ' order by fecha_llegada_cliente'.
                     format(year=str(self.year), month=str(self.month),
                            day_b='01', day_e=self.day_e
                            ))
        if query:
            return raw_query
        else:
            return self.get_orders_items(raw_query)

    def get_partials(self, query=False):
        '''Productos de parciales llegados a bodega'''
        partials = []
        details = []
        products_arrived = []
        raw_query = ('SELECT * from parcial where fecha_llegada_cliente'
                     ' BETWEEN "{year}-{month}-{day_b}" AND "{year}-{month}-{day_e}"'
                     ' order by fecha_llegada_cliente'.
                     format(year=str(self.year), month=str(self.month),
                            day_b='01', day_e=self.day_e
                            ))
        for p in Partial.objects.raw(raw_query):
            partials.append(p)

        if partials.__len__() == 0:
            loggin('i', 'Listado de parciales vacio, retorna []')
            return []

        for p in partials:
            details = InfoInvoiceDetail().get_by_partial(p.id_parcial)
            details = [] if details is None else list(details)
            for det in details:
                products_arrived.append(det)

        if query:
            return raw_query
        else:
            return products_arrived

    def get_orders_items(self, raw_query):
        """Funcion auxiliar. obtiene los productos de un pedido"""
        orders = []
        details = []
        products_arrived = []
        for o in Order.objects.raw(raw_query):
            orders.append(o)

        if orders.__len__() == 0:
            loggin(
                'e', 'No tiene registros retornamos lista vacia {}'.format(raw_query))
            return []

        for o in orders:
            details = list(OrderInvoiceDetail().get_by_order(o.nro_pedido))
            details = [] if details is None else details
            for det in details:
                products_arrived.append(det)

        return products_arrived
