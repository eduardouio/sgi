from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sgi.settings import EMPRESA

from logs.app_log import loggin

# /logout/
class LogoutRedirectView(LoginRequiredMixin, RedirectView):
    """Realiza el cierre de la sesion del usuario"""
    url = 'login/'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Cerrando sesion para {}'.format(request.User))
        logout(request)
        return HttpResponseRedirect(self.get_redirect_url())
