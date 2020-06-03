from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import RedirectView, TemplateView

from logs.app_log import loggin


class LoginTemplateView(TemplateView):
    template_name = 'base/login-form.html'
    success_url = 'pedidos/listar/'
    login_url = '/?error=true'

    def get(self, request, *args, **kwargs):
        if request.GET:
            self.success_url = request.GET['next']

        if request.user.is_authenticated:            
            return HttpResponseRedirect(self.success_url)

        loggin('i', 'intentando inciar sesion')
        context = self.get_context_data(**kwargs)
        context['empresa'] = settings.EMPRESA
        context['have_next'] = True if request.GET else False
        context['next'] = '' if not request.GET else request.GET['next']
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
        if user_db.check_password(data['password']) == False:
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

            # colocar aqui la redireccion para los otros perfiles
            if data.get('next'):
                self.success_url = data['next']
            elif user.groups.filter(name='auditoria').exists():
                self.success_url = 'auditoria/'

            return HttpResponseRedirect(self.success_url)
        return HttpResponseRedirect(self.error_url)


# /logout/
class LogoutRedirectView(RedirectView):
    """Realiza el cierre de la sesion del usuario"""
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(self.get_redirect_url())
