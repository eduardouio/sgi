from django.urls import path
from products.views import ProductDetailView

app_name = 'products'

urlpatterns = [
    path('ver/<pk>/', ProductDetailView.as_view(), name='product-detail')
]
