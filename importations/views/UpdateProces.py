from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# /importaciones/actualizar-procesos/
class UpdateProcesTV(TemplateView, LoginRequiredMixin):
    template_name = 'importations/actualizar-procesos.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page' : 'Actualizar Procesos'
        }

        return self.render_to_response(context)
