from datetime import date

from django.db.models import Q

from orders.models import OrderInvoice
from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from partials.models import Partial
from suppliers.models import Supplier


class InvoicesUtils(object):
    '''Utilidades para trabajar con facturas para el modulo de audotoria'''

    def __init__(self):
        super().__init__()

    def get_unapproved_local_invoices(self):
        '''Facturas pendientes por aprobar'''
        return list(PaidInvoice.get_deny_by_audit())

    def get_unapproved_foreign_invoices(self):
        '''Facturas del esterior por aprobar'''        
        return list(OrderInvoice.get_deny_by_audit())
    
    def search_local(self, query):
        '''busca una factura en el sistema'''        
        invoices = PaidInvoice.objects.filter(
            Q(nro_factura__contains = query) 
            | Q(nro_factura__icontains = query) 
            | Q(identificacion_proveedor__nombre__icontains = query)
            | Q(identificacion_proveedor__nombre__startswith = query)
            | Q(identificacion_proveedor__nombre__istartswith = query)
            )[:100]
        return list(invoices)

    def search_foreign(self,query):
        '''Reotorna la lista de facturas del exterior'''
        return []
