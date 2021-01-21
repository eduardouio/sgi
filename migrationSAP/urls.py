from django.urls import path

# import views
from .views import SapProductsTV, SapImportWizardTV

app_name = 'sap'

urlpatterns = [
    path('productos/', SapProductsTV.as_view(), name='sap-productos'),
    path('importar-pedidos/', SapImportWizardTV.as_view(), name='sap-pedidos'),
]
