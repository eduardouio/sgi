from logs.app_log import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from partials.models import InfoInvoice, InfoInvoiceDetail, Partial
from suppliers.models import Supplier


class CompletePaidInvoice(object):
    """Retorna la informacion completa de una factura"""

    def __init__(self):
        self.invoice = {
            'invoice' : None,
            'details' : None
        }
    
    def get(self, id_invoice):
        """Retorna informacion completa de una factura
        
        Arguments:
            id_invoice {int} identificador de la factura

        Keyword Arguments:
            product_invoice {bool} -- Indica si la factura es de gastos (default: {False})
        """
        self.invoice['invoice'] = PaidInvoice.get_by_id(id_invoice)
        if self.invoice['invoice'] is None:
            loggin('i', 'La factura que busca no existe')
            return None
        
        self.invoice['details'] = PaidInvoiceDetail.get_by_paid_invoice(
            self.invoice['invoice'].id_documento_pago
        )
        
        return {
            'invoice' : self.invoice,
            'order' : self.get_order_data(self.invoice['details']),
            'parcial' : self.get_parcial_data(),
            'user' : self.get_userdata(),
        }
    
    def get_order_data(self, invoice_details):
        """Obtiene informacion basica de los pedidos"""
        pass

    def get_parcial_data(self):
        """Obtiene la informacion completa del parcual"""
        pass

    def get_user_data(self):
        """Obtiene la informacion del usuarios"""
        pass
