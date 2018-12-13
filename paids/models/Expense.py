from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from orders.models.Order import Order
from partials.models.Partial import Partial
from suppliers.models.Supplier import Supplier
from logs.app_log import loggin

class Expense(models.Model):
    id_gastos_nacionalizacion = models.AutoField(primary_key=True)
    nro_pedido = models.ForeignKey(Order, models.PROTECT, db_column='nro_pedido')
    id_parcial = models.PositiveSmallIntegerField(default=0)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    concepto = models.CharField(max_length=45)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    valor_provisionado = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    bg_closed = models.IntegerField(default=0)
    bg_is_visible_gi = models.IntegerField(default=1)
    bg_iscontabilizado = models.IntegerField(default=0)
    bg_iscontabilizado_por = models.IntegerField(blank=True, null=True, default=0)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return  ''.join([str(self.id_gastos_nacionalizacion), ' ', self.concepto]) 


    class Meta:
        managed = False
        db_table = 'gastos_nacionalizacion'
        unique_together = (('nro_pedido', 'id_parcial', 'concepto'),)
        ordering = ['concepto','nro_pedido','id_parcial','tipo']
        verbose_name_plural = 'Gastos Nacionalizacion'
    

    @classmethod
    def get_by_order(self, nro_order):
        expenses =  self.objects.filter(nro_pedido = nro_order)
        if expenses.count() is 0:
            loggin('w', 'No existen gastos para el pedido {nro_order}'.format(nro_order = nro_order))
            return None
        return expenses
    

    @classmethod
    def get_by_parcial(self, partial):
        provisions =  self.objects.filter(id_parcial = partial.id_parcial)
        if provisions.count() == 0:
            loggin('w', 'El parcial {id_partial} no se tiene gastos'.format(id_partial=partial.id_parcial))
            return None
        
        return provisions

    
    @classmethod
    def get_by_supplier(self, id_supplier):
        pass


    @classmethod
    def get_by_concept(self, query_concept):
        pass


    @classmethod
    def get_all_open_provisions(self):
        provisions = self.objects.filter(bg_closed=0).exclude(concepto='ISD')
        if provisions.count() == 0:
            return []
        
        for p in provisions:
            if p.nro_pedido_id == '000-00':                
               p.order = Partial.get_order_by_parcial(p.id_parcial)
               pass
            else:
                p.order = p.nro_pedido
            
            if p.id_parcial == 0:
                p.id_parcial =1

        return provisions