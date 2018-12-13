from orders.models.Order import Order
from orders.models.OrderInvoice import OrderInvoice
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from paids.models.Expense import Expense
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail
from suppliers.models.Supplier import Supplier
from partials.models.Partial import Partial
from costings.models.Ledger import Ledger
from lib_src.serializers import OrderSerializer
from lib_src.serializers import OrderInvoiceSerializer
from lib_src.serializers import OrderInvoiceDetailSerializer
from lib_src.serializers import ExpenseSerializer
from lib_src.serializers import PaidInvoiceSerializer
from lib_src.serializers import PaidInvoiceDetailSerializer
from lib_src.serializers import SupplierSerializer
from lib_src.serializers import PartialSerializer
from lib_src.serializers import LedgerSerializer
from logs.app_log import loggin
from lib_src.CompleteParcialInfo import CompleteParcialInfo

class CompleteOrderInfo(object):
    '''Returns all info of de order'''

    def __init__(self):
        self.status_order = {
            'order' : True,
            'order_invoice' : True,
            'order_invoice_details' : True,
            'ledger' : True,
        }

        self.serialized = False
        self.nro_order = None
   

    def get_data(self, nro_order, serialized = False):        
        self.nro_order = nro_order
        self.serialized = serialized

        return ({
            'order': self.get_order(),
            'order_invoice':self.get_order_invoice(),
            'parcials':self.get_parcials(),
            'expenses':self.get_expenses(),
            'ledger' : self.get_ledger(),
            'status' : self.status_order,
            })

    
    def get_order(self):
        order = Order.get_by_order(nro_order=self.nro_order)
        
        if order is None:
            self.status_order['order'] = False
            return None
        
        if self.serialized:
            order_serializer = OrderSerializer(order)
            return order_serializer.data
        
        return order


    def get_order_invoice(self):
        order_items = {
            'order_invoice' : None,
            'supplier' : None,
            'order_invoice_detail' : None
        }

        order_invoice = OrderInvoice.get_by_order(self.nro_order)
        if order_invoice is None:
            self.status_order['order_invoice'] = False
            return None
        
        order_items['order_invoice'] = order_invoice
        order_items['order_invoice_details'] = OrderInvoiceDetail.get_by_id_order_invoice(order_invoice.id_pedido_factura)
        order_items['supplier'] = Supplier.get_by_ruc(order_invoice.identificacion_proveedor)

        if order_items['order_invoice_details'] is None:
            self.status_order['order_invoice_details'] = False        

        if self.serialized:
            order_invoice_serializer = OrderInvoiceSerializer(order_items['order_invoice'])
            order_invoice_det_serializer = OrderInvoiceDetailSerializer(order_items['order_invoice_details'],many=True)
            supplier_serializer = SupplierSerializer(order_items['supplier'])

            return {
                'order_invoice' : order_invoice_serializer.data,
                'supplier' : supplier_serializer.data,
                'order_invoice_detail' : order_invoice_det_serializer.data
            }

        return order_items


    def get_parcials(self):
        parcials = Partial.get_by_order(self.nro_order)
        parcials_data = []
        if parcials is None:
            return None
        
        for p in parcials:
            parcials_data.append(
                CompleteParcialInfo().get_data(p, self.serialized)
                )

        return parcials_data


    def get_expenses(self):
        data_expenses = []       
        expenses = Expense.get_by_order(self.nro_order)

        if expenses is None:
            return None

        for item in expenses:
            paids = []                
            item.paids = PaidInvoiceDetail.get_by_expense(item)
            item.invoiced_value = 0
            item.ledger = 0            

            for paid in item.paids:
                item.invoiced_value += paid.valor
                paid.invoice = PaidInvoice.get_by_id(paid.id_documento_pago_id)
                paid.supplier = Supplier.get_by_ruc(paid.invoice.identificacion_proveedor_id)

                paids.append(
                    {
                        'paid' : paid,
                        'invoice' : paid.invoice,
                        'supplier': paid.supplier,
                    }
                )

                if paid.bg_mayor == 1:
                    item.ledger += paid.valor

            item.sale = (item.valor_provisionado - item.invoiced_value)            

            if self.serialized:
                expense_serializer = ExpenseSerializer(item)                    
                paids_serialized = []

                for p in paids:
                    paid_serializer = PaidInvoiceDetailSerializer(p['paid'])
                    invoice_serializer = PaidInvoiceSerializer(p['invoice'])
                    supplier_serializer = SupplierSerializer(p['supplier'])
                    paids_serialized.append(
                        {
                        'paid' : paid_serializer.data,
                        'invoice' : invoice_serializer.data,
                        'supplier': supplier_serializer.data,
                        }
                    )

                data_expenses.append({
                    'expense' : expense_serializer.data,
                    'paids' : paids_serialized,
                    'invoiced_value' : item.invoiced_value,
                    'sale' : item.sale,
                    'legder' : item.ledger,
                })
        
        if self.serialized:
            return data_expenses

        return expenses
    
    def get_ledger(self):
        order = Order.get_by_order(self.nro_order)
        ledger_order = Ledger.get_by_order(order)
        if ledger_order is None and order.regimen == '10':
            self.status_order['ledger'] = False
            return None
        
        if self.serialized:
            ledger_serializer = LedgerSerializer(ledger_order, many=True)
            return ledger_serializer.data
        
        return ledger_order
            