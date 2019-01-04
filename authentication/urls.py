from django.urls import path, include
from authentication.views import LoginTemplateView
app_name = 'authentication'

urlpatterns = [
    path('',LoginTemplateView.as_view(),name="authetication")
]

