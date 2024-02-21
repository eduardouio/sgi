from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

def environment(**options):
    '''
        Enlace django templates con jinja2
    '''
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': reverse,
    })
    return env