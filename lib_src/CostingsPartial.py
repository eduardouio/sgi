from decimal import Decimal

from logs.app_log import loggin


class CostingsPartial(object):
    '''
        Realiza la reliquidacion de un parcial
    '''
    
    def __init__(self, *args, **kwargs):
        '''Retorna los valores de reliquidacion para un pedido
        
        Arguments:
        complete_order_info {dict} : informacion completa de un pedido
        '''
        loggin('i', 'Iniciando clase de reliquidacion de parcial')
        self.complete_order_info = kwargs['complete_order_info']
        self.all_partials = kwargs['all_partials']
        self.apportionment_expenses = kwargs['apportionment_expenses']
        self.current_partial = kwargs['ordinal_current_partial']
        self.incoterm = None
        self.origin_expenses = 0
        self.total_items = 0
        self.rates = self.set_rates()
        self.ice_reliquidado = 0
    
    
    def get_costs(self):
        
        '''Realiza el costeo del producto en base a los costos indirectos
            y costos adicionales en la liquidacion, de forma adicional 
            realiza el calculo de pago de ice advalorem reliquidado
        
        Returns:
            {dict}      'taxes' : [],
                        'sums' : {'ice_reliquidado; = 564},
                        'data_general' : {}, 
        '''
        reliquidate_items = self.get_taxes()
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

        return {
            'taxes' : reliquidate_items,
            'sums' : sums,
            'ice_reliquidado' : self.ice_reliquidado,
        } 
               

    def set_rates(self):
        ''' inicializa las variables de calculo  '''
        self.incoterm = self.complete_order_info['order'].incoterm
        self.origin_expenses = self.complete_order_info['order'].gasto_origen
        return {
            'base_etiquetas' : self.complete_order_info['order'].base_etiquetas,
            'base_ice_advalorem' : self.current_partial['partial'].base_ice_advalorem,
            'porcentaje_ice_advalorem' : self.complete_order_info['order'].porcentaje_ice_advalorem,
            'base_fodinfa' : self.complete_order_info['order'].base_fodinfa,
            'tipo_cambio_trimestral' : self.complete_order_info['order_invoice']['order_invoice'].tipo_cambio,
        }


    def get_taxes(self):
        ''' Obtiene la reliquidacion de ice de los items de la factura '''
        taxes_line_items  = []
        
        if self.current_partial['partial'].bg_isclosed == 1:
            loggin('i', 'No se realiza el costeo se retorna el existente')
            return self.current_partial['info_invoice']['info_invoice_details']

        for line_item in self.current_partial['info_invoice']['info_invoice_details']:
            taxes_line_items.append(self.get_costs_item(line_item)) 
        
        return taxes_line_items


    def get_costs_item(self, line_item):
        ''' Obtiene el costo del item  '''

        line_item = self.get_apportionment_item(line_item)
        line_item.costo_total = line_item.prorrateos_total + line_item.fob_tasa_trimestral
        line_item.costo_caja_final = line_item.costo_total / line_item.nro_cajas
        line_item.costo_unidad = line_item.costo_total / line_item.unidades
        line_item.save()
        return line_item


    def get_apportionment_item(self, line_item):
        ''' Obtiene el prorrateo del item NO SE USA INDIRECTOS  '''
        ice_reliquidado = 0
        line_item.fob_percent = (
            (line_item.nro_cajas * line_item.costo_caja) 
            / self.current_partial['info_invoice']['totals']['value']
            )
        line_item.etiquetas_fiscales = (
                        line_item.nro_cajas 
                        * line_item.cantidad_x_caja
                        * self.rates['base_etiquetas']
            ) 
        line_item.ex_aduana = (
            line_item.ex_aduana_antes
            + line_item.etiquetas_fiscales
            + line_item.tasa_control
            )
        line_item.ex_aduana_unitario = (line_item.ex_aduana / line_item.unidades)
        line_item.base_advalorem_reliquidado = (self.rates['base_ice_advalorem'] * (line_item.capacidad_ml/1000))
        print(self.rates['base_ice_advalorem'])
        if line_item.ex_aduana_unitario > line_item.base_advalorem_reliquidado:
            line_item.ice_advalorem_reliquidado = (
                (line_item.ex_aduana_unitario - line_item.base_advalorem_reliquidado)
                * self.rates['porcentaje_ice_advalorem']
            ) * line_item.unidades

            line_item.total_ice = line_item.ice_advalorem_reliquidado + line_item.ice_especifico
            ice_reliquidado = (line_item.ice_advalorem_reliquidado - line_item.ice_advalorem)
        else:
            line_item.total_ice = line_item.ice_advalorem + line_item.ice_especifico
            
        line_item.fob_tasa_trimestral = ( 
                self.current_partial['info_invoice']['totals']['value'] 
                * self.rates['tipo_cambio_trimestral']
                * line_item.fob_percent
                )
        self.ice_reliquidado += line_item.total_ice
        line_item.ice_advalorem_diferencia = 0
        line_item.gastos_origen_tasa_trimestral = 0
        
        if self.incoterm == 'FOB':
            line_item.gastos_origen_tasa_trimestral = (
                self.origin_expenses * line_item.fob_percent
                )

        line_item.prorrateo_parcial = (
            self.apportionment_expenses['apportionment'].almacenaje_aplicado 
            * line_item.fob_percent
            )
        line_item.prorrateo_pedido = ((
            self.apportionment_expenses['total_aplicado_sin_tributos'] * line_item.fob_percent) 
            +  line_item.fodinfa
            +  line_item.etiquetas_fiscales
            + line_item.total_ice
            + line_item.arancel_especifico_pagar
            + line_item.arancel_advalorem_pagar
            )

        line_item.prorrateos_total = (
            line_item.prorrateo_parcial 
            + line_item.prorrateo_pedido
            )

        return line_item