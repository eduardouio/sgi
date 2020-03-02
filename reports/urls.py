from django.urls import path

from .views import (ICEAnexoReportTemplateView, ICEReportTemplateView,
                    PurcharseSupplierTemplateView)

app_name = 'reports'

urlpatterns = [
    path('ice/<int:year>/<int:month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
    path('anexo-ice/<int:year>/<int:month>/',ICEAnexoReportTemplateView.as_view(), name='anexo-ice'),
    path('compras/<str:id_supplier>/', PurcharseSupplierTemplateView.as_view(),name='reporte-compras'),
]
