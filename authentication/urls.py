from django.urls import include, path

from authentication.views import (HomeTemplateView, LoginTemplateView,
                                  LogoutRedirectView)

app_name = 'authentication'

urlpatterns = [
    path('login/',LoginTemplateView.as_view(),name="authetication"),
    path('logout/',LogoutRedirectView.as_view(),name="desauthetication"),
    path('', HomeTemplateView.as_view(), name="home"),
]
