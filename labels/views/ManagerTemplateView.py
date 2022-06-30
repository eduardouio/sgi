import json
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView
from labels.lib_src import ValidateRangeSafeTrack, SignMessageSafeTrack
from labels.models import Label
from lib_src.sgi_utlils import get_host
from logs.app_log import loggin


# /labels/manager/
class ManagerTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'labels/administrador.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Accesando a Administrador de Etiquetas')
        labels = Label.objects.all()

        if request.GET:
            action = request.GET.get('action')
            deep = int(request.GET.get('deep'))

            if action == 'verify':
                self.validate(labels, deep)

            if action == 'activate':
                self.activate(labels, deep)

        context = self.get_context_data(**kwargs)
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

    def validate(self, labels, deep):
        loggin('i', 'Validando rango de etiquetas')
        validate_range = ValidateRangeSafeTrack()
        labels = Label.objects.filter(Q(bg_status='I') | Q(bg_status='E'))
        labels = labels[:deep]

        for label in labels:
            loggin('i', 'Validando rango etiquetas')
            result = validate_range.validate(
                    label.initial_range, label.end_range, label.quantity
            )
            if (((result['first_tag'] == label.initial_range) or 
                (result['first_tag'] == label.end_range)) and
            ((result['last_tag'] == label.initial_range) or
             (result['last_tag'] == label.end_range))):
                label.bg_status = 'V'
                label.message_status = 'Validado Correctamente'
                label.validated_date = datetime.now()
                label.initial_range = result['first_tag']
                label.end_range = result['last_tag']
                label.checked_reverse = result['cheked_reverse']
                label.concordance = result['concordance']
                label.difference = result['difference']
                data = result['response']
                del(result['response'])
                result = json.dumps(result)
                label.response = result + '===> ' + data.text
                label.save()
                self.sign(label)
            else:
                label.bg_status = 'E'
                label.validated_date = datetime.now()
                label.message_status = 'Error al Validar'
                label.response = json.dumps(result)
                label.save()

    def sign(self, label):
        loggin('i', 'Firmando mensaje')
        message = '{"uniqueMarks":["{f_tag}"],"iceSku":"{l_tag}","businessId":"{business_id}"}'
        import ipdb; ipdb.set_trace()
        message.replace('f.tag', label.initial_range)
        message.replace('l.tag', label.end_range)
        import ipdb; ipdb.set_trace()

    def activate(self, labels, deep):
        loggin('i', 'Activando rango de etiquetas')
        pass


