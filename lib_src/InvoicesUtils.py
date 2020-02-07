import pdb

from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from partials.models import Partial
from suppliers.models import Supplier


class InvoicesUtils(object):
    '''Utilidades para trabajar con facturas'''

    def __init__(self):
        super().__init__()

    def get(self, *args, **kwargs):
        invoices = []
        if 'nro_invoice' in kwargs.keys():
            result = PaidInvoice.objects.filter(nro_factura = kwargs['nro_invoice'])
            invoices.extend([x for x in result])

        if 'nro_order' in kwargs.keys():
            init_expenses  = Expense.geta_all_by_order(kwargs['nro_order'])
            partial_expenses = []
        
        return invoices
    

    def get_open_invoices(self):
        '''Facturas con saldo pendiente'''
        pass


    def get_from_order(self, nro_order):
        ''' Obtiene todas las facturas de un pedido'''
        pass