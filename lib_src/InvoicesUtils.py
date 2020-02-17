from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from datetime import date
from partials.models import Partial
from suppliers.models import Supplier
from django.db.models import Q


class InvoicesUtils(object):
    '''Utilidades para trabajar con facturas para el modulo de audotoria'''

    def __init__(self):
        super().__init__()

    def get_unapproved_invoices(self):
        '''Facturas pendientes por aprobar'''
        return list(PaidInvoice.get_deny_by_audit())

    def get_approved_invoices(self):
        '''Facturas aprobadas'''
        return list(PaidInvoice.get_autorized_by_audit())
    
    def search(self, query):
        '''busca una factura en el sistema'''        
        invoices = PaidInvoice.objects.filter(
            Q(nro_factura__contains= query) 
            | Q(identificacion_proveedor__nombre__icontains = query)
            | Q(identificacion_proveedor__nombre__startswith = query)
            | Q(identificacion_proveedor__nombre__istartswith = query)
            )[:200]
        print(invoices.query)
        return list(invoices)
