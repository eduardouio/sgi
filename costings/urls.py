from django.urls import include, path

from costings.views import (LiquidateOrderTemplateView,
                            LiquidatePartialTemplateView, ErrorTemplateView, LedgerReportView)

app_name = 'costings'

urlpatterns = [
    path('pedido/<nro_order>/',LiquidateOrderTemplateView.as_view(),name="validate_order"),
    path('parcial/<nro_order>/<ordinal_parcial>/',LiquidatePartialTemplateView.as_view(),name="validate_partial"),    
    path('error/<nro_order>/<ordinal_parcial>/', ErrorTemplateView.as_view(), name ="error_last_open"),
    path('saldo-mayor/<nro_order>/', LedgerReportView.as_view(), name="reporte_mayor"),
]
