from django import forms
from django.views.generic import TemplateView
from orders.models import Order


class FileUploadFormView(TemplateView):
    template_name = 'importations/subir-dai-liquidacion.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        print('Se ejectut')
        context['data'] = {}
        return self.render_to_response(context)
