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
        self.check_reverse = False
        super().__init__()

    def validate(self, first_tag, last_tag, quantity_spected):
        """
        Verifica que el rango de etiquetas sea valido, 
        verifica el orden del rango

        Args:
            fisrtTag (str): Etiqueta incial
            lastTag (str): Etiqueta Final
        """
        loggin('i', 'Llama a la funcion validate')
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
        quantity = len(response.json())
        result = {
            'first_tag': first_tag,
            'last_tag': last_tag,
            'quantity': quantity,
            'status_code': response.status_code,
            'response': response,
            'cheked_reverse': self.check_reverse,
            'concordance': False,
            'difference': quantity - quantity_spected,
        }

        if result['difference'] == 0:
            result['concordance'] = True
        else:
            result['concordance'] = False

        if quantity == 0 and not self.check_reverse:
            loggin('e', 'No se encontraron etiquetas, revertimos orden rango')
            self.check_reverse = True
            result['fist_tag'] = last_tag
            result['last_tag'] = first_tag
            return self.validate(last_tag, first_tag, quantity_spected)

        return result
