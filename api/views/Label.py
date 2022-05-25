from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from labels.models import Label
from lib_src.serializers import LabelSerializer


class LabelCreateView(generics.CreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDeleteView(generics.DestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetailView(generics.RetrieveAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelUpdateView(generics.UpdateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


# /api/labels/from-id-invoice/<id_factura_detalle>/
class LabelsFromDetallePedidoFactura(APIView):
    def get(self, request, id_factura_detalle, format=None):
        labels = Label.objects.filter(
            id_factura_detalle_id=id_factura_detalle
        )
        serializer = LabelSerializer(labels, many=True)
        return Response(serializer.data)
    