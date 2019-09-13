from logs.app_log import loggin
from django.conf import settings

def get_host(request):
    '''
    Obtiene la direccion con la que el usuario se conecta al servidor
    '''
    loggin('i', 'Obteniendo ip del server')
    # indica si loa configuracion queda en modo red interna
    is_local = False
    try:
        return 'http://{}/'.format(request.META['HTTP_HOST'])
    except KeyError:
        loggin('e', 'No se encuentra la variable de Host en el requets')
        if settings.DATABASES['default']['NAME'] == 'cordovezApp':
            return 'http://192.168.0.198:5001/' if is_local else 'http://179.49.60.158:5001/'
        
        if settings.DATABASES['default']['NAME'] == 'imnacApp':
            return 'http://192.168.0.198:5002/' if is_local else 'http://179.49.60.158:5002/'

        if settings.DATABASES['default']['NAME'] == 'vidApp':
            return 'http://192.168.0.198:5003/' if is_local else 'http://179.49.60.158:5003/'
