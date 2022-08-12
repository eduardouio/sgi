import json

import requests

from logs.app_log import loggin
from sgi.settings import EMPRESA


class ValidateBatchSafeTrack():
    """
    Verificamos que el batch sea valido
    """

    def __init__(self, login):
        self.url = EMPRESA['safetrack']['url_validate_range']
        self.login = login

    def validate(self, batch):
        loggin('i', 'Validando Lote de etiquetas')
        batch_data = {
            "status": -1,
            "agregationCode": batch
        }

        response = requests.post(
            self.url,
            data=json.dumps(batch_data),
            headers=self.login.my_headers
        )

        if len(response.json()) == 0:
            loggin('e', 'Error al Validar Lote de etiquetas')
            return {
                'batch': None,
                'first_tag': None,
                'last_tag': None,
                'quantity': None,
                'response': None,
                'status': 500
            }

        data = response.json()
        loggin('i', 'Lote {} de etiquetas validado'.format(batch))
        return {
            'batch': batch,
            'first_tag': data[0]['uniquemark'],
            'last_tag': data[-1]['uniquemark'],
            'quantity': len(response.json()),
            'response': response,
            'status': response.status_code
        }
