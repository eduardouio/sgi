from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from sgi.settings import EMPRESA

from logs.app_log import loggin


# /home/
class HomeTemplateView(LoginRequiredMixin, TemplateView):
    '''Direcciona al home del proyecto'''
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
        }
        return self.render_to_response(context)