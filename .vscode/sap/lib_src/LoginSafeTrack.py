import json

import requests
from logs.app_log import loggin
from sgi.settings import EMPRESA


class LoginSafeTrack():
    def __init__(self):
        loggin('i', 'Obteniendo el ultimo jwt ')
        self.token = self.get_token()
        self.my_headers = {
            'Authorization': 'Bearer ' + self.token['token'],
            'Host': 'bdo.safetrack.cloud',
            'content-type': 'application/json',
        }
        self.status_service = self.token['status_service']

    def get_token(self):
        loggin('i', 'Renovando JWT')
        safe_track_user = EMPRESA['safetrack']['login_data']
        url_login = EMPRESA['safetrack']['url_login']
        response = requests.post(
            url_login,
            data=safe_track_user,
        )

        if response.status_code != 200:
            loggin('e', 'Error al obtener el token de safetrack {}'.format(
                response.text)
            )
            return({
                'status_code': response.status_code,
                'error': json.loads(response.text),
                'status_service': False,
                'error_message': ''
            })

        loggin('i', 'Token obtenido de safetrack')
        return({
            'token': response.json()['access_token'],
            'sub': EMPRESA['safetrack']['sub'],
            'response': response.json(),
            'status_code': response.status_code,
            'status_service': True,
            'error_message': '',
        })
