from rest_framework import generics
from partials.models import Apportionment
from lib_src.serializers import ApportionmentSerializer


class ApportionmenCreateView(generics.CreateAPIView):
    queryset = Apportionment.objects.all()
    serializer_class = ApportionmentSerializer


class ApportionmenDeleteView(generics.DestroyAPIView):
    queryset = Apportionment.objects.all()
    serializer_class = ApportionmentSerializer


class ApportionmenDetailView(generics.RetrieveAPIView):
    queryset = Apportionment.objects.all()
    serializer_class = ApportionmentSerializer


class ApportionmenUpdateView(generics.UpdateAPIView):
    queryset = Apportionment.objects.all()
    serializer_class = ApportionmentSerializer
