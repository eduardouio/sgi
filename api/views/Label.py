import json

from labels.lib_src import ValidateRangeSafeTrack, ValidateBatchSafeTrack, LoginSafeTrack
from labels.models import Label
from lib_src.serializers import LabelSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


class LabelCreateView(generics.CreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDeleteView(generics.DestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    def delete(self, response, pk, *args, **kwargs):
        label = Label.objects.get(pk=pk)
        if(label.bg_status == 'I'):
            label.delete()

        return Response(status=204)


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


# /api/labels/validate-range/<first_tag>/<last_tag>/<quatity_spected>/
class LabesValidRange(APIView):
    def get(self, request, first_tag, last_tag, quantity_spected):
        login = LoginSafeTrack()
        validateRange = ValidateRangeSafeTrack(login)
        data = validateRange.validate(
            first_tag,
            last_tag,
            int(quantity_spected)
        )
        response = json.dumps(data['response'].text)
        data['response'] = response
        return Response(data)


# /api/labels/validate-bacth/<batch>/
class LabesValidateBatch(APIView):
    def get(self, request, batch):
        validateBatch = ValidateBatchSafeTrack()
        data = validateBatch.validate(batch)
        if data['status'] == 200:
            data['response'] = json.dumps(data['response'].text)
            response = json.dumps(data['response'].text)
            data['response'] = response

        return Response(data)


# /api/labels/validate-label/<label>/
class LabelsValidateLabel(APIView):
    pass


# /api/activate/range/<first_tag>/<last_tag>/<ice_sku>/
class ActivateRange(APIView):
    pass
