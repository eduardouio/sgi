from django.urls import path, include
from orders.views.apiViews import GetCompleteOrderInfoAPIView
from orders.views.OrderSaleTemplateView import OrderSaleTemplateView
from orders.views.ListOrders import pedidos_lista
app_name = 'authentication'

urlpatterns = [
    path('get_all_data/<nro_order>/', GetCompleteOrderInfoAPIView.as_view() ,name="validate_order_json"),
    path('saldos/', OrderSaleTemplateView.as_view() ,name="sales_of_order"),    
    path('listado', pedidos_lista ,name="lista"),    
]