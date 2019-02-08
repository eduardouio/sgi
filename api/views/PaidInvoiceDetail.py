from paids.models import PaidInvoiceDetail
from lib_src.serializers import PaidInvoiceDetailSerializer
from rest_framework.generics import (
                                    RetrieveAPIView, 
                                    UpdateAPIView, 
                                    DestroyAPIView, 
                                    CreateAPIView
                                    )

class PaidInvoiceDetailCreateView(CreateAPIView):
    queryset = PaidInvoiceDetail.objects.all()
    serializer_class = PaidInvoiceDetailSerializer


class PaidInvoiceDetailDeleteView(DestroyAPIView):
    queryset = PaidInvoiceDetail.objects.all()
    serializer_class = PaidInvoiceDetailSerializer


class PaidInvoiceDetailDetailView(RetrieveAPIView):    
    queryset = PaidInvoiceDetail.objects.all()
    serializer_class = PaidInvoiceDetailSerializer


class PaidInvoiceDetailUpdateView(UpdateAPIView):
    queryset = PaidInvoiceDetail.objects.all()
    serializer_class = PaidInvoiceDetailSerializer
