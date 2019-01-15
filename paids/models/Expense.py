from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from orders.models.Order import Order
from partials.models.Partial import Partial
from suppliers.models.Supplier import Supplier
from logs.app_log import loggin
from django.core.exceptions import ObjectDoesNotExist
from simple_history.models import HistoricalRecords

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
    history = HistoricalRecords()

    def __str__(self):
        return  ''.join([str(self.id_gastos_nacionalizacion), ' ', self.concepto]) 


    class Meta:
        #managed = False
        managed = True
        db_table = 'gastos_nacionalizacion'
        unique_together = (('nro_pedido', 'id_parcial', 'concepto'),)
        ordering = ['concepto','nro_pedido','id_parcial','tipo']
        verbose_name_plural = 'Gastos Nacionalizacion'
    

    @property
    def ordinal_parcial(self):
        return Partial.get_ordinal_number(self.id_parcial)


    @classmethod
    def get_by_id_expense(self, id_expense):
        try:
            expense = self.objects.get(pk=id_expense)
        except ObjectDoesNotExist:
            loggin('w', 'La provision {id_expense} no existe'.format(id_expense=id_expense))
            return None
        
        return expense


    @classmethod
    def get_all_by_orderR10(self, nro_order):
        ''' Returns all expesnes from order R10 only '''
        expenses =  self.objects.filter(nro_pedido = nro_order)
        order = Order.get_by_order(nro_order)
        
        loggin('i', 'Obteniendo todos los gastos iniciales Pedido Consumo {}'.format(nro_order))
        
        if order is None or order.regimen == '70':
            loggin(
                'w', 
                'No se pueden obtener los gastos EL pedido {} no existe o es un regimen 70'
                .format(nro_order)
                )

        if expenses.count() is 0:
            loggin('w', 'No existen gastos para el pedido {}'.format(nro_order))
        
        return expenses
    

    @classmethod
    def get_by_parcial(self, id_partial):
        ''' Returns all expesnes from a one parcial only '''
        provisions =  self.objects.filter(id_parcial = id_partial)
        if provisions.count() == 0:
            loggin(
                'w', 
                'El parcial {} no se tiene gastos'
                .format(id_partial)
                )
            return None
        
        return provisions
    

    @classmethod
    def get_all_by_orderR70(self, nro_order):
        ''' Returns all expesnes from order R70 only '''
        pass