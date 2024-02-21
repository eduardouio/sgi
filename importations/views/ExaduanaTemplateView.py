from django.views.generic import TemplateView


# importaciones/exaduana/<nro-pedido>/<id-parcial>/
class ExaduanaTemplateView(TemplateView):
    template_name = 'importations/exaduana.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = {
            'title_page': 'Exaduana pedido',
        }

        return self.render_to_response(context)
