from django import forms
from django.views.generic import FormView
from orders.models import Order


class FormUpload(forms.Form):
    nro_pedido = forms.CharField(label='Nro Pedido', max_length=6)
    url_dai = forms.URLField(label='URL DAI')
    url_liquidacion = forms.URLField(label="URL LIQUIDACION")


class FileUploadFormView(FormView):
    form_class = FormUpload
    template_name = 'importations/subir-dai-liquidacion.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['data'] = {}
        return self.render_to_response(context)