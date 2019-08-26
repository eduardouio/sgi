from django.urls import path, include
from orders.views import OrderSaleTemplateView, CompleteOrderTemplateView, OrdersListView
app_name = 'authentication'

urlpatterns = [
    path('', OrdersListView.as_view(), name="list of orders"),
    path('ficha/<nro_order>/', CompleteOrderTemplateView.as_view(), name="view_all_order"),
    path('saldos/', OrderSaleTemplateView.as_view() ,name="sales_of_order"),
]