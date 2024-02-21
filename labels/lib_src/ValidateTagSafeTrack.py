from sgi.settings import EMPRESA
from logs.app_log import loggin
import requests
import json


class ValidateTagSafeTrack():
    """
    Valida que una etiqueta sea valida
    https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{id_tag}/{bussines_id}/{ice_sku}/

    Args:
        LoginSafeTrack (obj): autoinicia la secion al instanaciar la clase
    """

    def __init__(self, login):
        loggin('i', 'Iniciando validacion de etiqueta')
        self.url = EMPRESA['safetrack']['url_validate_tag']
        self.login = login
        super().__init__()

    def validate(self, id_tag, ice_sku):
        """Verifica la validez de una etiqueta"""
        loggin('i', 'Validanto etiquetas solas {}'.format(id_tag))
        result = {
            'tag': id_tag,
            'status_service': None,
            'is_valid': False,
            'status_code': 0,
            'error_message': '',
            'response': None,
            'is_active': False,
        }

        url = self.url.format(id_tag, ice_sku)
        response = requests.get(url, headers=self.login.my_headers)
        result['status_code'] = result['status_service'] = response.status_code
        result['response'] = response.text
        loggin('i', response.text)

        if response.status_code == 200:
            loggin('s', 'Etiqueta valida {}'.format(id_tag))
            result['is_valid'] = True
            return result
        else:
            response_dict = json.loads(response.text)
            if response_dict.get('status'):
                loggin('e', 'El servidor rechaza la peticion')
                result['error_message'] = 'Exceso de Consultas Intente Luego'
                return result

            if response_dict.get('description') == 'Unique mark has status 2':
                result['is_valid'] = True
                result['is_active'] = True
                result['error_message'] = 'Etiqueta Activada'
                return result

            result['error_message'] = response_dict['description']

            return result
