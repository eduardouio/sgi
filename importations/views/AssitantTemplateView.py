from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AssistantTemplateView(LoginRequiredMixin,TemplateView):
    login_url = '/admin/'
    template_name = 'importations/asistente.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = {
        'title_page' : 'Asistente',
        'host' : 'Eduardo Villota',
        }
        return context
    
