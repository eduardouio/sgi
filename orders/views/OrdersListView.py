# django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# sgi
from lib_src.sgi_utlils import get_host, run_query
from orders.models import Order
from partials.models import Partial
from logs.app_log import loggin


# /pedidos/listar/
class OrdersListView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/lista_pedidos.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Mostrando pedidos por liquidar')

        orders_list = None
        search = False

        if request.GET:
            orders_list = self.search_order(request.GET['q'])
            search = True
        else:
            orders_list = self.get_orders_list()

        context = self.get_context_data(**kwargs)
        context['data'] = {
            'search': search,
            'title_page': 'Pedidos por liquidar',
            'request': request,
            'host': get_host(request),
            'orders_list': orders_list,
        }

        return self.render_to_response(context)

    def get_orders_list(self):
        """Obtiene la lista de pedidos llegados a Almagro
        los pendientes de llegada del puerto
        """
        orders_r10 = """
            select o.nro_pedido, s.nombre, o.nro_liquidacion, o.nro_refrendo, o.fecha_liquidacion, o.regimen, '1' as id_parcial, o.fecha_llegada_cliente 
            from pedido as o
            left join pedido_factura as pf on (pf.nro_pedido = o.nro_pedido)
            left join proveedor as s on (s.identificacion_proveedor = pf.identificacion_proveedor)
            where 
            o.regimen = 10
            AND
            o.bg_isliquidated = 1 and (o.bg_isclosed = 0 OR o.bg_isclosed IS NULL )
        """
        orders_r70 = """
           select p.nro_pedido, s.nombre, p.nro_liquidacion, fi.nro_refrendo, 
            p.fecha_liquidacion, o.regimen, p.id_parcial, p.fecha_llegada_cliente 
            from parcial as p
            left join factura_informativa as fi on (fi.id_parcial = p.id_parcial)
            left join pedido as o on (o.nro_pedido = p.nro_pedido)
            left join pedido_factura as pf on (pf.nro_pedido = o.nro_pedido)
            left join proveedor as s on (s.identificacion_proveedor = pf.identificacion_proveedor)
            where 
            p.bg_isliquidated =1 and (p.bg_isclosed = 0 or p.bg_isclosed IS NULL )
        """
        results = run_query(orders_r10)
        results_almagro = run_query(orders_r70)
        for item in results_almagro:
            item['partial'] = Partial.objects.get(pk=item['id_parcial'])
        return (results + results_almagro)

    def search_order(self, query):
        query = query.replace('/','-')
        limit = 10 if (query == '') else 50
        orders = """
            select o.nro_pedido, s.nombre, o.nro_liquidacion, o.nro_refrendo, o.fecha_liquidacion, o.regimen, '1' as id_parcial, o.fecha_llegada_cliente 
            from pedido as o
            left join pedido_factura as pf on (pf.nro_pedido = o.nro_pedido)
            left join proveedor as s on (s.identificacion_proveedor = pf.identificacion_proveedor)
            where 
            o.nro_pedido = '{}'
            or o.nro_pedido like '{}%'
            or o.nro_pedido like '%{}%'
            or o.nro_pedido like '%{}'
            limit {}
        """.format(query,query,query,query, limit)
        return run_query(orders)