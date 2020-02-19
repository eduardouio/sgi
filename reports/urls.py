from django.urls import include, path
from .views import ICEReportTemplateView, PurcharseSupplierTemplateView

app_name = 'reports'

urlpatterns = [
    path('ice/<int:year>/<int:month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
    path('compras/<str:id_supplier>/', PurcharseSupplierTemplateView.as_view(),name='reporte-compras'),
]
