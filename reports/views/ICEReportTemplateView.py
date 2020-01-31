from django.views.generic import TemplateView

#/reportes/ice/<year>/<month>/
class ICEReportTemplateView(TemplateView):
    template_name = 'reports/reporte_ice.html'

    def get(self, response, year, month, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)