from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from orders.models.Order import Order
from logs.app_log import loggin
from simple_history.models import HistoricalRecords
from django.core.exceptions import ObjectDoesNotExist


class Partial(models.Model):
    id_parcial = models.AutoField(primary_key=True)
    nro_pedido = models.ForeignKey(Order,models.PROTECT, db_column='nro_pedido')
    tipo_cambio = models.DecimalField(max_digits=15, decimal_places=10, default=1)
    fecha_nacionalizacion = models.DateField(blank=True, null=True)    
    bg_isclosed = models.IntegerField(blank=True, null=True, default=0)
    fecha_salida_almacenera = models.DateField(blank=True, null=True)
    proximo_almacenaje_desde = models.DateField(blank=True, null=True)
    otros = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    exoneracion_arancel = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    bg_have_etiquetas_fiscales = models.IntegerField(default=0, blank=True, null=True)
    bg_isliquidated = models.IntegerField(blank=True, null=True)
    bg_have_tasa_control = models.IntegerField(blank=True, null=True)
    fodinfa = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fodinfa_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_advalorem = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_advalorem_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_especifico = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_especifico_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iva_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar_pagado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    liquidacion_con_tasa = models.IntegerField(blank=True, null=True)
    base_arancel_advalorem = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_arancel_especifico = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_ice_especifico = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_ice_advalorem = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    porcentaje_ice_advalorem = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_iva = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_fodinfa = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_etiquetas = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)
    arancel_especifico_pagar = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    arancel_especifico_pagar_pagado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    nro_liquidacion = models.CharField(max_length=22, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    id_user_cierre = models.PositiveSmallIntegerField(blank=True, null=True)
    fecha_llegada_cliente = models.DateField(blank=True, null=True)
    notas_cierre = models.CharField(max_length=200, blank=True, null=True)
    fecha_salida_autorizada_almagro = models.DateTimeField(blank=True, null=True)
    url_dai_1 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_2 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_3 = models.CharField(max_length=600, blank=True, null=True)
    path_dai_3 = models.FileField(upload_to='dais_parciales/', max_length=600, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True) 
    fecha_solicitud_salida_almagro = models.DateField(blank=True, null=True)
    agente_aduana = models.CharField(max_length=100, blank=True, null=True)
    ruc_agente_aduana = models.CharField(max_length=13, blank=True, null=True)
    fecha_declaracion_inicial = models.DateField(blank=True, null=True)  
    fecha_entrega_etiquetas_senae = models.DateField(blank=True, null=True)
    fecha_pegado_etiquetas = models.DateField(blank=True, null=True)
    etiquetas_pegadas = models.IntegerField(blank=True, null=True)
    fecha_aforo_fisico = models.DateField(blank=True, null=True)
    fecha_aprovacion_dai = models.DateField(blank=True, null=True)
    punto_lledada = models.CharField(max_length=60, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_parcial)

    class Meta:
        #managed = False
        managed = True
        db_table = 'parcial'
        verbose_name_plural = 'Parciales'
        ordering = ['nro_pedido', 'id_parcial']
    

    @property
    def ordinal_parcial(self):
        return self.get_ordinal_number(self.id_parcial)

    @property
    def partial_url(self):
        return ''.join([self.nro_pedido_id, '/' , str(self.ordinal_parcial) , '/'])
    
    @classmethod
    def get_by_order(self, nro_order):
        parcials =  self.objects.filter(nro_pedido= nro_order)
        if parcials.count() == 0:
            loggin('w', 'No existe informacion para el id del parcial indicado')
            return None
        
        return parcials
    

    @classmethod
    def get_by_id(self, id_partial):
        try:
            partial = self.objects.get(pk=id_partial)
        except ObjectDoesNotExist:
            loggin('w', 'El Parcial {id_partial} no existe'.format(id_partial=id_partial))
            return None
        
        return partial

    
    @classmethod
    def get_by_arrived_local_warenhouse(self, date_start, date_end):
        pass

    @classmethod
    def get_info_invoice(self, if_parcial):
        pass
    

    @classmethod
    def get_ordinal_number(self, id_partial):
        ''' Ordinal from parcial '''
        current_partial = self.get_by_id(id_partial)
        if current_partial is None:
            return 0
        
        all_partials = self.get_by_order(current_partial.nro_pedido)
        ordinal = 1 
        for p in all_partials:
            if p.id_parcial == current_partial.id_parcial:
                return ordinal
            ordinal += 1


    @classmethod
    def get_order_by_parcial(self, id_parcial):
        try:
            parcial = self.objects.get(pk = id_parcial)
        except:
            loggin('e', 'El parcual no existe {id_parcial}'.format(id_parcial = id_parcial))
            return None
        
        if parcial is None:
            loggin('w', 'No se puede recupear la order de un parcial que no existe {id_parcial}'.format(id_parcial=id_parcial))
            return None

        return Order.get_by_order(parcial.nro_pedido_id)
        