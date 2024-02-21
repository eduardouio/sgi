from django.urls import path, include
from audit.views import InvoiceTemplateView, InvoiceListTemplateView, ProductInvoiceTemplateView
app_name = 'audit'

urlpatterns = [
    path('', InvoiceListTemplateView.as_view(), name="lint-invoice"),
    path('factura/<id_invoice>/', InvoiceTemplateView.as_view(), name="show-invoice"),
    path('factura-exterior/<id_invoice>/', ProductInvoiceTemplateView.as_view(), name="show-ext-invoice"),
]