from lib_src.serializers import ApportionmentDetailSerializer
from partials.models.ApportionmentDetail import ApportionmentDetail
from rest_framework import generics


class ApportionmentDetailCreateView(generics.CreateAPIView):
    queryset = ApportionmentDetail.objects.all()
    serializer_class = ApportionmentDetailSerializer


class ApportionmentDetailDeleteView(generics.DestroyAPIView):
    queryset = ApportionmentDetail.objects.all()
    serializer_class = ApportionmentDetailSerializer


class ApportionmentDetailDetailView(generics.RetrieveAPIView):
    queryset = ApportionmentDetail.objects.all()
    serializer_class = ApportionmentDetailSerializer


class ApportionmentDetailUpdateView(generics.UpdateAPIView):
    queryset = ApportionmentDetail.objects.all()
    serializer_class = ApportionmentDetailSerializer