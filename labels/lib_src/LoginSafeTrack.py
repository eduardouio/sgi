from cmath import log
from email import header
import requests
from labels.models import Label
from logs.app_log import loggin
from sgi.settings import EMPRESA


class LoginSafeTrack():
    def __init__(self):
        loggin('i', 'Obteniendo el ultimo jwt ')
        self.last_jwt = None

    def get_jwt(self):
        last_labels = Label.get_last_jwt()
        if self.check_jwt(last_labels.jwt):
            loggin('i', 'Token Válido')
            return last_labels.jwt

        loggin('i', 'Token Inválido, solicitamos un nuevo')
        safe_track_user = EMPRESA['safetrack']['login_data']
        url_login = EMPRESA['safetrack']['url_login']

        response = requests.post(
            url_login,
            data=safe_track_user
        )

        return response.json()

    def check_jwt(self, jwt):
        import ipdb; ipdb.set_trace()
        loggin('t', 'Comptando el ultimo jwt')
        