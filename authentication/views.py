from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import http


class LoginTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/'
    template_name = 'base/base.html'    

    def get(self, request, *args, **kwargs):
        context = super(LoginTemplateView, self).get_context_data(*args, **kwargs)
        return http.HttpResponseRedirect('/admin/')