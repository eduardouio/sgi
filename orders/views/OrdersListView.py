from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import ListView

from lib_src.sgi_utlils import get_host
from orders.models import Order


class OrdersListView(LoginRequiredMixin, ListView):
    model = Order
    login_url = '/admin/'
    template_name = 'orders/lista_pedidos.html'
    allow_empty = True

    def get_context_data(self, *args, object_list=None, **kwargs):
        """Obteniendo la lista de pedidos"""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(
                queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'orders_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'orders_list': queryset
            }

        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        context.update(data = {
            'title_page' : 'Listado de pedidos',
            'host' : get_host(self.request)
        })
        
        return super().get_context_data(**context)