from django.urls import path, include
from audit.views import InvoiceTemplateView
app_name = 'audit'

urlpatterns = [
    path('factura/<id_invoice>/', InvoiceTemplateView.as_view(), name="show-invoice")
]