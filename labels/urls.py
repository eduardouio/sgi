from django.urls import path
from labels.views import (TagsListTemplateView, TagsOrderTemplateView)


app_name = 'labels'

urlpatterns = [
    path('pedidos/', TagsListTemplateView.as_view(), name="pedidos-activos"),
    path('detalle/<nro_order>/', TagsOrderTemplateView.as_view(), name="pedidos-activos"),
]
