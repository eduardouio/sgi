from django.views.generic import TemplateView
from logs.app_log import loggin
from lib_src.CompleteOrderInfo import CompleteOrderInfo

class liquidateOrderTemplateView(TemplateView):
    template_name = 'costings/liquidar_pedido.html'

    def get(self, request, nro_order , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Iniciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = super(liquidateOrderTemplateView, self).get_context_data(*args, **kwargs)        
        complete_order = CompleteOrderInfo().get_data(nro_order=nro_order, serialized=False, request=request)
        complete_order['title_page'] = 'Revision de Gastos Iniciales {}'.format(nro_order)       
        context.update({'data': complete_order})

        if complete_order['status']['ledger'] == False:
            loggin('e','El pedido {} no tiene una mayor registrado'.format(nro_order))
            complete_order['status']['ledger']= True
        
        for status_det in complete_order['status']:            
            print(complete_order['status'][status_det])
            if complete_order['status'][status_det] == False:
                loggin('e', 'El pedido {} no existe o esta incompleto, cambniando de plantilla'.format(nro_order))
                self.template_name = 'errors/error_en_pedido.html'
        
        print (type(complete_order['order'].regimen))

        if complete_order['order'].regimen == '70':
            self.template_name = 'costings/seleccionar_parcial.html'

        return self.render_to_response(context)