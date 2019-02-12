from django.urls import include, path

from costings.views import (LiquidateOrderTemplateView,
                            LiquidatePartialTemplateView)

app_name = 'costings'


urlpatterns = [
    path('pedido/<nro_order>/',LiquidateOrderTemplateView.as_view(),name="validate_order"),
    path('parcial/<nro_order>/<ordinal_parcial>/',LiquidatePartialTemplateView.as_view(),name="validate_partial"),    
]
