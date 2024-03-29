from costings.models import Ledger
from lib_src.serializers import LedgerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from logs.app_log import loggin
from rest_framework import status
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


class LedgerExisting(APIView):
    """Verifica la existencia de un mayor"""
    def get(self, requets, nro_order, id_partial):
        loggin('i', 'Recuprando mayor pedido {} parcial {}'.format(nro_order, id_partial))
        my_ledger = Ledger.get_by_order_and_partial(nro_order, id_partial)
        return Response({
            'exist' : 1 if my_ledger else 0, 
            'id_mayor' : my_ledger.id_mayor if my_ledger else 0})