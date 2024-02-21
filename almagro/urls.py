from django.urls import include, path
from .views import AlmagroImportTV, ValidatorTV, SuccessTV

app_name='importations'

urlpatterns = [
     path('importar/', AlmagroImportTV.as_view(), name="almagro-import"),
     path('analisis/', ValidatorTV.as_view(), name="almagro-analisis"),
     path('ok/', SuccessTV.as_view(), name="almagro-success"),
]