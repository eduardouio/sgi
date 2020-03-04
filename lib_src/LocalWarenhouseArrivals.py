from datetime import date
from calendar import monthrange

from logs import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from partials.models import InfoInvoice, InfoInvoiceDetail, Partial


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

    def get(self):
        '''retorna reporte completo de llegadas a las bodegas'''
        return True

    def get_orders(self):
        ''' lista de pedidos R10 llegados a las bodeDesarrolladogas '''
        pass

    def get_partials(self):
        ''' Lista de parciales llegados a las bodegas '''
        pass
