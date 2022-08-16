from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from labels.lib_src import ActivateRangeSafeTrack, LoginSafeTrack
from labels.models import Label
from lib_src.sgi_utlils import get_host
from logs.app_log import loggin


# /labels/manager/
class ManagerTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'labels/administrador.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Accesando a Administrador de Etiquetas')
        if request.GET:
            action = request.GET.get('action')
            pk = int(request.GET.get('pk'))
            self.activate(action, pk, deep=pk)

        labels = Label.objects.all()
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Manager Etiquetas',
            'host': get_host(request),
            'labels': self.sortOut(labels)
        }
        return self.render_to_response(context)

    def sortOut(self, labels):
        data = {
            'inactive': [],
            'active': [],
            'error': [],
            'rejected': [],
            'total_inactive': 0,
            'total_active': 0,
            'total_error': 0,
            'total_rejected': 0,
        }
        if len(labels) == 0:
            return data

        for label in labels:
            if label.bg_status == 'I':
                data['inactive'].append(label)
                data['total_inactive'] += label.quantity
            elif label.bg_status == 'A':
                data['active'].append(label)
                data['total_active'] += label.quantity   
            elif label.bg_status == 'E' or label.bg_status == 'S':
                data['error'].append(label)
                data['total_error'] += label.quantity
            else:
                data['rejected'].append(label)
                data['total_rejected'] += label.quantity

        return data

    def activate(self, action, pk, deep=0):
        loggin('i', 'accion  {} con rango de etiquetas {}'.format(action, pk))

        if action == 'activate_pk':
            login = LoginSafeTrack()
            RangeActivator = ActivateRangeSafeTrack(login)
            label = Label.objects.get(pk=pk)
            RangeActivator.try_activate(label)
        elif action == 'activate_all':
            login = LoginSafeTrack()
            RangeActivator = ActivateRangeSafeTrack(login)
            labels = Label.objects.filter(bg_status='I')
            for label in labels:
                RangeActivator.try_activate(label)
        elif action == 'move_to_error':
            label = Label.objects.get(pk=pk)
            label.bg_status = 'E'
            label.last_jwt = 'Se mueve a la cola de error'
            label.save()
        elif action == 'move_to_inactive':
            label = Label.objects.get(pk=pk)
            label.bg_status = 'I'
            label.last_jwt = 'Se mueve a la cola de inactivo'
            label.save()
        elif action == 'move_all_to_inactive':
            labels = Label.objects.all().exclude(bg_status='A')
            for label in labels:
                label.bg_status = 'I'
                label.last_jwt = 'Se mueve a la cola de inactivo'
                label.save()

        return None
