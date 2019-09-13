from logs.app_log import loggin
from orders.models import Order, OrderInvoice, OrderInvoiceDetail
from partials.models import InfoInvoice, InfoInvoiceDetail, Partial
from products.models import Product


class IceReportImportations(object):
    
    def __init__(self, year, month):
        """Obtencion de datos del reporte ICE
    
    Arguments:
        year {string} -- Anio del reporte
        mounth {string} -- Mes del Reporte
    """
        self.year = year
        self.month = month

    def get(self):
        return {
            'almacenera' : self.get_alamacenera_arrivals(),
            'consumo' : self.get_vinesa_arrivals(),
            'parciales': [],
        }
    
    def get_alamacenera_arrivals(self):
        loggin('i', 'Obteniendo lista de pedidos en R70')
        orders = Order.objects.filter(
            fecha_ingreso_almacenera__year = self.year, 
            fecha_ingreso_alamacenera__month=self.month
            )
        details = []
        for order in orders:            
            products = OrderInvoiceDetail.get_by_order(order.nro_pedido)
            if products is not None:
                details.append(products)
        
        return details


    def get_vinesa_arrivals(self):
        """
        Obtiene la lista de pedidos a consumo llegados a Vinesa 
        """
        orders = Order.objects.filter(
            fecha_llegada_cliente__year = self.year,
            fecha_llegada_cliente__month = self.month
        )
        details = []
        for order in orders:
            products = OrderInvoiceDetail.get_by_order(order.nro_pedido)
            if products is not None:
                details.append(products)

        return details
        
    

    def get_partials_arrivals(self):
        """Parciales llegados a las bodegas de Vinesa
        """
        pass
