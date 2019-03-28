from logs.app_log import loggin

def get_host(request):
    '''
    Obtiene la direccion con la que el usuario se conecta al servidor    
    '''

    host = 'http://179.49.60.158:5001'

    try:
        return request.META['HTTP_HOST']
    except KeyError:
        return host


def get_file_from_url(url, type):
    '''[summary]
    
    Arguments:
        url {[type]} -- [description]
        type {[type]} -- [description]
    '''

