from django.views.generic import FormView

from filemanager.forms import FileUploadModelForm
from filemanager.models import FileManager
from logs.app_log import loggin
from partials.models import Partial


class UploadFileFormView(FormView):
    form_class = FileUploadModelForm
    template_name = 'filemanager/frm_subir_archivos.html'

    def get(self, request, id_partial, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        partial = Partial.get_by_id(id_partial)
        if partial is None:
            loggin('e', 'No se puede subir archivos si el registro no existe')

        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        print('Estamos recibiendo por post')