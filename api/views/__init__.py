from api.views.AllOrders import AllOrders
from api.views.Apportionment import (ApportionmenCreateView,
                                     ApportionmenDeleteView,
                                     ApportionmenDetailView,
                                     ApportionmenUpdateView)
from api.views.ApportionmentDetail import (ApportionmentDetailCreateView,
                                           ApportionmentDetailDeleteView,
                                           ApportionmentDetailDetailView,
                                           ApportionmentDetailUpdateView)
from api.views.Expense import (ExpenseCreateView, ExpenseDeleteView,
                               ExpenseDetailView, ExpenseUpdateView)
from api.views.InfoInvoice import (InfoInvoiceCreateView,
                                   InfoInvoiceDeleteView,
                                   InfoInvoiceDetailView,
                                   InfoInvoiceUpdateView)
from api.views.InfoInvoiceDetail import (InfoInvoiceDetailCreateView,
                                         InfoInvoiceDetailDeleteView,
                                         InfoInvoiceDetailDetailView,
                                         InfoInvoiceDetailUpdateView)
from api.views.Ledger import (LedgerCreateView, LedgerDeleteView,
                              LedgerExisting, LedgerDetailView,
                              LedgerUpdateView)
from api.views.Order import (GetCompleteOrderInfoAPIView, OrderCreateView,
                             OrderDeleteView, OrderDetailView, OrderUpdateView, OrderCloseView)
from api.views.OrderInvoice import (OrderInvoiceCreateView,
                                    OrderInvoiceDeleteView,
                                    OrderInvoiceDetailView,
                                    OrderInvoiceUpdateView)
from api.views.OrderInvoiceDetail import (OrderInvoiceDetailCreateView,
                                          OrderInvoiceDetailDeleteView,
                                          OrderInvoiceDetailDetailView,
                                          OrderInvoiceDetailUpdateView)
from api.views.PaidInvoice import (CompletePaidView, PaidInvoiceCreateView,
                                   PaidInvoiceDeleteView,
                                   PaidInvoiceDetailView,
                                   PaidInvoiceUpdateView)
from api.views.PaidInvoiceDetail import (PaidInvoiceDetailCreateView,
                                         PaidInvoiceDetailDeleteView,
                                         PaidInvoiceDetailDetailView,
                                         PaidInvoiceDetailUpdateView)
from api.views.Partial import (CompletePartialInfoApiView, PartialCreateView,
                               PartialDeleteView, PartialDetailView,
                               PartialUpdateView)
from api.views.Product import (ProductCreateView, ProductDeleteView,
                               ProductDetailView, ProductUpdateView)
from api.views.Suppliers import (SupplierCreateView, SupplierDeleteView,
                                 SupplierDetailView, SupplierUpdateView)
from api.views.Label import (LabelCreateView, LabelDeleteView,
                             LabelDetailView, LabelUpdateView,
                             LabelsFromDetallePedidoFactura,
                             LabesValidRange, LabesValidateBatch, LabelsValidateLabel)
