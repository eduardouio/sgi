from logs.app_log import loggin 

class ReliquidateICE(object):
    '''
        Realiza la reliquidacion de un pedido
    '''
    
    def __init__(self, *args, **kwargs):
        '''Retorna los valores de reliquidacion para un pedido
        
        Arguments:
        complete_order_info {dict} : informacion completa de un pedido
        '''
        loggin('i', 'Iniciando clase de reliquidacion de pedido')
        self.complete_order_info = kwargs['complete_order_info']
        self.incoterm = None
        self.origin_expenses = 0
        self.total_items = 0
        self.rates = self.set_rates()
    
    
    def get_data(self):
        '''Realiza el costeo del producto en base a los costos indirectos
            y costos adicionales en la liquidacion, de forma adicional 
            realiza el calculo de pago de ice advalorem reliquidado
        
        Returns:
            {dict}      'taxes' : [],
                        'sums' : [],
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
        }
    

    def set_rates(self):
        self.incoterm = self.complete_order_info['order'].incoterm
        self.origin_expenses = self.complete_order_info['order'].gasto_origen
        return {
            'base_etiquetas' : self.complete_order_info['order'].base_etiquetas,
            'base_ice_advalorem' : self.complete_order_info['order'].base_ice_advalorem,
            'porcentaje_ice_advalorem' : self.complete_order_info['order'].porcentaje_ice_advalorem,
            'base_fodinfa' : self.complete_order_info['order'].base_fodinfa,
            'tipo_cambio_trimestral' : self.complete_order_info['order_invoice']['order_invoice'].tipo_cambio,
        }

    def get_taxes(self):
        taxes_line_items  = []
        
        for item in self.complete_order_info['order_invoice']['order_invoice_details']:
            taxes_line_items.append(self.get_costs_item(item)) 
        
        return taxes_line_items


    def get_costs_item(self, line_item):
        line_item = self.get_apportionment_item(line_item)
        #verificar si es necesario 
        line_item.indirectos = (
              line_item.ice_advalorem_reliquidado
            + line_item.ice_especifico
            + line_item.fodinfa
            + line_item.tasa_control
            + line_item.arancel_advalorem_pagar
            + line_item.arancel_especifico_pagar
        )
        
        line_item.costo_total = line_item.indirectos + line_item.prorrateos_total
        line_item.costo_caja_final = line_item.costo_total / line_item.nro_cajas
        line_item.costo_unidad = line_item.costo_total / line_item.unidades

        return line_item


    def get_apportionment_item(self, line_item):        
        totals = self.complete_order_info['order_invoice']['totals']['value']
        total_init_expenses = self.complete_order_info['init_expenses']
        for expense in self.complete_order_info['expenses']:
            if expense.concepto == 'ETIQUETAS FISCALES' or expense.concepto == 'TASA DE CONTROL ADUANERO':
                total_init_expenses -= expense.valor_provisionado
        
        line_item.fob_percent = ((line_item.nro_cajas * line_item.costo_caja) / totals)
        line_item.etiquetas_fiscales = (
                        line_item.nro_cajas 
                        * line_item.cantidad_x_caja
                        * self.rates['base_etiquetas']
                ) 
        
        line_item.prorrateo_pedido = (total_init_expenses * line_item.fob_percent)

        line_item.ex_aduana = (
            line_item.ex_aduana_antes
            + line_item.etiquetas_fiscales
            + line_item.tasa_control
        )
        line_item.ex_aduana_unitario = (line_item.ex_aduana / line_item.unidades)
        line_item.base_advalorem_reliquidado = (
            self.rates['base_ice_advalorem'] 
            * (line_item.capacidad_ml/1000)
            )

        if line_item.ex_aduana_unitario > line_item.base_advalorem_reliquidado:
            line_item.ice_advalorem_reliquidado = (
                (line_item.ex_aduana_unitario - self.rates['base_ice_advalorem'])
                * self.rates['porcentaje_ice_advalorem']
            ) * line_item.unidades

        line_item.fob_tasa_trimestral = ( 
                totals * 
                self.rates['tipo_cambio_trimestral'] * 
                line_item.fob_percent
                )
        
        line_item.gastos_origen_tasa_trimestral = 0
        
        if self.incoterm == 'FOB':
            line_item.gastos_origen_tasa_trimestral = (
                self.origin_expenses * line_item.fob_percent
                )

        line_item.prorrateos_total = (
            line_item.prorrateo_pedido 
            + line_item.prorrateo_parcial 
            + line_item.fob_tasa_trimestral
            )

        return line_item