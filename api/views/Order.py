from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from lib_src import CompleteOrderInfo, OrderProductSale
from lib_src.serializers import OrderSerializer
from logs.app_log import loggin
from orders.models import Order


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

#/order/close/<nro_pedido>/
class OrderCloseView(APIView):
    """Compueba saldos de un pedido y lo cierra"""
    def get(self, request, nro_pedido):
        order_sale = OrderProductSale(nro_pedido)
        products_sale = order_sale.get_sale()
        import ipdb; ipdb.set_trace()
        if products_sale:
            for item in products_sale['items']:
                import ipdb; ipdb.set_trace()
                if int(item['cajas']) != int(item['nacionalizado']):
                    return Response({
                        'nro_pedido':nro_pedido,
                        'is_closable' : 0, 
                    })
            order = Order().get_by_order(nro_pedido)
            if order.bg_isclosed == 0:
                order.bg_isclosed = 1
                order.save()
                loggin('i', 'Cerrando pedido en SGI')
            return Response({
                        'nro_pedido':nro_pedido,
                        'is_closable' : 1, 
                    })
        else:
            return Response({
                        'nro_pedido':nro_pedido,
                        'is_closable' : 0, 
                    })