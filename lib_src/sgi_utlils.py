from logs.app_log import loggin
from django.conf import settings
from django.db import connection

def get_host(request):
    '''
    Obtiene la direccion con la que el usuario se conecta al servidor
    '''
    loggin('i', 'Obteniendo ip del server') 
    return settings.EMPRESA['url_app']


def run_query(query):
    loggin('i',  'ejecutando sql a la base')
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = tuple_to_dict(cursor)
    
    return result

def tuple_to_dict(cursor):
    """Retorna el valor de las tuplas como diccionario
    """
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]