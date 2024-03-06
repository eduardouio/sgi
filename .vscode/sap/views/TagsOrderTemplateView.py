from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from lib_src.sgi_utlils import get_host
from logs.app_log import loggin
from orders.models import Order, OrderInvoiceDetail, OrderInvoice
from lib_src.serializers import (
    OrderSerializer,
    OrderInvoiceSerializer,
    OrderInvoiceDetailSerializer,
    SupplierSerializer,
)


# /importaciones/etiquetas/detalle/<nro_order>/
class TagsOrderTemplateView(LoginRequiredMixin, TemplateView):

    template_name = 'labels/etiquetas-pedido.html'

    def get(self, request, nro_order, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        order = Order.get_by_order(nro_order)
        order_data = self.get_complete_order_info(nro_order)

        if order is None:
            loggin('e', 'No se puede listar los productos del pedido')
            return HttpResponseRedirect(
                '/importaciones/pedidos-etiquetas/?show_error=1'
            )

        context['data'] = {
            'title_page': 'Detalle de etiquetas Pedido ' + nro_order,
            'host': get_host(request),
            'order': order,
            'order_data': order_data,
        }

        context['data']['serialized_data'] = self.serialize_data(
            context['data']
        )

        return self.render_to_response(context)

    def get_complete_order_info(self, nro_order):
        data = {
            'order_invoice': None,
            'oder_invoice_details': None,
            'supplier': None,
            'boxes': 0,
            'units': 0,
        }
        order_invoice = OrderInvoice.get_by_order(nro_order)

        if order_invoice is None:
            return HttpResponseRedirect(
                '/importaciones/pedidos-etiquetas/?show_error=1'
            )
        data['order_invoice'] = order_invoice
        data['order_invoice_details'] = OrderInvoiceDetail.get_by_order(
            nro_order
        )

        data['supplier'] = order_invoice.identificacion_proveedor

        for detail in data['order_invoice_details']:
            data['boxes'] += detail.nro_cajas
            data['units'] += detail.unidades

        return data

    def serialize_data(self, data):
        base = data['order_data']
        supplier_serializer = SupplierSerializer(base['supplier'])
        order_serializer = OrderSerializer(data['order'])
        invoice_serializer = OrderInvoiceSerializer(base['order_invoice'])
        invoice_detail_serializer = OrderInvoiceDetailSerializer(
            base['order_invoice_details'], many=True
        )

        return {
            'order': order_serializer.data,
            'order_invoice': invoice_serializer.data,
            'oder_invoice_details': invoice_detail_serializer.data,
            'supplier': supplier_serializer.data,
        }
