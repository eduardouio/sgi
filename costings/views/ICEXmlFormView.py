import io

from costings.lib_src import IceSriXml
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import FormView
from logs.app_log import loggin
from costings.forms import FormICEXML


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
        form = FormICEXML(self.request)

        if self.form_valid(form=form):
            request.sesion['data'] = self.check_data(request)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def check_data(self, sh_importations):

        book = xlrd.open_workbook(
            file_contents=input_file.read(),
            encoding_override='iso-8859-1'
        )  

        # definir los valores de los usuarios
        # sh_sales = book.sheet_by_name('ventas')
        # sh_returns = book.sheet_by_name('devoluciones')

        importations = self.check_importations(
            book.sheet_by_name('importaciones')
        )

        # definimos los ice que necesitamos para el reporte
        idx_import = {
            'cod_ice': 0,
            'date': 0,
            'quantity': 0,
            'referendo_sequential': 0,
            'referendo_year': 0,
            'referendo_reg': 0,
            'referendo_district': 0,
        } 

        matriz = []
        # quitamos las dos filas de la cabecera
        for idl in range(2, sh_importations.nrows):
            matriz.append(sh_importations.row_values(idl))
