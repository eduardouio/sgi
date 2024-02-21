"""Completa la información del perfil de la empresa"""
from sgi.settings import EMPRESA


class DataCompletionMiddleware(object):
    """
    Insert into http resquest data from current company
    """

    def __init__(self, get_reponse):
        self.get_response = get_reponse

    def __call__(self, request):
        """
        This method run before call the django view
        """
        if not request.user.is_anonymous:
            request.enterprise = EMPRESA

        response = self.get_response(request)

        return response
