from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView

from filemanager.forms import FileUploadModelForm
from filemanager.models import FileManager
from lib_src import get_host
from logs.app_log import loggin
from orders.models import Order
from partials.models import Partial


class UploadFileView(LoginRequiredMixin, FormView):
    form_class = FileUploadModelForm
    template_name = 'filemanager/frm_subir_archivos.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)        
        orders = []
        for order in Order.get_all():
            partials = []

            orders.append({
                'order' : order.nro_pedido,
                'partials' : partials,
            })




        context['data'] = {
            'title_page':'Subir Archivos',
            'host': get_host(request),
            }
        return self.render_to_response(context)
