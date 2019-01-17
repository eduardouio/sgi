import re

import products
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompleteParcialInfo import CompleteParcialInfo
from logs.app_log import loggin


class OrderSale(object):
    '''
    obtiene, los saldos de un pedido, tanto en productos como en provisiones
    y gastos que aun no han sido justificados

    Arguments:
        nro_order {string} -- Nro de pedido, no importa regimens
    
    Returns:
        dict -- Diccionario Clave Valor, se puede serializar
    '''

    def __init__(self):
       self.nro_order = None
       self.order_data = None
       self.type_change_trim = 1
       self.have_partials = False
       self.partials_data = []
    

    def get_all_data(self, nro_order):
        self.nro_order = nro_order
        self.order_data = CompleteOrderInfo().get_data(self.nro_order)
        self.type_change_trim = self.order_data['tipo_cambio_trimestral']
        
        if self.order_data['partials']:
            for partial in self.order_data['partials']:
                self.partials_data.append(CompleteParcialInfo().get_data(partial.id_parcial))
                self.have_partials = True

        data = {
            'product_sale' : self.get_product_sale(),
            'expenses_sale' : self.get_expenses_sale(),
            }

        return data
    

    def get_product_sale(self):
        sale_product = {
            'products' : [],
            'type_change_trim' : float(self.type_change_trim),
            'supplier' : self.order_data['order_invoice']['supplier'].nombre,
            'nro_order' : self.order_data['order'].nro_pedido,
            'totals' : {
                'imported' : 0.0,
                'nationalized' : 0.0,
                'sale' : 0.0,
            },
        }

        if re.search('SF-', self.order_data['order_invoice']['order_invoice'].id_factura_proveedor):
            loggin('w','El pedido no tiene registrada la factura')
            return sale_product


        if self.order_data['status']['order_invoice_details'] == False:
            loggin(
                'w', 
                'Pedido sin {} productos registrados'
                .format(self.nro_order)
                )
            return sale_product
        #imported
        for product in self.order_data['order_invoice']['order_invoice_details'].values():
            product['imported'] = float(product['nro_cajas'])
            sale_product['totals']['imported'] += (float(product['nro_cajas']) * float(product['costo_caja']) * float(self.type_change_trim))

            if int(self.order_data['order'].regimen) == 10:
                product['sale'] = product['imported']
                sale_product['totals']['sale'] += product['sale']
                if self.order_data['order'].bg_isclosed:
                    product['nationalizad'] = product['import']
                    sale_product['totals']['nationalized'] = sale_product['totals']['imported']
                    sale_product['totals']['sale'] = 0

            sale_product['products'].append(product)

        #partials Liquidates
        if int(self.order_data['order'].regimen) == 70:
            for product in sale_product['products']:
                product['nationalized'] = (self.get_nationalized_product(product))
                product['sale'] = product['imported'] - product['nationalized']
                sale_product['totals']['nationalized'] += (float(product['nationalized']) * float(product['costo_caja']) * float(self.type_change_trim))
                sale_product['totals']['sale'] += (float(product['sale']) * float(product['costo_caja']))
        
        return sale_product


    def get_nationalized_product(self, product):
        nationalized = 0
        for partial in self.partials_data:
            if partial['status']['info_invoice_details']:
                if partial['partial'].bg_isclosed == 1:
                    for line_item in partial['info_invoice']['info_invoice_details']:
                        if product['detalle_pedido_factura'] == int(line_item.detalle_pedido_factura_id):
                            nationalized += float(line_item.nro_cajas)

        return (nationalized)


    def get_expenses_sale(self):

        def get_taxes_paid():
            if self.order_data['order'].regimen == '10' :
                return float(self.order_data['taxes']['total_pagado'])
            
            total_taxes = 0

            for partial in self.partials_data:
                total_taxes += partial['taxes']['total_pagado']

            loggin('i', 'Recupernado Tributos Parcial %d'%total_taxes)
            return float(total_taxes)
            
        def get_descargas():
            total_descargas = 0;

            for partial in self.partials_data:
                if partial['partial'].bg_isclosed:
                    for line_item in partial['info_invoice']['info_invoice_details']:
                        if partial['partial'].id_parcial == 127:
                            try:
                                total_descargas += line_item['indirectos']
                            except:
                                total_descargas += 0
            return total_descargas             

        all_expenses = {
            'expenses' : [],
            'type_change' : self.order_data['tipo_cambio_trimestral'],
            'taxes' : get_taxes_paid(),
            'indirectos' : get_descargas(),
                'totals' : {
                    'provision' : 0,
                    'invoiced' : 0,
                    'sale' : 0,
                }
            }
        
        for exp in self.order_data['expenses']:
            all_expenses['expenses'].append(exp)
            all_expenses['totals']['provision'] += float(exp.valor_provisionado)
            all_expenses['totals']['invoiced'] += float(exp.invoiced_value)
            all_expenses['totals']['sale'] += float(exp.sale)

        if self.order_data['order'].regimen != '70':
            return all_expenses
        
        for partial in self.partials_data:
            if partial['expenses']:
                for exp in partial['expenses']:
                    all_expenses['expenses'].append(exp)
                    all_expenses['totals']['provision'] += float(exp.valor_provisionado)
                    all_expenses['totals']['invoiced'] += float(exp.invoiced_value)
                    all_expenses['totals']['sale'] += float(exp.sale)
        
        return all_expenses