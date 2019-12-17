from decimal import Decimal

from logs.app_log import loggin
from orders.admin import OrderInvoiceDetailInline


class CostingsOrder(object):
    
    def __init__(self, *args, **kwargs):
        """Retorna el costeo de un pedido
        
        Arguments:
            cmp_order_info {CompleteOrderInfo} - informacion completa del pedido
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
    
    def get_costs(self) -> dict:
        """Realiza el costo de un pedido r10, en base a los costos indirectos
        y costos adicionales en la liquidacion, de forma adicional realiza
        el calculo de pago de ice advalorem reliquidado
        
        Returns:
            dict -- {
                taxes : [],
                sums : {},
                data_general: {}
            }
        """
        reliquidate_items = self.__get_taxes()
        sums = {}

        for x, line_item in enumerate(reliquidate_items):
            if x == 0:
                for k in line_item.__dict__:
                    sums[k] = 0.0
                break
        
        for k in sums:
            for line_item in reliquidate_items:
                try:    
                    if float(line_item.__dict__[k]) > 0.0:
                        sums[k] += float(line_item.__dict__[k])
                except:
                    continue
        loggin('t', sums)
        return {
            'taxes' : reliquidate_items,
            'sums' : sums,
            'ice_reliquidado' : self.ice_reliquidado,
        }

        
    def __get_taxes(self) -> list:
        """Obtiene la reliquidacion de ICE de cada uno de los items
        
        Returns:
            list -- Lista de impuestos por item
        """        
        taxes_line_item = []

        if self.cmp_order_info['order'].bg_isclosed:
            loggin('w', 'no se costea un pedido cerrado, se retorna el existente')
            return self.cmp_order_info['order_invoice']['order_invoice_details']
        
        for line_item in self.cmp_order_info['order_invoice']['order_invoice_details']:
            taxes_line_item.append(self.__get_costs_item(line_item))            


        return taxes_line_item


    def __get_costs_item(self, line_item):
        """Obtiene el costo para la linea de la factura
        
        Arguments:
            line_item {OrderInvoiceDetail} -- Objeto linea de factura de proveedor
        """
        line_item = self.__get_apportionment_item(line_item)
        line_item.costo_total = line_item.prorrateos_total + line_item.fob_tasa_trimestral
        line_item.costo_caja_final = line_item.costo_total / line_item.nro_cajas
        line_item.costo_unidad = line_item.costo_total / line_item.unidades
        line_item.save()
        return line_item


    def __get_apportionment_item(self, line_item):
        """Retorna el prorrateo del costo pata el item de la factura
        
        Arguments:
            line_item {OrderInvoiceDEtail} -- item de factura proveedor
        """
        line_item.fob_percent = (
            (line_item.nro_cajas * line_item.costo_caja)
            / self.cmp_order_info['order_invoice']['totals']['value']
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
        line_item.base_advalorem_reliquidado = (
            self.rates['base_ice_advalorem'] * (line_item.capacidad_ml / 1000 )
            )
        
        if line_item.ex_aduana_unitario > line_item.base_advalorem_reliquidado:
            line_item.ice_advalorem_reliquidado = (
                (line_item.ex_aduana_unitario - line_item.base_advalorem_reliquidado)
                * self.rates['porcentaje_ice_advalorem']
            ) * line_item.unidades
            line_item.total_ice = (line_item.ice_advalorem_pagado 
                                    + line_item.ice_especifico)
            line_item.ice_advalorem_reliquidado = (line_item.ice_advalorem_reliquidado -
                                 line_item.ice_advalorem_pagado)
        else:
            line_item.total_ice = (line_item.ice_advalorem_pagado 
                                    + line_item.ice_especifico)
            line_item.ice_advalorem_reliquidado = 0

        self.ice_reliquidado += line_item.ice_advalorem_reliquidado
        line_item.ice_advalorem_diferencia = 0
        line_item.gastos_origen_tasa_trimestral = 0
        line_item.gastos_origen_tasa_trimestral = (
            self.cmp_order_info['origin_expenses_tct'] 
            * line_item.fob_percent)
        line_item.prorrateo_parcial = 0
        line_item.prorrateo_pedido = (
            + line_item.fodinfa
            + line_item.etiquetas_fiscales
            + line_item.total_ice
            + line_item.arancel_especifico_pagar
            + line_item.arancel_advalorem_pagar
            + line_item.gastos_origen_tasa_trimestral
            )
  
        line_item.prorrateo_pedido += (
            self.cmp_order_info['init_expenses'] - 
            self.cmp_order_info['etiquetas_fiscales']
            ) * line_item.fob_percent

        line_item.fob_tasa_trimestral = (
            line_item.costo_caja 
            * line_item.nro_cajas
            * self.cmp_order_info['order_invoice']['order_invoice'].tipo_cambio
            )
        line_item.prorrateos_total = line_item.prorrateo_pedido
        line_item.indirectos = line_item.prorrateo_pedido
        return line_item
