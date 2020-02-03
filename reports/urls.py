from django.urls import include, path
from .views import ICEReportTemplateView

app_name = 'reports'

urlpatterns = [
    path('ice/<int:year>/<int:month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
]
