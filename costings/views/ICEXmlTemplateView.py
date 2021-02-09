from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from logs.app_log import loggin
from costings.lib_src import IceSriXml
from django.http import HttpResponse
import io


# costos/ice-xml/
class ICEXmlTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'costings/ice-xml.html'

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
        sales = request.POST['ventas']
        sales = sales.replace(',', '')

        returns = request.POST['devoluciones']
        returns = returns.replace(',', '')

        importations = request.POST['importaciones']

        ice_XMl = IceSriXml()
        ice_XMl.set_data(
            sales=sales,
            returns=returns,
            importations=importations,
            year=request.POST['year'],
            month=request.POST['month'],
        )

        ice_XMl.gerate_report()
        report = ice_XMl.get_xml()
        f = io.StringIO(report)

        return HttpResponse(f, content_type="application/xml")
