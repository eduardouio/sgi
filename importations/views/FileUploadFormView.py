from django import forms
from django.views.generic import TemplateView
from orders.models import Order


class FileUploadFormView(TemplateView):
    template_name = 'importations/subir-dai-liquidacion.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        order = Order()
        context['data'] = {
        	'title_page' : 'Subir Archivos A Parcial',
        	'open_orders' : order.get_open_orders(),
        }
        return self.render_to_response(context)