from django.urls import path, include
from orders.views.apiViews import get_complete_order_info
from orders.views.OrderSaleTemplateView import OrderSaleTemplateView
from orders.views.ListOrders import pedidos_lista
app_name = 'authentication'

urlpatterns = [
    path('get_all_data/<nro_order>/', get_complete_order_info ,name="validate_order"),    
    path('saldos/<nro_order>/', OrderSaleTemplateView.as_view() ,name="sales_of_order"),    
    path('listado', pedidos_lista ,name="lista"),    
]