from django.urls import path, include
from orders.views import OrderSaleTemplateView, CompleteOrderTemplateView, OrdersListView
from orders.views.OrderCreateView import OrderCreateView
app_name = 'authentication'

urlpatterns = [
    path('listar/', OrdersListView.as_view(), name="list of orders"),
    path('ficha/<nro_order>/', CompleteOrderTemplateView.as_view(), name="view_all_order"),
    path('saldos/', OrderSaleTemplateView.as_view() ,name="sales_of_order"),
    path('crear/', OrderCreateView.as_view(), name="crear_order"),
]