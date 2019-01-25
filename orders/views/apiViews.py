from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from partials.models.Partial import Partial
from logs.app_log import loggin


class GetCompleteOrderInfoAPIView(APIView):
    
    def get(self,request, nro_order):
        order = CompleteOrderInfo().get_data(nro_order=nro_order,serialized=True)
        return Response(order)
