from django.db import models
from logs.app_log import loggin
from simple_history.models import HistoricalRecords

class Ledger(models.Model):    
    id_mayor = models.AutoField(primary_key=True)
    #Inicial | Gastos Iniciales | Gastos Parciales Nparcials 
    tipo = models.CharField(max_length=50)
    nro_pedido = models.CharField(max_length=6)
    id_parcial = models.PositiveSmallIntegerField(default=0)
    valor_en_provisiones = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    valor_en_facturas = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    valor_prorrateado = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)    
    precio_de_indirectos_entrega = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    saldo_mayor_a_liquidacion = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()


    def __str__(self):
        return self.tipo

    class Meta:
        managed = True
        db_table = 'mayor'
        unique_together = (('nro_pedido', 'id_parcial', 'tipo'),)
        verbose_name_plural = 'Mayores Liquidaciones'
        ordering = ['nro_pedido', 'id_parcial','tipo']
    
    @classmethod
    def get_by_order(self, order):
        if(order.regimen == '70'):
            loggin('e', 'Se esta solicitando un mayor del pedido {nro_pedido} R70'.format(nro_pedido=order.nro_pedido))
            return None
            
        items = self.objects.filter(nro_pedido = order.nro_pedido)
        if items.count() == 0:
            loggin('w', 'El pedido {nro_pedido} no tiene registrado ningun mayor'.format(nro_pedido=order.nro_pedido))
            return None

        return items

    @classmethod
    def get_by_parcial(self, partial):
        items = self.objects.filter(id_parcial=partial.id_parcial)
        if items.count() == 0:
            loggin('w', 'El parcial {id_parcial} no registra un mayor'.format(id_parcial=partial.id_parcial))
            return None
        
        return items