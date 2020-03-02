# Completando la informacion del anexo del ICE
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from partials.models import Partial, InfoInvoice, InfoInvoiceDetail


class AnexoICE(Object):
    ''' Reporte mensual del ICE detallado en unidades'''

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_report(self):
        pass

    def get_almagro(self):
        pass

    def get_consumo(self):
        pass
