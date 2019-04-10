from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order
from partials.models import Partial
from lib_src.serializers import OrderSerializer, PartialSerializer
from logs.app_log import loggin


class AllOrders(APIView):
    def get(self, request):
        data = []
        orders = Order.get_open_orders()
        loggin('i', 'Obteniendo todos los pedidos abiertos con sus parciales')

        for order in orders:
            partials = Partial.get_by_order(order.nro_pedido)
            order_serializer = OrderSerializer(order)
            partial_serializer = PartialSerializer(partials, many=True)

            data.append({
                'order': order_serializer.data,
                'partials' : partial_serializer.data
            })
        
        return Response(data)