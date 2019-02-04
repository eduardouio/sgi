from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from logs.app_log import loggin
from orders.models.Order import Order


class LiquidateOrderTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/admin/'
    template_name = 'costings/liquidar_pedido.html'
    pass