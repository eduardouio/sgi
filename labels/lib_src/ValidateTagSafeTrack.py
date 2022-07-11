from sgi.settings import EMPRESA
from labels.lib_src import LoginSafeTrack
from logs.app_log import loggin
import requests


class ValidateTagSafeTrack(LoginSafeTrack):
    """
    Valida que una etiqueta sea valida
    https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{id_tag}/{bussines_id}/{ice_sku}/

    Args:
        LoginSafeTrack (obj): autoinicia la secion al instanaciar la clase
    """

    def __init__(self):
        loggin('i', 'Iniciando validacion de etiqueta')
        self.url = EMPRESA['safetrack']['url_validate_tag']
        super().__init__()

    def validTag(self, id_tag, ice_sku):
        result = {
            'tag': id_tag,
            'status_service': self.status_service,
            'is_valid': False,
            'status_code': 0,
            'error_message': '',
        }

        if self.status_service is False:
            loggin('e', 'Error al validar la etiqueta')
            return result

        url = self.url.format(id_tag, ice_sku)
        response = requests.get(url, headers=self.my_headers)
        result['status_code'] = response.status_code

        if response.status_code == 200:
            loggin('s', 'Etiqueta valida {}'.format(id_tag))
            result['is_valid'] = response.json()
            return result
        else:
            loggin('e', 'Error al procesar la solicitd {}'.format(id_tag))
            result['error_message'] = response.json()
            return result
