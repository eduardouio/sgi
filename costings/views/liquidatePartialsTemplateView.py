from django.views.generic import TemplateView
from lib_src.CompleteParcialInfo import CompleteParcialInfo

class liquidatePartialsTemplateView(TemplateView):
    template_name = "costings/revisar_gastos_parciales.html"
    
    def get(self, request, nro_order , ordinal_parcial , *args, **kwargs):
        """
        Muestra la pagina de liquidacion de gastos Parciales
        Args:
            nro_order (string): pedido a recuperar 000-00
        Return: TemplateView
        """
        context = super(liquidatePartialsTemplateView, self).get_context_data(*args, **kwargs)                
        return self.render_to_response(context)