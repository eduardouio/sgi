""" This is show errros views from http Request
"""

from django.shortcuts import render


def error_404(request, exception):
    data = {
        'data': {
            'title_page': 'Error 404',
            'request': request,
        }
    }
    return render(request, 'errors/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'errors/500.html', data)
