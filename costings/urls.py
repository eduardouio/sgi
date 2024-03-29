from django.urls import include,  path

from costings.views import (ErrorTemplateView, GeneralLedgerTemplateView,
                            LedgerReportView, LiquidateOrderTemplateView,
                            LiquidatePartialTemplateView, ICEXmlFormView)

app_name = 'costings'

urlpatterns = [
    path('pedido/<nro_order>/',LiquidateOrderTemplateView.as_view(),name="validate_order"),
    path('parcial/<nro_order>/<ordinal_parcial>/',LiquidatePartialTemplateView.as_view(),name="validate_partial"),    
    path('error/<nro_order>/<ordinal_parcial>/', ErrorTemplateView.as_view(), name ="error_last_open"),
    path('saldo-mayor-general/', LedgerReportView.as_view(), name="reporte_mayor"),
    path('mayor/', GeneralLedgerTemplateView.as_view(), name="listado_mayor"),
    path('ice-xml/', ICEXmlFormView.as_view(), name="anexo_ice"),
]
