from paids.models.Expense import Expense
from paids.models.PaidInvoice import PaidInvoice
from paids.models.PaidInvoiceDetail import PaidInvoiceDetail
from partials.models.Apportionment import Apportionment
from partials.models.ApportionmentDetail import ApportionmentDetail
from partials.models.InfoInvoice import InfoInvoice
from partials.models.InfoInvoiceDetail import InfoInvoiceDetail
from suppliers.models.Supplier import Supplier
from costings.models.Ledger import Ledger
from lib_src.serializers import (
                                ApportionmentSerializer,
                                ApportionmentDetailSerializer,
                                ExpenseSerializer,
                                InfoInvoiceSerializer,
                                InfoInvoiceDetailSerializer,
                                PaidInvoiceDetailSerializer,
                                PaidInvoiceSerializer,
                                PartialSerializer,
                                SupplierSerializer,
                                LedgerSerializer,
                                SupplierSerializer,
                            )

class CompleteParcialInfo(object):

    def __init__(self):
        self.status_parcial = {
            'parial' : True,
            'info_invoice' : True,
            'info_invoice_detail' : True,
            'apportioment' : True,
            'ledger' : True,
            'is_closed' : False,
        }
        self.request = None
        self.init_ledger = 0
        self.tributes = None
        self.total_expenses = 0
        self.total_invoiced = 0
        self.serialized = False
        self.partial = None
    

    def get_data(self, partial, serialized = False):        
        self.partial = partial
        self.serialized = serialized               
        return ({
            'partial': self.get_partial(),
            'info_invoice': self.get_info_invoice(),
            'expenses':self.get_expenses(),
            'ledger' : self.get_ledger(),
            'apportiomen' : self.get_apportioment(),
            'status' : self.status_parcial,
            })


    def get_partial(self):                
        if self.partial.bg_isclosed:
            self.is_closed = True

        if self.serialized:
            partia_serializer = PartialSerializer(self.partial)
            return partia_serializer.data
        
        return self.partial


    def get_info_invoice(self):      
        info_invoice = InfoInvoice.get_by_id_partial(self.partial.id_parcial)        
        partial_items = {
            'items' : 0,
            'boxes' : 0,
            'value' : 0,
            'bottles' : 0,
        }

        if info_invoice is None:
            self.status_parcial['info_invoice'] = False
            return None
        partial_items['total'] = info_invoice.total_value        
        info_invoice.supplier = Supplier.get_by_ruc(info_invoice.identificacion_proveedor_id)
        info_invoice.info_invoice_details= InfoInvoiceDetail.get_by_info_invoice(info_invoice)        

        if info_invoice.info_invoice_details is None:
            self.status_parcial['info_invoice_detail'] = False            
        else:
            for item in info_invoice.info_invoice_details:
                partial_items['boxes'] += item.nro_cajas                        


        if self.serialized:
            info_invoice_serializer = InfoInvoiceSerializer(info_invoice)
            supplier_serializer =SupplierSerializer(info_invoice.supplier)
            inf_invoice_detail_serializer = InfoInvoiceDetailSerializer(info_invoice.info_invoice_details, many=True)

            return {
                'info_invoice' : info_invoice_serializer.data,
                'info_invoice_details' : inf_invoice_detail_serializer.data,
                'info_invoice_details_sums' : partial_items,
                'supplier' : supplier_serializer.data,
                }         
        
        info_invoice.info_invoice_details_sums = partial_items
        return info_invoice


    def get_expenses(self):
        data_expenses = []
        expenses = Expense.get_by_parcial(self.partial)
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
    

    def get_apportioment(self):
        apportionment = Apportionment.get_by_parcial(self.partial)
        if apportionment is None:
            self.status_parcial['apportioment'] = False
            return None
        
        apportionment.apportionment_detail = ApportionmentDetail.get_by_apportionment(apportionment)

        if apportionment.apportionment_detail is None:
            self.status_parcial['apportioment'] = False

        if self.serialized:
            apportionment_serializer = ApportionmentSerializer(apportionment)
            apportionment_detail_serializer = ApportionmentDetailSerializer(apportionment.apportionment_detail, many=True)

            return {
                'apportioment': apportionment_serializer.data,
                'apportionment_detail' : apportionment_detail_serializer.data
            }
        
        return apportionment
    
    def get_ledger(self):
        partial_ledger = Ledger.get_by_parcial(self.partial)
        if partial_ledger is None:
            self.status_parcial['ledger'] = False
        
        if self.serialized:
            legder_serializer = LedgerSerializer(partial_ledger, many=True)
            return legder_serializer.data
        
        return partial_ledger