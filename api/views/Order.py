from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.serializers import OrderSerializer
from logs.app_log import loggin
from orders.models.Order import Order


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    
class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    
class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GetCompleteOrderInfoAPIView(APIView):
    def get(self,request, nro_order):
        order = CompleteOrderInfo().get_data(nro_order=nro_order,serialized=True)
        return Response(order)
