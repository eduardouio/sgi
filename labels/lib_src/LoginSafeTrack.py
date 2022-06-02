import requests
from logs.app_log import loggin
from sgi.settings import EMPRESA


class LoginSafeTrack():
    """
    Obtiene el token de acceso a SafeTrack
    y la información del usuario
    """
    def get_jwt(self):
        loggin('i', 'Accediendo al servicio de SafeTrack')
        response = requests.post(
            EMPRESA['safe_track']['url_login'],
            data=EMPRESA['safe_track']['data_login']
        )

        import ipdb;ipdb.set_trace()
        
        return response.json()
