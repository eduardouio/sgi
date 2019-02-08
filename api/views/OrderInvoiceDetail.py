from orders.models import OrderInvoiceDetail
from lib_src.serializers import OrderInvoiceDetailSerializer
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView
)

class OrderInvoiceDetailCreateView(CreateAPIView):
    queryset = OrderInvoiceDetail.objects.all()
    serializer_class = OrderInvoiceDetailSerializer


class OrderInvoiceDetailDeleteView(DestroyAPIView):
    queryset = OrderInvoiceDetail.objects.all()
    serializer_class = OrderInvoiceDetailSerializer


class OrderInvoiceDetailDetailView(RetrieveAPIView):
    queryset = OrderInvoiceDetail.objects.all()
    serializer_class = OrderInvoiceDetailSerializer
    lookup_field = 'nro_pedido'


class OrderInvoiceDetailUpdateView(UpdateAPIView):
    queryset = OrderInvoiceDetail.objects.all()
    serializer_class = OrderInvoiceDetailSerializer