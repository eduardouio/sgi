from django.urls import path

# import views
from .views import SapProductsTV

app_name = 'sap'

urlpatterns = [
    path('productos/', SapProductsTV.as_view(), name='sap-productos'),
]
