import os
from datetime import datetime 
path = os.path.dirname(os.path.abspath(__file__)) + '/log.log'

def loggin(type_log , message):
    '''
    loggin message in text file
    Args
        types_message (char): 
                            e -> ERROR
                            s -> SUCCESS
                            w -> WARNING
                            i -> INFO
        message (string): log message
        request (django-request): session data for get current user info
    '''
    types_message = {
        'e':'ERROR',
        's':'SUCCESS',
        'w':'WARNING',
        'i':'INFO',
        }   
    log_file = open(path,'a')
    log_file.write(
        '[{type_log}] [{date_time}] {message} \n'.format(
                                            type_log=types_message[type_log],
                                            date_time=datetime.now(),
                                            message=message
                                        )
        )
    log_file.close()