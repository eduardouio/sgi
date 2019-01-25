from django.urls import path, include
from costings.views.LiquidateOrderTemplateView import LiquidateOrderTemplateView
from costings.views.LiquidatePartialTemplateView import LiquidatePartialTemplateView
app_name = 'authentication'


urlpatterns = [
    path('pedido/<nro_order>/',LiquidateOrderTemplateView.as_view(),name="validate_order"),
    path('parcial/<nro_order>/<ordinal_parcial>/',LiquidatePartialTemplateView.as_view(),name="validate_partial"),    
]
