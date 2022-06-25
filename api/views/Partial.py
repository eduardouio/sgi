from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from lib_src import CompletePartialInfo
from lib_src.serializers import PartialSerializer
from lib_src.TypeChangeOrder import get_by_parcial
from partials.models import Partial


class PartialCreateView(generics.CreateAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer


class PartialDeleteView(generics.DestroyAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer

    def delete(self, request, pk, *args, **kwargs):
        partial = Partial.objects.get(pk=pk)
        partial.delete()
        return Response(status=204)


class PartialDetailView(generics.RetrieveAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer


class PartialUpdateView(generics.UpdateAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer
       


class CompletePartialInfoApiView(generics.GenericAPIView):
    def get(self, request, id_partial):
        partial_all_data = CompletePartialInfo().get_data(
            id_partial=id_partial,
            serialized=True,
            type_change_trimestral=get_by_parcial(id_partial)
            )
        return Response(partial_all_data)