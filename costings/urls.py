from django.urls import path, include
from .views import validOrderTemplateView
app_name = 'authentication'

urlpatterns = [
    path('liquidar/<type>/<id_row>',validOrderTemplateView.as_view(),name="validate_order")
]

