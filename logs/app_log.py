import os
from datetime import datetime 
path = os.path.dirname(os.path.abspath(__file__)) + '/log.log'


def loggin(type_log , message):
    '''
    types_message = 'e':'ERROR' | 's':'SUCCESS' | 'w':'WARNING'
    message = log message
    '''
    types_message = {'e':'ERROR','s':'SUCCESS','w':'WARNING'}   

    log_file = open(path,'a')
    log_file.write('[{type_log}] [{date_time}] {message} \n'.format(type_log=types_message[type_log],date_time=datetime.now(),message=message))
    log_file.close()