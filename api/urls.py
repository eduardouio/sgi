from django.urls import include, path
from api.views import (ApportionmenCreateView, ApportionmenDeleteView,
                       ApportionmenDetailView, ApportionmentDetailCreateView,
                       ApportionmentDetailDeleteView,
                       ApportionmentDetailDetailView,
                       ApportionmentDetailUpdateView, ApportionmenUpdateView,
                       CompletePaidView, CompletePartialInfoApiView,
                       ExpenseCreateView, ExpenseDeleteView, ExpenseDetailView,
                       ExpenseUpdateView, GetCompleteOrderInfoAPIView,
                       InfoInvoiceCreateView, InfoInvoiceDeleteView,
                       InfoInvoiceDetailCreateView,
                       InfoInvoiceDetailDeleteView,
                       InfoInvoiceDetailDetailView,
                       InfoInvoiceDetailUpdateView, InfoInvoiceDetailView,
                       InfoInvoiceUpdateView, LedgerCreateView,
                       LedgerDeleteView, LedgerDetailView, LedgerUpdateView,
                       OrderCreateView, OrderDeleteView, OrderDetailView,
                       OrderInvoiceCreateView, OrderInvoiceDeleteView,
                       OrderInvoiceDetailCreateView,
                       OrderInvoiceDetailDeleteView,
                       OrderInvoiceDetailDetailView,
                       OrderInvoiceDetailUpdateView, OrderInvoiceDetailView,
                       OrderInvoiceUpdateView, OrderUpdateView,
                       PaidInvoiceCreateView, PaidInvoiceDeleteView,
                       PaidInvoiceDetailCreateView,
                       PaidInvoiceDetailDeleteView,
                       PaidInvoiceDetailDetailView,
                       PaidInvoiceDetailUpdateView, PaidInvoiceDetailView,
                       PaidInvoiceUpdateView, PartialCreateView,
                       PartialDeleteView, PartialDetailView, PartialUpdateView,
                       ProductCreateView, ProductDeleteView, ProductDetailView,
                       ProductUpdateView, SupplierCreateView,
                       SupplierDeleteView, SupplierDetailView,
                       SupplierUpdateView, AllOrders,)

app_name = 'api'

