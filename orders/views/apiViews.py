from django.http import JsonResponse
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def get_complete_order_info(request, nro_order):    
    order = CompleteOrderInfo().get_data(nro_order,True)

    return JsonResponse({ 'data' : order})
