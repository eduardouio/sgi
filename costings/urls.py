from django.urls import path, include
from costings.views.liquidateOrderTemplateView import liquidateOrderTemplateView
from costings.views.AllProvisionsTemplateView import AllProvisionsTemplateView
app_name = 'authentication'

urlpatterns = [
    path('iniciales/<nro_order>/',liquidateOrderTemplateView.as_view(),name="validate_order"),    
    path('parciales/<nro_order>/<ordinal_parcial>/',liquidateOrderTemplateView.as_view(),name="validate_order"),    
    path('provisiones/',AllProvisionsTemplateView.as_view(),name="all_provisions"),    
]