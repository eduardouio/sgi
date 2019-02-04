from logs.app_log import loggin
from decimal import Decimal

class ProductsCosts(object):
    def __init__(self, complete_order_info, complete_partial_info = None, apportionmet_partial = None):
        """
        realiza el calculo de costeo del producto de un parcial o pedido R10,
        si la liquidacion es de un regimen 10 solo pasa el primer parametro
        
        Arguments:
            order_data {dict} -- Informacion completa de un pedido
        
        Keyword Arguments:
            partial_data {dict} -- Informacion completa del parcial al liquidar (default: {None})
            apportionmet {dict} -- detalle completo de prorrateos (default: {None})
        """ 
        self.order_info = complete_order_info
        self.partial_info = complete_partial_info
        self.apportionment = apportionmet_partial
        self.partial_calc = (complete_order_info is None)


    def get_costings(self):
        '''
        obtener los costos del producto
        {Dict} -- 
        
        costs = {
            'taxes' : [],
            'order' : [],
            'partial' : [],
            'sums' : {},
            'reliquidacion_ice' : 0.0,
        }
        '''

        self.set_configurations()
        if self.partial_calc:
            pass
        else:
            pass


        
        sums = []

        for line_item in self.order_data['order_invoice']['order_invoice_details']:
            costs['taxes'].append(self.get_line_item_cost(line_item))

        for k,line_item in enumerate(costs['taxes']):            
            if k == 0:
                for key in line_item.__dict__.keys():
                    sums.append({key : 0.0})
            current_line_item = line_item.__dict__
            for i,total in enumerate(sums):
                for idx in total:
                    if isinstance(current_line_item[idx], Decimal):
                        sums[i][idx] += float(current_line_item[idx])

        for i in sums:
            costs['sums'].update(i)
        
        costs['reliquidacion_ice'] = (
            costs['sums']['total_ice'] 
            - float(self.order_data['order'].ice_advalorem_pagado)
            - float(self.order_data['order'].ice_especifico_pagado)
            )

        return costs


    def calc_partial_constings():
        pass
    

    def calc_order_costings():
        pass


    def set_configurations(self):       
        '''
        Set init params from costings product invoice
        '''
        self.type_change_order = self.order_data['order_invoice']['order_invoice'].tipo_cambio
        self.incoterm = self.order_data['order'].incoterm

        if self.incoterm == 'FOB':
            self.gasto_origen_tasa_trimestral = (
                self.order_data['order'].gasto_origen
                * self.type_change_order
                )

        self.taxes_params['base_etiquetas'] = self.order_data['order'].base_etiquetas
        self.taxes_params['base_advalorem'] = self.order_data['order'].base_ice_advalorem
        self.taxes_params['base_fodinfa'] = self.order_data['order'].base_fodinfa
        self.taxes_params['porcentaje_ice_advalorem'] = 0.75
        #self.taxes_params['porcentaje_ice_advalorem'] = self.order_data['order'].porcentaje_ice_advalorem

    
    def get_line_item_cost(self, order_invoice_detail):
        '''
        join reliquidatios ice with prorrateos
        '''
        line_item_cost = self.get_reliquidation_line_item(order_invoice_detail)
        return self.get_prorrateo_line_item(line_item_cost)


    def get_reliquidation_line_item(self, order_invoice_detail):
        '''
        Return reliquidation ICE Value
        param (OrderInvoiceDetail) order_invoice_detail
        return -> OrderInvoiceDetail        
        '''
        order_invoice_detail.etiquetas_fiscales = (
                self.taxes_params['base_etiquetas'] * order_invoice_detail.unidades
        )

        exaduana_reliquidacion = (
            order_invoice_detail.etiquetas_fiscales
            + order_invoice_detail.cif
            + order_invoice_detail.tasa_control
            + order_invoice_detail.otros
            + order_invoice_detail.arancel_especifico_pagar
            + order_invoice_detail.arancel_advalorem_pagar
        )

        exaduana_reliquidacion_unitario = (
            exaduana_reliquidacion
            / order_invoice_detail.unidades
            )

        order_invoice_detail.ex_aduana = exaduana_reliquidacion
        order_invoice_detail.ex_aduana_unitario = exaduana_reliquidacion_unitario
        ice_advalorem_reliquidado = 0.0 

        if exaduana_reliquidacion_unitario > self.taxes_params['base_advalorem']:
            loggin('i', 'Producto con reliquidacion de ICE Advalorem')
            ice_advalorem_reliquidado = (
                (exaduana_reliquidacion_unitario - self.taxes_params['base_advalorem'])
                * self.taxes_params['porcentaje_ice_advalorem'] * order_invoice_detail.unidades
            )

        order_invoice_detail.ice_advalorem_reliquidado = ice_advalorem_reliquidado

        return order_invoice_detail
        

    def get_prorrateo_line_item(self, order_invoice_detail):
        '''
        Returns indirect costs for the line item
        params (int) id_order_invoice_detail
        return -> dict 
        fob_tasa_trimestral
        gasto_origen_tasa_trimestral    
        '''
        order_invoice_detail.fob_tasa_trimestral = (
            order_invoice_detail.costo_caja 
            * order_invoice_detail.nro_cajas
            * self.type_change_order
        )

        order_invoice_detail.gasto_origen_tasa_trimestral = (
            self.gasto_origen_tasa_trimestral
            * order_invoice_detail.fob_percent
        )

        gastos_inciales = self.order_data['init_expenses']

        prorrateos_gastos_inciales = ( 
            (gastos_inciales * order_invoice_detail.fob_percent)
            + order_invoice_detail.gasto_origen_tasa_trimestral
        )

        order_invoice_detail.prorrateo_pedido = order_invoice_detail.prorrateos_total = prorrateos_gastos_inciales

        order_invoice_detail.indirectos  = (
            + order_invoice_detail.fodinfa
            + order_invoice_detail.arancel_advalorem_pagar
            + order_invoice_detail.arancel_especifico_pagar
            + order_invoice_detail.total_ice
            + order_invoice_detail.prorrateo_pedido
        )


        order_invoice_detail.costo_total = (
            order_invoice_detail.indirectos
            + order_invoice_detail.fob_tasa_trimestral
        )

        order_invoice_detail.costo_caja_final = (
            order_invoice_detail.costo_total / order_invoice_detail.nro_cajas
        )
        order_invoice_detail.costo_botella = (
            order_invoice_detail.costo_caja_final / order_invoice_detail.cantidad_x_caja
        )

        if order_invoice_detail.save():
            loggin(
                's', 
                'La informacion de costeo se ha guarado correntamente line item {}'
                .format(order_invoice_detail.detalle_pedido_factura)
                )
        
        return order_invoice_detail