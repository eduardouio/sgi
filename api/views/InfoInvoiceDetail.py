from rest_framework import generics
from partials.models import InfoInvoiceDetail
from lib_src.serializers import InfoInvoiceDetailSerializer

class InfoInvoiceDetailCreateView(generics.CreateAPIView):
    queryset = InfoInvoiceDetail.objects.all()
    serializer_class = InfoInvoiceDetailSerializer


class InfoInvoiceDetailDeleteView(generics.DestroyAPIView):
    queryset = InfoInvoiceDetail.objects.all()
    serializer_class = InfoInvoiceDetailSerializer


class InfoInvoiceDetailDetailView(generics.RetrieveAPIView):
    queryset = InfoInvoiceDetail.objects.all()
    serializer_class = InfoInvoiceDetailSerializer


class InfoInvoiceDetailUpdateView(generics.UpdateAPIView):
    queryset = InfoInvoiceDetail.objects.all()
    serializer_class = InfoInvoiceDetailSerializer
