from rest_framework import generics
from lib_src.serializers import PartialSerializer
from partials.models.Partial import Partial

class PartialCreateView(generics.CreateAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer



class PartialDeleteView(generics.DestroyAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer


class PartialDetailView(generics.RetrieveAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer


class PartialUpdateView(generics.UpdateAPIView):
    queryset = Partial.objects.all()
    serializer_class = PartialSerializer