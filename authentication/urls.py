from django.urls import path, include
from authentication.views import LoginTemplateView, LogoutRedirectView
app_name = 'authentication'

urlpatterns = [
    path('',LoginTemplateView.as_view(),name="authetication"),
    path('logout/',LogoutRedirectView.as_view(),name="desauthetication")
]

