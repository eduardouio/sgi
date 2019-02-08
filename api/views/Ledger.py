from costings.models import Ledger
from lib_src.serializers import LedgerSerializer
from rest_framework.generics import (
                        CreateAPIView, 
                        UpdateAPIView, 
                        DestroyAPIView, 
                        RetrieveAPIView,
                        )

class LedgerCreateView(CreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class LedgerDeleteView(DestroyAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class LedgerDetailView(RetrieveAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class LedgerUpdateView(UpdateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer