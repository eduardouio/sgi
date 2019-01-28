from django.urls import path, include
from orders.views.OrderSaleTemplateView import OrderSaleTemplateView
app_name = 'authentication'

urlpatterns = [
    path('saldos/', OrderSaleTemplateView.as_view() ,name="sales_of_order"),
]