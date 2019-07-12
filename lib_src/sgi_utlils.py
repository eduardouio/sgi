from logs.app_log import loggin

def get_host(request):
    '''
    Obtiene la direccion con la que el usuario se conecta al servidor
    '''

    host = 'http://179.49.60.158:5001'

    try:
        return 'http://{}'.format(request.META['HTTP_HOST'])
    except KeyError:
        return host
