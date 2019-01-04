from django.urls import path, include
from costings.views.liquidateOrderTemplateView import liquidateOrderTemplateView
#from costings.views.liquidatePartialsTemplateView import liquidatePartialsTemplateView
from costings.views.AllProvisionsTemplateView import AllProvisionsTemplateView
app_name = 'authentication'

urlpatterns = [
    path('pedido/<nro_order>/',liquidateOrderTemplateView.as_view(),name="validate_order"),    
    #path('parcial/<nro_order>/<ordinal_parcial>/',liquidatePartialsTemplateView.as_view(),name="validate_order"),    
]