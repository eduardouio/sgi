from django.urls import path

from .views import (HomeReportsTemplateView,
                    ICEAnexoReportTemplateView, ICEReportTemplateView,
                    WarenhouseArrivalsTemplateView, ExpensesReportTemplateView)

app_name = 'reports'

urlpatterns = [
    path('', HomeReportsTemplateView.as_view(),name='home-reportes'),
    path('ice/<int:year>/<int:month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
    path('anexo-ice/<int:year>/<int:month>/',ICEAnexoReportTemplateView.as_view(), name='anexo-ice'),
    path('llegadas/bodega/local/<int:year>/<int:month>/', WarenhouseArrivalsTemplateView.as_view(),name='llegada-bodega-local'),
    path('provisiones/', ExpensesReportTemplateView.as_view(), name='reporte-provisiones'),
]
