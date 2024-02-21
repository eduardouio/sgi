from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from logs.app_log import loggin


# /logout/
class LogoutRedirectView(LoginRequiredMixin, RedirectView):
    """Realiza el cierre de la sesion del usuario"""
    url = '/'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Se cierra la sesion de usuario {}'.format(
            request.user.username
        ))
        logout(request)
        return HttpResponseRedirect(self.get_redirect_url())
