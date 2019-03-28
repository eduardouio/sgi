from django.views.generic import TemplateView

from filemanager.forms import FileUploadModelForm
from filemanager.models import FileManager
from logs.app_log import loggin
from partials.models import Partial
from lib_src import get_host

class UploadFileView(TemplateView):
    form_class = FileUploadModelForm
    template_name = 'filemanager/frm_subir_archivos.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page':'Subir Archivos',
            'host': get_host(request)
            }
        return self.render_to_response(context)

    def post(self,request, *args, **kwargs):
        pass