import csv
from io import StringIO
import json

from almagro.forms import FormAlmagro
from almagro.lib_src import ImportAlmagro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.core.serializers.json import DjangoJSONEncoder
from logs.app_log import loggin


class AlmagroImportTV(LoginRequiredMixin, FormView):
    template_name = 'almagro/importar.html'
    form_class = FormAlmagro
    success_url = '/almagro/analisis/'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        invalid = False

        if request.session.get('almagro'):
            del(request.session['almagro'])

        if request.GET.get('invalid'):
            invalid = True
        context['data'] = {
            'title_page': 'Importar Almagro',
            'invalid': invalid,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        data = form.files['reporte'].read()
        data = data.decode('ISO-8859-1')
        reader = csv.reader(StringIO(data))
        almagro_data = [row for row in reader]

        if almagro_data.__len__() > 0:
            loggin('i', 'El archivo no esta vacio ')
            almagro = ImportAlmagro().set_data(almagro_data)
            request.session['almagro'] = json.dumps(
                almagro,
                cls=DjangoJSONEncoder
            )
            return self.form_valid(form)
        else:
            loggin('e', 'El archivo es invalido')
            return self.form_invalid(form)
