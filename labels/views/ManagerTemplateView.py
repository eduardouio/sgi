import json
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import TemplateView
from labels.lib_src import (ActivateRangeSafeTrack, SignMessageSafeTrack,
                            ValidateRangeSafeTrack)
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
            deep = int(request.GET.get('deep'))

            if action == 'verify':
                self.validate(deep)

            if action == 'activate':
                self.activate(deep)

        labels = Label.objects.all()
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

    def validate(self, deep):
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
        ice_sku = label.id_factura_detalle.cod_contable.cod_ice
        valid_ice_sku = self.vefrify_ice_sku(ice_sku)

        if not valid_ice_sku:
            loggin('e', 'SKU ICE no valido')
            label.status = 'E'
            label.message_status = 'SKU ICE no valido, las logitudes no coinciden'
            label.save()
            return False
        message = '{"uniqueMarks": [{"uniqueMarkStart": "f_tag", "uniqueMarkEnd": "l_tag"}], "iceSku": "{ice_sku}", "businessId": "{business_id}"}'
        message = message.replace('f_tag', label.initial_range)
        message = message.replace('l_tag', label.end_range)
        message = message.replace('ice_sku', valid_ice_sku)
        SignMessage = SignMessageSafeTrack()
        label.sign = SignMessage.sign(message)
        label.status = 'S'
        label.message_status = 'Mensaje Firmado'
        label.message = message
        label.save()
        return True

    def activate(self, deep):
        loggin('i', 'Activando rango de etiquetas')
        RangeActivator = ActivateRangeSafeTrack()
        labels = Label.objects.filter(bg_status='V')
        labels = labels[:deep]

        for label in labels:
            RangeActivator.activate(label)
        return True

    def vefrify_ice_sku(self, ice_sku):
        """Verify long ice SKU of the label

        Args:
            ice_sku (str): 'xxxx-xxx-xxxxxx-xxxx-xxxxxx-xx-xxx-xxxxx'
            En el nuevo codigod debe tener e digitos en la seguda posicion
        https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/7578a9e9-32f4-4dbf-bd12-c0ec688ea9a2/FICHA+T%C9CNICA+ANEXO+ICE.pdf
        https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/7510a56f-d397-4188-99b5-bd68af19c10e/CATALOGO_ANEXO_ICE.xls

        xxxx -> Codigo impuesto 4 caracteres
        xxx -> Clasificacion 3 caracteres codigo ICE ejem Vino
        xxxxxx -> Marca 6 caracteres ejem: Henkell Rose
        xxx -> Presentacion 3 caracteres ejem: Botella de Vidrio (013)
        xxxxxx -> Capacidad 6 caracteres ejem: 1500 (001500)
        xx -> Unidad de Medida 2 caracteres ejem: 66 - para ml
        xxx -> Codigo de pais ejem: 593 -> Ecuador
        xxxxxx -> Grados alcoholicos ver tabla de grados alcoholicos
        """
        spected_long_ice_sku = [4, 3, 6, 3, 6, 2, 3, 6]
        ice_sku_parts = ice_sku.split('-')
        ice_valid = ''

        if len(spected_long_ice_sku) != len(ice_sku_parts):
            loggin('e', 'Longitud de ICE SKU incorrecta')
            return False

        for i, sku in enumerate(ice_sku_parts):
            if i == 1:
                sku = '0' + sku

            if len(sku) != spected_long_ice_sku[i]:
                loggin('e', 'Longitud de ICE SKU incorrecta')
                return False
            ice_valid += sku
        import ipdb; ipdb.set_trace()
        loggin('i', 'Logitudes ICE SKU correcto')
        return ice_valid
