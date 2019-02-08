from lib_src.serializers import (ExpenseSerializer,
                                 PaidInvoiceDetailSerializer,
                                 PaidInvoiceSerializer, SupplierSerializer)
from logs import loggin
from orders.models import Order
from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from partials.models import Partial
from suppliers.models import Supplier


class CompletePaidinfo(object):
    '''  Return all information from paid 
        -> {
            supplier : [],
            invoice : [],
            invoice_detail : [
                order: {},
                partial : {},
                detail : {
                    expese : {},
                    detail : {},
                },
            ]
        }
    '''

    def __init__(self, id_invoice):
        self.id_invoice = id_invoice
        self.invoice_value = 0
        self.cross_value = 0
        self.invoice = None
        self.serialized = False


    def get_data(self, serialized = False):
        self.serialized = serialized       
        self.invoice = PaidInvoice.get_by_id(self.id_invoice)

        if self.invoice is None:
            loggin('i', 'Recuperacion de factura de pago completa no se realizo')
            return {}

        return {
            'supplier' : self.get_supplier(),
            'invoice'  : self.get_invoice(),
            'details'  : self.get_detail(),
            'value' : self.invoice_value,
            'cross_value' : self.cross_value,
            'sale' : (self.invoice_value - self.cross_value)
        }
    

    def get_supplier(self):
        supplier = self.invoice.identificacion_proveedor
        if self.serialized:
            supplier_serializer = SupplierSerializer(supplier)
            return supplier_serializer.data
        
        return supplier


    def get_invoice(self):
        self.invoice_value = self.invoice.valor
        if self.serialized:
            paids_serializer = PaidInvoiceSerializer(self.invoice)
            return paids_serializer.data
        
        return self.invoice


    def get_detail(self):
        details = PaidInvoiceDetail.get_by_paid_invoice(self.id_invoice)
        if details is None:
            return []
        
        data = []
        self.cross_value = 0
        for item in details:            
            self.cross_value += item.valor
            data.append({
                'expense' : Expense.get_by_id_expense(item.id_gastos_nacionalizacion_id),
                'detail' : item
            })

        if self.serialized:
            serialized = []
            for item in data:
                expense_serializer = ExpenseSerializer(item['expense'])
                paids_invoice_det_serializer = PaidInvoiceDetailSerializer(item['detail'])
                serialized.append({
                    'expense' : expense_serializer.data,
                    'detail' : paids_invoice_det_serializer.data
                })

            return serialized
        
        return data
    
    def test(self):
        return self.id_invoice
