from django.urls import include, path
from .views import ICEReportTemplateView

app_name = 'reports'

urlpatterns = [
    path('ice/<year>/<month>/', ICEReportTemplateView.as_view(),name='reporte-ice'),
]
