from django.urls import path

from .views import (ICEAnexoReportTemplateView, ICEReportTemplateView,
                    PurcharseSupplierTemplateView,
                    WarenhouseArrivalsTemplateView, HomeTemplateView)

app_name = 'reports'

urlpatterns = [
    path('', HomeTemplateView.as_view(),name='home-reportes'),
    path('ice/<int:year>/<int:month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
    path('anexo-ice/<int:year>/<int:month>/',ICEAnexoReportTemplateView.as_view(), name='anexo-ice'),
    path('compras/<str:id_supplier>/', PurcharseSupplierTemplateView.as_view(),name='reporte-compras'),
    path('llegadas/bodega/local/<int:year>/<int:month>/', WarenhouseArrivalsTemplateView.as_view(),name='llegada-bodega-local'),
]
