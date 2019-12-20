from logs.app_log import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from paids.models import Expense, PaidInvoice, PaidInvoiceDetail
from partials.models import InfoInvoice, InfoInvoiceDetail, Partial
from suppliers.models import Supplier
from lib_src.sgi_utlils import run_query


class CompletePaidInvoice(object):
    """Retorna la informacion completa de una factura"""

    def __init__(self):
        self.jutified_value = 0


    def get(self, id_invoice):
        """Retorna informacion completa de una factura
        
        Arguments:
            id_invoice {int} identificador de la factura

        Keyword Arguments:
            product_invoice {bool} -- Indica si la factura es de gastos (default: {False})
        """
        loggin('i', 'Informacion completa de Pago')
        invoice = PaidInvoice.get_by_id(id_invoice)
        if invoice is None:
            loggin('i', 'La factura que busca no existe')
            return None
        return {
            'invoice' : invoice,
            'details' : self.get_details(invoice), 
            'user' : self.get_userdata(invoice.id_user),
            'invoiced_value' : invoice.valor,
            'justified_value' : self.jutified_value,
            'balance' : invoice.valor - self.jutified_value,
            'is_complete' : True if (invoice.valor - self.jutified_value == 0) else False,
        }


    def get_details(self, invoice):
        """informacion completa detalles factura
        
        Arguments:
            invoice {PaidInvoice} -- Factura
        """
        details = PaidInvoiceDetail.get_by_paid_invoice(
            invoice.id_documento_pago
            )
        loggin('i', 'Obteniendo detalle del pago')
        if details is None:
            return None
        my_details = []
        for item in details:
            expense = item.id_gastos_nacionalizacion
            self.jutified_value += item.valor
            my_details.append({
                'expense' : expense,
                'detail' : item,
                'order' : self.get_order_data(expense.nro_pedido),
                'partial' : self.get_partial_data(expense.id_parcial),
                'userdata' : self.get_userdata(expense.id_user)
            })
        loggin('i', 'Recuperando informacion de factura ')
        return my_details


    def get_order_data(self, nro_order):
        """Informacion completa del pedido"""
        order = Order.get_by_order(nro_order)
        if order is None:
            return None
        order_invoice = OrderInvoice.get_by_order(nro_order)
        return {
            'order' : order,
            'order_invoice' : order_invoice,
            'supplier' : order_invoice.identificacion_proveedor,
            'order_details' : OrderInvoiceDetail.get_by_id_order_invoice(order_invoice.id_pedido_factura)
        }


    def get_partial_data(self, id_partial):
        """Informacion completa del Parcial"""
        partial = Partial.get_by_id(id_partial)
        if partial is None:
            return None
        
        info_invoice = InfoInvoice.get_by_id_partial(partial.id_parcial)

        return {
            'partial' : partial,
            'order' : partial.nro_pedido,
            'info_invoice' : info_invoice,
            'info_invoice_details' : InfoInvoiceDetail.get_by_info_invoice(info_invoice.id_factura_informativa),
        }


    def get_userdata(self, id_user):
        """Informacion completa de usuario
        
        Arguments:
            invoice {PaidInvoice} -- Factura
        """
        results = run_query(
            'select * from usuario where id_user = {}'.format(id_user))
        
        if results:
            return results[0]
        
        loggin('e', 'No existe el usuario registrado')
        return None