from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from logs import loggin
from suppliers.models import Supplier

# /reportes/compras/<id_supplier/>
class PurcharsesProductSupplier(object):
    ''' Lista copleta de productos importados a un proveedor'''
    
    def __init__(self):
        loggin('i', 'Obteneniendo lista de productos comprados a un proveedor')
        self.id_supplier = None
        super().__init__()
    
    def get_purcharses(self,id_supplier):
        '''Obtiene la lista de compras para un proveedor'''
        self.id_supplier = id_supplier
        supplier = Supplier.get_by_ruc(id_supplier)
        
        if supplier is None:
            loggin('e', 'El proveedor no existe')
            return None
            
        invoices = self.get_invoices()

        data = {
            'supplier': supplier,
            'invoices' : [],
            'all_products' : [],
        }

        for invoice in invoices:
            details_invoice = self.get_products_detail(invoice.id_pedido_factura)
            data['invoices'].append({
                'invoice' : invoice, 
                'details' : details_invoice
                })
            data['all_products'].extend(details_invoice)
        
        data['resume'] = self.resume_products(data['all_products'])

        return data


    def get_products_detail(self, id_order_invoice):
        invoices = self.get_invoices()
        if invoices is None:
            loggin('i', 'las facturas no tiene producto registrado')
            return []
        invoice_details = OrderInvoiceDetail.get_by_id_order_invoice(
            id_order_invoice
            )

        return list(invoice_details)
    
    def get_invoices(self):
        ''' Obtiene las facturas del proveedor dentro del anio'''
        invoices = list(OrderInvoice.objects.filter(
            identificacion_proveedor = self.id_supplier
            ))        
        return invoices if invoices else []
    

    def resume_products(self, all_products):
        '''Crea una lista unica con los productos importados en el resumen '''
        return []