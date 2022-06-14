import json

import requests

from labels.lib_src import LoginSafeTrack
from logs.app_log import loggin
from sgi.settings import EMPRESA


class ValidateBatchSafeTrack(LoginSafeTrack):
    """
    Verificamos que el batch sea valido
    """
    def __init__(self):
        self.url = EMPRESA['safetrack']['url_validate_range']
        super().__init__()

    def validate(self, batch):
        loggin('i', 'Validando Lote de etiquetas')
        batch_data = {
            "status": -1,
            "agregationCode": batch
        }
        response = requests.post(
            self.url,
            data=json.dumps(batch_data),
            headers=self.my_headers
        )

        if len(response.json()) == 0:
            return False
        data = response.json()

        return {
            'batch': batch,
            'first_tag': data[0]['uniquemark'],
            'last_tag': data[-1]['uniquemark'],
            'quantity': len(response.json()),
            'response': response,
        }
