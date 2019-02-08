from lib_src.serializers import OrderInvoiceSerializer
from orders.models import OrderInvoice
from rest_framework.generics import (
                                CreateAPIView,
                                UpdateAPIView,
                                DestroyAPIView,
                                RetrieveAPIView,
                    )

class OrderInvoiceCreateView(CreateAPIView):
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer


class OrderInvoiceDeleteView(DestroyAPIView):
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer


class OrderInvoiceDetailView(RetrieveAPIView):
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer


class OrderInvoiceUpdateView(UpdateAPIView):
    queryset = OrderInvoice.objects.all()
    serializer_class = OrderInvoiceSerializer