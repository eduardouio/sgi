from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from sgi.settings import EMPRESA

from logs.app_log import loggin


# /login/
class LoginTemplateView(TemplateView):
    template_name = 'base/login-form.html'
    success_url = '/'
    login_url = '/'
    error_url = '?error=true'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['have_next'] = False
        if request.GET:
            if request.GET.get('next'):
                self.success_url = request.GET['next']
                context['have_next'] = True

        # Si el usuario tiene sesion va al home
        if request.user.is_authenticated:            
            return HttpResponseRedirect(self.success_url)

        loggin('i', 'intentando inciar sesion')
        context['next'] = self.success_url
        context['enterprise'] = EMPRESA
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        loggin('i', 'Verificando informacion')
        data = request.POST
        user_is_valid = True
        try:
            user_db = User.objects.get(username=data['username'])
        except ObjectDoesNotExist:
            loggin('w', 'Usuario incorrecto {}'.format(data['username']))
            return HttpResponseRedirect(self.error_url)
        if user_db.check_password(data['password']) is False:
            loggin('w', 'Password incorrecto {}'.format(data['password']))
            return HttpResponseRedirect(self.error_url)
        if user_is_valid:
            user = authenticate(
                    request=request,
                    username=data['username'],
                    password=data['password'])
            login(
                request=request,
                user=user,
                backend='django.contrib.auth.backends.ModelBackend'
                )

            return HttpResponseRedirect(self.success_url)
        return HttpResponseRedirect(self.error_url)
