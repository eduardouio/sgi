import json
from datetime import datetime

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from labels.lib_src import (LoginSafeTrack, SignMessageSafeTrack,
                            ValidateTagSafeTrack)
from labels.models import OneLabel
from logs.app_log import loggin
from products.models import Product
from sgi.settings import EMPRESA


# /etiquetas/label/
class LabelTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'labels/etiquetas-solas.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Administrador de activacion etiquetas sueltas')
        message = None

        if request.GET.get('action') == 'regiter':
            message = 'Etiquetas Registradas, proceda a activarlas'
        if request.GET.get('action') == 'activate':
            message = 'Etiquetas enviadas a activar, veirifique el estado'
            self.validate_tag(int(request.GET.get('size')))
            self.__sign()
            self.activate_tag()
        if request.GET.get('action') == 'move_all_to_incatives':
            self.move_to_inactive_all()

        all_products = Product.objects.all().order_by('nombre')[:5000]
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Activacion Etiquetas',
            'all_products': all_products,
            'meesage': message,
            'labels': self.get_labels(),
        }

        if request.GET.get('action'):
            return HttpResponseRedirect('/etiquetas/label/')

        return self.render_to_response(context)

    def validate_tag(self, size):
        loggin(
            'i', 'Enviamos un lote de {} etiquetas a activar'.format(size)
        )
        today = datetime.now()
        labels = OneLabel.objects.filter(bg_status='I')[:size]
        login = LoginSafeTrack()
        validate_tag = ValidateTagSafeTrack(login)

        for label in labels:
            label.validated_date = today
            result = validate_tag.validate(
                label.code_label,
                self.vefrify_ice_sku(label.cod_contable.cod_ice)
            )
            label.response = result['response']
            label.message_status = result['error_message']

            if result['is_valid']:
                label.notas = result['error_message']
                if result['is_active']:
                    label.bg_status = 'A'
                else:
                    label.bg_status = 'V'
            else:
                label.bg_status = 'E'
                label.notas = result['error_message']

            label.save()

    def __sign(self):
        loggin('i', 'firmamos etiqetas')
        labels = OneLabel.objects.filter(bg_status='V')
        signMessage = SignMessageSafeTrack()
        today = datetime.now()
        for label in labels:
            label.signed_date = today
            cod_ice = self.vefrify_ice_sku(label.cod_contable.cod_ice)
            if cod_ice is not False:
                message = """{"uniqueMarks":["label"],"iceSku":"ice_sku","businessId":"business_id"}"""
                message = message.replace('label', label.code_label)
                message = message.replace(
                    'ice_sku', self.vefrify_ice_sku(label.cod_contable.cod_ice)
                )
                sign = signMessage.sign(message)
                label.sign = sign['signature']
                label.message = sign['message']
                label.bg_status = 'F'
                label.message_status += ' Mensaje Firmado'
                label.save()
            else:
                label.bg_status = 'E'
                label.message_status = 'Error en el codigo ICE'
                label.save()

    def activate_tag(self):
        loggin('i', 'activamos etiqetas')
        labels = OneLabel.objects.filter(bg_status='F')  # F->Signed
        if len(labels) == 0:
            loggin('i', 'Sin etiquetas por activar')
            return None
        today = datetime.now()
        login = LoginSafeTrack()

        for label in labels:
            label.activated_date = today
            label.bg_status = 'S'
            label.message_status += ' Enviado request para activar'
            data = {
                "address": EMPRESA['safetrack']['wallet']['networkAddress'],
                "network": EMPRESA['safetrack']['wallet']['network'],
                "msg": label.message,
                "signature": label.sign
            }
            response = requests.put(
                EMPRESA['safetrack']['url_activate_tag'],
                data=json.dumps(data),
                headers=login.my_headers
            )
            response_data = json.loads(response.text)
            label.response = response.text
            if response.status_code == 200:
                label.bg_status = 'A'
                label.notas = response.text
                label.message_status = 'Activado Correctamente'
            elif response.status_code == 500:
                label.notas = response_data['description']
                label.bg_status = 'E'
                label.message_status = '{} Error no se puede activar'.format(
                    response.status_code
                )
            label.save()

    def post(self, request, *args, **kwargs):
        loggin('i', 'registrado etiquetas para activacion')
        product = Product.get_by_cod_contable(request.POST.get('cod_contable'))
        labels = request.POST.get('labels').upper().splitlines()
        for label in labels:
            new_label = {
                'cod_contable': product,
                'code_label': label,
                'bg_status': 'I',
            }
            one_label = OneLabel(**new_label)
            one_label.save()

        return HttpResponseRedirect('/etiquetas/label/?registered=ok')

    def get_labels(self):
        all_lables = OneLabel.objects.all().order_by('-date_created')[:1200]
        loggin('i', 'Clasificando Etiquetas')
        data = {
            'total_inactives': 0,
            'total_actives': 0,
            'total_rejected': 0,
            'total_error': 0,
            'labels': {
                'inactives': [],
                'actives': [],
                'rejected': [],
                'error': []
            }
        }
        for label in all_lables:
            if label.bg_status == 'I':
                data['total_inactives'] += 1
                data['labels']['inactives'].append(label)
            elif label.bg_status == 'A':
                data['total_actives'] += 1
                data['labels']['actives'].append(label)
            else:
                data['total_error'] += 1
                data['labels']['error'].append(label)

        return data

    def move_to_inactive_all(self):
        loggin('i','Mueve todo a inactivos')
        labels = OneLabel.objects.exclude(bg_status='A')
        for label in labels:
            label.bg_status = 'I'
            label.message_status = 'Movido a la cola de inactivos'
            label.save()
        return None

    def vefrify_ice_sku(self, ice_sku):
        spected_long_ice_sku = [4, 3, 6, 3, 6, 2, 3, 6]
        ice_sku_parts = ice_sku.split('-')
        ice_valid = []

        if len(spected_long_ice_sku) != len(ice_sku_parts):
            loggin('e', 'Longitud de ICE SKU incorrecta')
            return False

        for i, sku in enumerate(ice_sku_parts):
            if i == 1:
                sku = '0' + sku

            if len(sku) != spected_long_ice_sku[i]:
                loggin('e', 'Longitud de ICE SKU incorrecta')
                return False

            ice_valid.append(sku)

        loggin('i', 'Logitudes ICE SKU correcto')
        return '-'.join(ice_valid)
