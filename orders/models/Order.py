from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from logs.app_log import loggin

class Order(models.Model):
    nro_pedido = models.CharField(primary_key=True, max_length=6)
    regimen = models.CharField(max_length=2, default='00')
    flete_aduana = models.DecimalField(max_digits=10, decimal_places=4)
    seguro_aduana = models.DecimalField(max_digits=10, decimal_places=4)
    incoterm = models.CharField(max_length=4)
    pais_origen = models.CharField(max_length=45, blank=True, null=True)
    ciudad_origen = models.CharField(max_length=45, blank=True, null=True)
    fecha_arribo = models.DateField(blank=True, null=True)
    dias_libres = models.PositiveIntegerField(default=21)
    fecha_salida_bodega_puerto = models.DateField(blank=True, null=True)
    fecha_ingreso_almacenera = models.DateField(blank=True, null=True)
    fecha_salida_almacenera = models.DateField(blank=True, null=True)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    nro_refrendo = models.CharField(max_length=22, blank=True, null=True)
    tipo_cambio_impuestosr10 = models.DecimalField(db_column='tipo_cambio_impuestosR10', max_digits=14, decimal_places=12, blank=True, null=True, default=1)
    tipo_cambio_almacenerar70 = models.DecimalField(db_column='tipo_cambio_almaceneraR70', max_digits=14, decimal_places=12, blank=True, null=True, default =1)
    otros = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    bg_isclosed = models.IntegerField(blank=True, null=True, default=0)
    bg_haveexpenses = models.IntegerField(db_column='bg_haveExpenses', blank=True, null=True, default=0)
    have_etiquetas_fiscales = models.IntegerField(blank=True, null=True, default=0)
    exoneracion_arancel = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    bg_have_tasa_control = models.IntegerField(blank=True, null=True, default=0)
    bg_isliquidated = models.IntegerField(blank=True, null=True, default=0)
    fodinfa = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fodinfa_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_advalorem = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_advalorem_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_especifico = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_especifico_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iva_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    arancel_especifico_pagar = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    arancel_especifico_pagar_pagado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    nro_liquidacion = models.CharField(max_length=12, blank=True, null=True)
    arancel_advalorem_pagar = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar_pagado = models.DecimalField(max_digits=16, decimal_places=0, blank=True, null=True)
    liquidacion_con_tasa = models.IntegerField(blank=True, null=True, default=0)
    base_arancel_advalorem = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    base_arancel_especifico = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    base_ice_especifico = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    base_ice_advalorem = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    porcentaje_ice_advalorem = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    base_iva = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    base_fodinfa = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    base_etiquetas = models.DecimalField(max_digits=16, decimal_places=3,blank=True, null=True, default=0)
    fecha_cierre = models.DateField(blank=True, null=True)
    id_user_cierre = models.PositiveSmallIntegerField(blank=True, null=True, default=0) 
    tipo_cambio_go = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True, default=1)
    gasto_origen = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True, default=0 )
    fecha_llegada_cliente = models.DateField(blank=True, null=True)
    notas_cierre = models.CharField(max_length=200, blank=True, null=True)
    fecha_salida_autorizada_puerto = models.DateTimeField(blank=True, null=True)
    bg_have_close_parcial = models.IntegerField(blank=True, null=True)
    docentry = models.IntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=100 ,blank=True, null=True)
    url_dai_1 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_2 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_3 = models.CharField(max_length=600, blank=True, null=True)
    path_dai_1 = models.FileField(upload_to='dai_pedido/',max_length=600, blank=True, null=True)
    path_dai_2 = models.FileField(upload_to='dai_pedido/',max_length=600, blank=True, null=True)
    path_dai_3 = models.FileField(upload_to='dai_pedido/',max_length=600, blank=True, null=True)

    def __str__(self):
        return ''.join([self.nro_pedido])

    class Meta:
        managed = False
        db_table = 'pedido'
        ordering = ['nro_pedido']
        verbose_name_plural = 'Pedidos'
    
    @classmethod
    def get_by_order(self, nro_order):        
        try:
            order = self.objects.get(pk=nro_order)
        except ObjectDoesNotExist:
            loggin('e', 'El pedido {nro_order} no existe'.format(nro_order=nro_order))
            return None
        
        if order.proveedor is None or order.proveedor is '':
            order.proveedor = 'No Definido'
        
        if order.nro_refrendo is None or order.nro_refrendo is '':
            order.nro_refrendo = 'Pendiente'
        
        if order.nro_liquidacion is None or order.nro_liquidacion is '':
            order.nro_liquidacion = 'Sin Liquidación SENAE'
        
        return order


        

    @classmethod
    def get_all(self):
        return self.objects.all()
    
    @classmethod
    def search(self, query):
        pass

    @classmethod
    def get_by_field(self, **args):
        pass
    
    @classmethod
    def get_arrived_cellar_by_date(self, year, month):
        pass

    @classmethod
    def close_order(self, nro_order):
        pass
    
    @classmethod
    def reopen_order(self, nro_order):
        pass
    
    @classmethod
    def get_paid_taxes(self, nro_order):
        order =  self.get_by_order(nro_order)        
        if order is None or order.regimen == '70':
            loggin('w', 'No se obtener los tributos del pedido {nro_order} pedido inexistente o regimen = 70'.format(nro_order=nro_order))
            return {}    

        taxes =  {
            'arancel_advalorem' : order.arancel_advalorem_pagar_pagado,
            'arancel_especifico' : order.arancel_especifico_pagar_pagado,
            'fondinfa' : order.fodinfa_pagado,
            'ice_advalorem' : order.ice_advalorem_pagado,
            'ice_especifico' : order.ice_especifico_pagado,
            'iva' : order.iva_pagado,
            'exoneracion_arancel' : order.exoneracion_arancel,
            'tipo_cambio' : (bool(order.tipo_cambio_impuestosr10) == False) and 1 or order.tipo_cambio_impuestosr10,
            'nro_liquidacion' : order.nro_liquidacion,
            'fecha_liquidacion' : order.fecha_liquidacion,
            'total_pagado' : (
                    order.arancel_advalorem_pagar_pagado
                    + order.arancel_especifico_pagar_pagado
                    + order.fodinfa_pagado
                    + order.ice_advalorem_pagado
                    + order.ice_especifico_pagado
                    + order.iva_pagado
            ),
            'arancel_advalorem_provisionado' : order.arancel_advalorem_pagar,
            'arancel_especifico_provisionado' : order.arancel_especifico_pagar,
            'fondinfa_provisionado' : order.fodinfa,
            'ice_advalorem_provisionado' : order.ice_advalorem,
            'ice_especifico_provisionado' : order.ice_especifico,
            'iva_provisionado' : order.iva,
            'total_provisionado' : (
                    order.arancel_advalorem_pagar
                    + order.arancel_especifico_pagar
                    + order.fodinfa
                    + order.ice_advalorem
                    + order.ice_especifico
                    + order.iva
            ),
            'complete' : False            
        }

        if (round(taxes['total_provisionado'],2) == round(taxes['total_pagado'],2)):
            taxes['complete'] = True
        
        return taxes