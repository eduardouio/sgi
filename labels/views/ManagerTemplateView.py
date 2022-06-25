from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from lib_src.sgi_utlils import get_host
from logs.app_log import loggin
from labels.models import Label


# /labels/manager/
class ManagerTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'labels/administrador.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Accesando a Administrador de Etiquetas')
        context = self.get_context_data(**kwargs)
        labels = Label.objects.all()

        context['data'] = {
            'title_page': 'Manager Etiquetas',
            'host': get_host(request),
            'labels': self.sortOut(labels),
        }
        return self.render_to_response(context)

    def sortOut(self, labels):
        data = {
            'inactive': [],
            'validated': [],
            'active': [],
            'error': [],
        }
        if len(labels) == 0:
            return data

        for label in labels:
            if label.bg_status == 'I':
                data['inactive'].append(label)
            elif label.bg_status == 'V':
                data['validated'].append(label)
            elif label.bg_status == 'A':
                data['active'].append(label)
            elif label.bg_status == 'E':
                data['error'].append(label)

        return data

    def validate(self, data):
        pass

    def activate(self, data):
        pass