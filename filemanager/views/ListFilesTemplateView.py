from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from lib_src import get_host


class ListFilesTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "filemanager/lista_archivos.html"


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args,**kwargs)
        context['data'] = {
            'title_page' : 'Lista Archivos SGI',
            'host' : get_host(request),
            'list_files' : ''
        }
        return self.render_to_response(context)
        