urlpatterns = [
    #Appotionment
    path('appotionment/create/', ApportionmenCreateView.as_view(), name='create-apportionmet'),
    path('appotionment/delete/<pk>/', ApportionmenDeleteView.as_view(), name='delete-apportionmet'),
    path('appotionment/detail/<pk>/', ApportionmenDetailView.as_view(), name='detail-apportionmet'),
    path('appotionment/update/<pk>/', ApportionmenUpdateView.as_view(), name='update-apportionmet'),
    #ApportionmentDetail
    path('apportionment-detail/create/', ApportionmentDetailCreateView.as_view(), name='create-apportionment-detail'),
    path('apportionment-detail/delete/<pk>/', ApportionmentDetailDeleteView.as_view(), name='delete-apportionment-detail'),
    path('apportionment-detail/detail/<pk>/', ApportionmentDetailDetailView.as_view(), name='detail-apportionment-detail'),
    path('apportionment-detail/update/<pk>/', ApportionmentDetailUpdateView.as_view(), name='update-apportionment-detail'),
    #Expense
    path('expense/create/', ExpenseCreateView.as_view(), name='create-expense'),
    path('expense/delete/<pk>/', ExpenseDeleteView.as_view(), name='delete-expense'),
    path('expense/detail/<pk>/', ExpenseDetailView.as_view(), name='detail-expense'),
    path('expense/update/<pk>/', ExpenseUpdateView.as_view(), name='update-expense'),
    #InfoInvoice
    path('info-invoice/create/', InfoInvoiceCreateView.as_view(), name='create-info-invoice'),
    path('info-invoice/delete/<pk>/', InfoInvoiceDeleteView.as_view(), name='delete-info-invoice'),
    path('info-invoice/detail/<pk>/', InfoInvoiceDetailDetailView.as_view(), name='detail-info-invoice'),
    path('info-invoice/update/<pk>/', InfoInvoiceUpdateView.as_view(), name='update-info-invoice'),
    #InfoInvoiceDetail
    path('info-invoice-detail/create/', InfoInvoiceDetailCreateView.as_view(), name='create-info-invoice-detail'),
    path('info-invoice-detail/delete/<pk>/', InfoInvoiceDetailDeleteView.as_view(), name='delete-info-invoice-detail'),
    path('info-invoice-detail/detail/<pk>/', InfoInvoiceDetailDetailView.as_view(), name='detail-info-invoice-detail'),
    path('info-invoice-detail/update/<pk>/', InfoInvoiceDetailUpdateView.as_view(), name='update-info-invoice-detail'),
    #Ledger
    path('ledger/create/', LedgerCreateView.as_view(), name='create-ledger'),
    path('ledger/delete/<pk>/', LedgerDeleteView.as_view(), name='delete-ledger'),
    path('ledger/detail/<pk>/', LedgerDetailView.as_view(), name='detail-ledger'),
    path('ledger/update/<pk>/', LedgerUpdateView.as_view(), name='update-ledger'),
    #Order
    path('order/create/', OrderCreateView.as_view(), name='create-order'),
    path('order/delete/<pk>/', OrderDeleteView.as_view(), name='delete-order'),
    path('order/detail/<pk>/', OrderDetailView.as_view(), name='detail-order'),
    path('order/update/<pk>/', OrderUpdateView.as_view(), name='update-order'),
    path('order/all-data/<nro_order>/', GetCompleteOrderInfoAPIView.as_view(), name='complete-order-data'),
    #OrderInvoice
    path('order-invoice/create/', OrderInvoiceCreateView.as_view(), name='create-order-invoice'),
    path('order-invoice/delete/<pk>/', OrderInvoiceDeleteView.as_view(), name='delete-order-invoice'),
    path('order-invoice/detail/<pk>/', OrderInvoiceDetailView.as_view(), name='detail-order-invoice'),
    path('order-invoice/update/<pk>/', OrderInvoiceUpdateView.as_view(), name='update-order-invoice'),
    #OrderInvoiceDetail
    path('order-invoice-detail/create/', OrderInvoiceDetailCreateView.as_view(), name='create-order-invoice-detail'),
    path('order-invoice-detail/delete/<pk>/', OrderInvoiceDetailDeleteView.as_view(), name='delete-order-invoice-detail'),
    path('order-invoice-detail/detail/<pk>/', OrderInvoiceDetailDetailView.as_view(), name='detail-order-invoice-detail'),
    path('order-invoice-detail/update/<pk>/', OrderInvoiceDetailUpdateView.as_view(), name='update-order-invoice-detail'),
    #PaidInvoice
    path('paid-invoice/create/', PaidInvoiceCreateView.as_view(), name='create-paid-invoice' ),
    path('paid-invoice/delete/<pk>/', PaidInvoiceDeleteView.as_view(), name='delete-paid-invoice' ),
    path('paid-invoice/detail/<pk>/', PaidInvoiceDetailView.as_view(), name='detail-paid-invoice' ),
    path('paid-invoice/update/<pk>/', PaidInvoiceUpdateView.as_view(), name='update-paid-invoice' ),
    path('paid-invoice/all/<id_paid>/', CompletePaidView.as_view(), name='all_paid_invoice'),
    #PaidInvoiceDetail
    path('paid-invoice-detail/create/', PaidInvoiceDetailCreateView.as_view(), name='create-paid-invoice-detail'),
    path('paid-invoice-detail/delete/<pk>/', PaidInvoiceDetailDeleteView.as_view(), name='delete-paid-invoice-detail'),
    path('paid-invoice-detail/detail/<pk>/', PaidInvoiceDetailDetailView.as_view(), name='detail-paid-invoice-detail'),
    path('paid-invoice-detail/update/<pk>/', PaidInvoiceDetailUpdateView.as_view(), name='update-paid-invoice-detail'),
    #Partial
    path('partial/create/', PartialCreateView.as_view(), name='create-partial' ),
    path('partial/delete/<pk>/', PartialDeleteView.as_view(), name='delete-partial' ),
    path('partial/detail/<pk>/', PartialDetailView.as_view(), name='detail-partial' ),
    path('partial/update/<pk>/', PartialUpdateView.as_view(), name='update-partial' ),
    path('partial/all-data/<id_partial>/', CompletePartialInfoApiView.as_view(), name='all-info-partial' ),
    #Product
    path('product/create/', ProductCreateView.as_view(), name='create-product' ),
    path('product/delete/<pk>/', ProductDeleteView.as_view(), name='delete-product' ),
    path('product/detail/<pk>/', ProductDetailView.as_view(), name='detail-product' ),
    path('product/update/<pk>/', ProductUpdateView.as_view(), name='update-product' ),
    #Suppliers
    path('suppliers/create/', SupplierCreateView.as_view(), name='create-suppliers' ),
    path('suppliers/delete/<pk>/', SupplierDeleteView.as_view(), name='delete-suppliers' ),
    path('suppliers/detail/<pk>/', SupplierDetailView.as_view(), name='detail-suppliers' ),
    path('suppliers/update/<pk>/', SupplierUpdateView.as_view(), name='update-suppliers' ),
    #utils
    path('orders/all/', AllOrders.as_view(), name="all-orders-list"),
]
