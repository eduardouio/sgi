from rest_framework.generics import (
                            CreateAPIView, 
                            DestroyAPIView, 
                            UpdateAPIView, 
                            RetrieveAPIView
                            )
from orders.models.Order import Order
from lib_src.serializers import OrderSerializer

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