'''
Procesador de contexto para la obtencion de url base_url
@author        Eduardo Villota <eduardouio7@gmail.com>
@copyright     Copyright (c) 2018,  Equipotel Cia. Ltda
@license      Derechos reservados Equipotel 2018
@link         https://equipotel.com
@since    Version 0.1.
'''

from django.conf import settings

def base_url(request):
    
    return {
             'BASE_URL': settings.BASE_URL,
             #'MEDIA_URL' : scheme + request.get_host() + '/media/',
             #'SITE_IMAGES_URL' : scheme + request.get_host() + '/media/img/'
           }