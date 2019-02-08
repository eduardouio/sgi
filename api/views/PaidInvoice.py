from paids.models import PaidInvoice
from lib_src.serializers import PaidInvoiceSerializer
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response


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



class CompletePaidView(APIView):
    def get(self, request, id_paid, format=None):
        complete_paid_info = CompletePaidinfo(id_paid)
        data =  complete_paid_info.get_data(serialized=True)
        return Response(data)