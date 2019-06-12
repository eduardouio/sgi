from decimal import Decimal

from logs.app_log import loggin
from orders.admin import OrderInvoiceDetailInline


class CostingsOrder(object):
    
    def __init__(self, *args, **kwargs):
        """
        Retorna el costeo de un pedido
        """
        loggin('i', 'Iniciando costeo de pedido Regimen 10')
        self.cmp_order_info = kwargs['complete_order_info']
        self.incoterm = None
        self.origin_expenses = 0
        self.total_items = 0
        self.rates = self.set_rates()
        self.ice_reliquidado = 0
    
    def set_rates(self):
        """
        Inicia los parametros para la liquidacion del pedido
        """
        self.incoterm = self.cmp_order_info['order'].incoterm
        if self.incoterm.upper() == 'FOB':
            self.origin_expenses = self.cmp_order_info['order'].gasto_origen 
        
        return {
            'base_etiquetas' : self.cmp_order_info['order'].base_etiquetas,
            'base_ice_advalorem' : self.cmp_order_info['order'].base_ice_advalorem,
            'porcentaje_ice_advalorem' : self.cmp_order_info['order'].porcentaje_ice_advalorem,
            'base_fodinfa' : self.cmp_order_info['order'].base_fodinfa,
            'tipo_cambio_trimestral' : self.cmp_order_info['tipo_cambio_trimestral'],
        }
    
    def get_costs(self):
        """
        Obtiene los costos del pedido
        """
        pass
    
    def get_costs_item(self, line_item):
        """Obtiene el costo para la linea de la factura
        
        Arguments:
            line_item {OrderInvoiceDetail} -- Objeto linea de factura de proveedor
        """
        line_item = self.get_apportionment_item(line_item)



    def get_taxes(self) -> list:
        """Obtiene la reliquidacion de ICE de cada uno de los items
        
        Returns:
            list -- Lista de impuestos por item
        """        
        taxes_line_item = []
        if self.cmp_order_inf['order'].bg_is_closed:
            loggin('w', 'no se costea un pedido cerrado, se retorna el existente')
            return self.cmp_order_info['order_invoice']['order_invoice_details']
        
        for line_item in self.cmp_order_info['order_invoice']['order_invoice_details']:
            taxes_line_item.append(self.get_costs_item(line_item))            


        return taxes_line_item

    def get_apportionment_item(self, line_item):
        """Retorna el prorrateo del costo pata el item de la factura
        
        Arguments:
            line_item {OrderInvoiceDEtail} -- item de factura proveedor
        """
        line_item.fob_percent = (
            (line_item.nro_cajas * line_item.costo_caja)
            / self.cmp_order_info['order']['order_invoice']['totals']['value']
        )

        line_item.etiquetas_fiscales = (
            line_item.nro_cajas 
            * line_item.cantidad_x_caja 
            * self.rates['base_etiquetas']
        )

        line_item.ex_aduana = (
            line_item.cif 
            + line_item.fodinfa
            + line_item.arancel_advalorem_pagar
            + line_item.arancel_especifico_pagar
            + line_item.etiquetas_fiscales
            + line_item.tasa_control 
        )

        line_item.ex_aduana_unitario = line_item.ex_aduana /  line_item.unidades
        