import json

import requests
from labels.lib_src import LoginSafeTrack
from logs.app_log import loggin
from sgi.settings import EMPRESA


class ValidateRangeSafeTrack(LoginSafeTrack):
    """
    Valida que una etiqueta sea valida
    https://bdo.safetrack.cloud/api/v1/unique-mark/validate-activate/{id_tag}/{bussines_id}/{ice_sku}/

    Args:
        LoginSafeTrack (obj): autoinicia la secion al instanaciar la clase
    """

    def __init__(self):
        loggin('i', 'Iniciando validacion de rango')
        self.url = EMPRESA['safetrack']['url_validate_range']
        super().__init__()

    def validateRange(self, first_tag, last_tag):
        """
        Verifica que el rango de etiquetas sea valido, 
        verifica el orden del rango

        Args:
            fisrtTag (str): Etiqueta incial
            lastTag (str): Etiqueta Final
        """
        range_data = {
            "uniqueMark": first_tag,
            "uniqueMarkEnd": last_tag,
            "businessId": "",
            "status": -1
        }

        response = requests.post(
            self.url,
            data=json.dumps(range_data),
            headers=self.my_headers
        )

        return response
