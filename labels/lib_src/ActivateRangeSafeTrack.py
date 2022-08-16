import json

import requests
from datetime import datetime
from logs.app_log import loggin
from sgi.settings import EMPRESA
from labels.lib_src import ValidateRangeSafeTrack, SignMessageSafeTrack


class ActivateRangeSafeTrack():

    def __init__(self, login):
        loggin('i', 'iniciamos la clase enccaragada de activar rango')
        self.url = EMPRESA['safetrack']['url_activate_range']
        self.address = EMPRESA['safetrack']['wallet']['networkAddress']
        self.network = EMPRESA['safetrack']['wallet']['network']
        self.login = login
        self.label = None
        self.is_valid = False
        self.is_signed = False

    def try_activate(self, label, ignore_diferences=False):
        loggin('i', 'Activando rango de etiquetas, validando etiquetas')
        self.label = label
        self.label.message_status = 'Iniciando Activacion de Rango;'
        self.is_valid = self.__validate_label(ignore_diferences)
        self.is_signed = self.__sign()
        self.__send_activate_request()
        self.label.save()
        return self.label

    def __validate_label(self, ignore_diferences=False):
        self.label.validated_date = datetime.now()
        validateRange = ValidateRangeSafeTrack(self.login)
        result = validateRange.validate(
            self.label.initial_range,
            self.label.end_range,
            self.label.quantity
        )
        self.label.last_jwt = result['response']
        if ignore_diferences and not result['concordance']:
            loggin('i', 'Ignorando diferencias')
            self.label.bg_status = 'V'
            self.label.message_status += (
                'Rango Validado igonrando diferencias diff:{} concordance:{};'
            ).format(result['difference'], result['concordance'])
            return True

        if result['concordance']:
            loggin('i', 'Rango validado correctamente')
            self.label.bg_status = 'V'
            self.label.message_status += 'Rango Validado correctamente;'
            return True

        self.label.bg_status = 'E'
        self.label.response = result['response'].text
        self.label.message_status += (
            'Rango invalido No coincide las cantiades,'
            ' revise response diff:{} concordance:{};'
            ).format(
                result['difference'], str(result['concordance'])
            )
        del(result['response'])
        self.label.message_status += json.dumps(result) + ';'
        return False

    def __send_activate_request(self):
        if not self.is_valid or not self.is_signed:
            loggin('i', 'No se puede activar el rango no valido o no firmado')
            return False

        self.label.activated_date = datetime.now()
        self.label.bg_status = 'S'
        self.label.message_status += 'Enviando Request para activar rango;'
        loggin('i', 'Enviando Request para activar rango')
        data = {
            "address": self.address,
            "network": self.network,
            "msg": self.label.message,
            "signature": self.label.sign
        }
        response = requests.put(
            self.url,
            data=json.dumps(data),
            headers=self.login.my_headers
        )

        if response.status_code == 400:
            self.label.bg_status = 'R'
            self.label.message_status += (
                'httpCode:400 Ocurrio un error en Serivicio BDO al activar el rango {};'
            ).format(self.label)
            self.label.response = response.text
            return False

        if response.status_code == 500:
            self.label.bg_status = 'E'
            self.label.message_status += (
                'httpCode:500 Error interno de Servidor de BDO, '
                'se pasa el rango a Error;'
            ).format()
            self.label.response = response.text
            return False

        loggin('i', 'Rango Activado correctamente')
        self.label.bg_status = 'A'
        self.label.message_status += 'Rango Activado;'
        self.label.response = response.text
        return True

    def __sign(self):
        if not self.is_valid:
            return False

        loggin('i', 'Firmando mensaje Rango Valido')
        self.label.signed_date = datetime.now()
        ice_sku = self.label.id_factura_detalle.cod_contable.cod_ice
        valid_ice_sku = self.__vefrify_ice_sku(ice_sku)

        if not bool(valid_ice_sku):
            self.label.bg_status = 'E'
            self.label.message_status += (
                'SKU ICE  {} no valido, las logitudes no coinciden;'
                ).format(ice_sku)
            return False

        message = """{"uniqueMarks":[{"uniqueMarkStart":"f_tag","uniqueMarkEnd":"l_tag"}],"iceSku":"ice_sku","businessId":"business_id"}"""
        message = message.replace('f_tag', self.label.initial_range)
        message = message.replace('l_tag', self.label.end_range)
        message = message.replace('ice_sku', valid_ice_sku)
        SignMessage = SignMessageSafeTrack()
        result = SignMessage.sign(message)
        self.label.message = result['message']
        self.label.sign = result['signature']
        self.label.message_status += 'Mensaje Firmado;'
        loggin('i', 'Mensaje Firmado')
        return True

    def __vefrify_ice_sku(self, ice_sku):
        """Verify long ice SKU of the label
        Args:
            ice_sku (str): 'xxxx-xxx-xxxxxx-xxxx-xxxxxx-xx-xxx-xxxxx'
        https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/7578a9e9-32f4-4dbf-bd12-c0ec688ea9a2/FICHA+T%C9CNICA+ANEXO+ICE.pdf
        https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/7510a56f-d397-4188-99b5-bd68af19c10e/CATALOGO_ANEXO_ICE.xls

        """
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
