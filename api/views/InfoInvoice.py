from lib_src.serializers import InfoInvoiceSerializer
from rest_framework import generics
from partials.models.InfoInvoice import InfoInvoice


class InfoInvoiceCreateView(generics.CreateAPIView):
    queryset = InfoInvoice.objects.all()
    serializer_class = InfoInvoiceSerializer


class InfoInvoiceDeleteView(generics.DestroyAPIView):
    queryset = InfoInvoice.objects.all()
    serializer_class = InfoInvoiceSerializer


class InfoInvoiceDetailView(generics.RetrieveAPIView):
    queryset = InfoInvoice.objects.all()
    serializer_class = InfoInvoiceSerializer


class InfoInvoiceUpdateView(generics.UpdateAPIView):
    queryset = InfoInvoice.objects.all()
    serializer_class = InfoInvoiceSerializer

