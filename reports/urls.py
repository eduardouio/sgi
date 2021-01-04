from django.urls import path

from .views import (ICEAnexoReportTemplateView, ICEReportTemplateView,
                    WarenhouseArrivalsTemplateView, ExpensesReportTemplateView,
                    ActiveOrdersTemplateView)

app_name = 'reports'

urlpatterns = [
    path('ice/<int:year>/<int:month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
    path('anexo-ice/<int:year>/<int:month>/',ICEAnexoReportTemplateView.as_view(), name='anexo-ice'),
    path('llegadas/bodega/local/', WarenhouseArrivalsTemplateView.as_view(),name='llegada-bodega-local'),
    path('provisiones/', ExpensesReportTemplateView.as_view(), name='reporte-provisiones'),
    path('activos/', ActiveOrdersTemplateView.as_view(), name='reporte-pedidos-activos'),
]
