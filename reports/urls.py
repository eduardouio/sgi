from django.urls import path

from .views import (ICEAnexoReportTemplateView, ICEReportTemplateView,
                    WarenhouseArrivalsTemplateView, ExpensesReportTemplateView,
                    ActiveOrdersTemplateView, CostAnalysisTemplateView,
                    CurrentNationalizationTV, LastCostTemplateView,)

app_name = 'reports'

urlpatterns = [
    path('ice/', ICEReportTemplateView.as_view(),name='reporte-ice'),
    path('anexo-ice/<int:year>/<int:month>/',ICEAnexoReportTemplateView.as_view(), name='anexo-ice'),
    path('llegadas/bodega/local/', WarenhouseArrivalsTemplateView.as_view(),name='llegada-bodega-local'),
    path('provisiones/', ExpensesReportTemplateView.as_view(), name='reporte-provisiones'),
    path('activos/', ActiveOrdersTemplateView.as_view(), name='reporte-pedidos-activos'),
    path('analisis-costos/', CostAnalysisTemplateView.as_view(),name='reporte-analisis-costos'),
    path('procesos-activos/', CurrentNationalizationTV.as_view(), name='reporte-nacionalizaciones'),
    path('ultimo-costo/', LastCostTemplateView.as_view(), name='reporte-ultimo-costo'),
]
