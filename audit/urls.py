from django.urls import path, include
from audit.views import InvoiceTemplateView, InvoiceListTemplateView
app_name = 'audit'

urlpatterns = [
    path('factura/<id_invoice>/', InvoiceTemplateView.as_view(), name="show-invoice"),
    path('', InvoiceListTemplateView.as_view(), name="lint-invoice"),
]