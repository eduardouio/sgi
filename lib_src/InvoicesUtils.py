from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from datetime import date
from partials.models import Partial
from suppliers.models import Supplier


class InvoicesUtils(object):
    '''Utilidades para trabajar con facturas'''

    def __init__(self):
        super().__init__()

    def get_unapproved_invoices(self):
        '''Facturas pendientes por aprobar'''
        return list(PaidInvoice.get_deny_by_audit())

    def get_approved_invoices(self):
        '''Facturas aprobadas'''
        return list(PaidInvoice.get_autorized_by_audit())
