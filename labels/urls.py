from django.urls import path

from labels.views import (LabelTemplateView, ManagerTemplateView,
                          TagsListTemplateView, TagsOrderTemplateView)

app_name = 'labels'

urlpatterns = [
    path('manager/', ManagerTemplateView.as_view(), name="manager-labels"),
    path('pedidos/', TagsListTemplateView.as_view(), name="pedidos-activos"),
    path('label/', LabelTemplateView.as_view(), name="pedidos-activos"),
    path('detalle/<nro_order>/', TagsOrderTemplateView.as_view(), name="pedidos-activos"),
]
