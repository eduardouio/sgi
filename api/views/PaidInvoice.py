from paids.models.PaidInvoice import PaidInvoice
from lib_src.serializers import PaidInvoiceSerializer
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView
)

class PaidInvoiceCreateView(CreateAPIView):
    queryset = PaidInvoice.objects.all()
    serializer_class = PaidInvoiceSerializer


class PaidInvoiceDeleteView(DestroyAPIView):
    queryset = PaidInvoice.objects.all()
    serializer_class = PaidInvoiceSerializer


class PaidInvoiceDetailView(RetrieveAPIView):
    queryset = PaidInvoice.objects.all()
    serializer_class = PaidInvoiceSerializer


class PaidInvoiceUpdateView(UpdateAPIView):
    queryset = PaidInvoice.objects.all()
    serializer_class = PaidInvoiceSerializer
