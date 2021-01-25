from django.urls import path

from products.views import (ProductDetailView, ProductListView,
                            ProductUpdateView, ProductCreateView)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('ver/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('editar/<pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('crear/', ProductCreateView.as_view(), name='product-create'),
]
