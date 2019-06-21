import os
from datetime import datetime 
path = os.path.dirname(os.path.abspath(__file__)) + '/log.log'

def loggin(type_log , message, request=None):
    '''
    loggin message in text file
    Args
        types_message (char): 
                            e -> ERROR
                            s -> SUCCESS
                            w -> WARNING
                            i -> INFO
                            t -> TEST
        message (string): log message
        request (django-request): session data for get current user info
    '''
    types_message = {
        'e':' error ',
        's':'success',
        'w':'warning',
        'i':' info  ',
        't':'testing'
        }   
    user_id = 0
    user_name = ''
    user_email = ''
    
    if request is not None:
        user_id = request.user.id
        user_name = request.user
        user_email = request.user.email

    log_file = open(path,'a')
    log_file.write(
        #'[{type_log}][{date_time}][uid:{user_id}{user_name}{user_email}]    {message} \n'
        '[{type_log}] {message} \n' #para depurar
            .format(
                type_log=types_message[type_log],
                date_time=datetime.now(),
                message=message,
                user_id=user_id,
                user_name = user_name,
                user_email = user_email,
            )
    )
    log_file.close()