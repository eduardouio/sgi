import io

from costings.lib_src import IceSriXml
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from logs.app_log import loggin
from costings.forms import FormICEXML
from django.http import HttpResponse


# costos/ice-xml/
class ICEXmlFormView(LoginRequiredMixin, FormView):
    template_name = 'costings/ice-xml.html'
    form_class = FormICEXML
    success_url = 'costings/ice-xml/result/'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Mostrando formulario para reporte ICE')
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Generador XML ICE',
            'view_form': True,
        }

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        loggin('i', 'Iniciando proceso de generacion de reporte')
        form = FormICEXML(self.request.POST)
        if form.is_valid():
            my_report = IceSriXml()
            sales = my_report.clean_data(form.cleaned_data['sales'])
            devs = my_report.clean_data(form.cleaned_data['devs'])
            importations = my_report.clean_imports(form.cleaned_data['importations'])
            report = my_report.get_report(
                form.cleaned_data['year'],
                form.cleaned_data['month'],
                sales,
                devs,
                importations
            )

            file_name = (
                'ICE_' +
                str(form.cleaned_data['year']) +
                '_' +
                str(form.cleaned_data['month']) +
                request.enterprise['empresa'].upper() +
                '.xml'
            )

            response = HttpResponse(
                my_report.get_xml_report(report),
                content_type='application/xml'
            )

            content_disposition = 'attachment; filename=' + file_name
            response['Content-Disposition'] = content_disposition

            return response

        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['data'] = {
            'title_page': 'Generador XML ICE',
            'view_form': True,
        }
        return self.render_to_response(context)
