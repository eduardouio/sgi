import json

import requests
from labels.lib_src import LoginSafeTrack
from logs.app_log import loggin
from sgi.settings import EMPRESA


class ActivateRangeSafeTrack(LoginSafeTrack):
    """clase encargada de actvar un rango de etiquetas

    Args:
        ValidateRangeSafeTrack (_type_): _description_
    """

    def __init__(self):
        loggin('i', 'iniciamos la clase enccaragada de activar rango')
        self.url = EMPRESA['safetrack']['url_activate_range']
        self.address = EMPRESA['safetrack']['wallet']['networkAddress']
        self.network = EMPRESA['safetrack']['wallet']['network']
        super().__init__()

    def activate(self, label):
        """Enviamos el request para activar el rango de etiquetas

        Args:
            label (Label): Objeto de la clase Label firmado
        """
        loggin('i', 'Ejecutamos la funcion activate_ranges')
        data = {
            "address": self.address,
            "network": self.network,
            "msg": label.message,
            "signature": label.sign
        }
        label.bg_status = 'S'
        label.message_status += 'Enviando Request para activar rango;'
        label.save()

        response = requests.put(
            self.url,
            data=json.dumps(data),
            headers=self.my_headers
        )

        if response.status_code == 400:
            loggin('i', 'Error al Activar el rango')
            label.bg_status = 'E'
            label.message_status += 'Ocurrio un error al activar el rango;' + response.text + ';'
            label.save()
            return False

        if response.status_code == 500:
            loggin('i', 'En peticion http')
            label.bg_status = 'E'
            label.message_status += 'Ocurrio un error al enviar peticion;' + response.text + ';'
            label.save()

        label.bg_status = 'A'
        label.message_status += 'Rango Activado;' + response.text + ';'
        label.save()
