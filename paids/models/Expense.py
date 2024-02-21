from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models import Order
from partials.models import Partial
from suppliers.models import Supplier


class Expense(models.Model):
    id_gastos_nacionalizacion = models.AutoField(primary_key=True)
    nro_pedido = models.ForeignKey(Order, models.PROTECT, db_column='nro_pedido')
    id_parcial = models.PositiveSmallIntegerField(default=0)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    concepto = models.CharField(max_length=45)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    valor_provisionado = models.DecimalField(max_digits=8, decimal_places=2)
    valor_ajuste = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    fecha = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    bg_closed = models.IntegerField(default=0)
    bg_is_visible_gi = models.IntegerField(default=1)
    bg_iscontabilizado = models.IntegerField(default=0)
    bg_iscontabilizado_por = models.IntegerField(blank=True, null=True, default=0)
    bg_isdrop = models.BooleanField(blank=True,null=True,default=False) #indica si el gasto es arrastrado similar a los gastos de bodega
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return  ''.join([str(self.id_gastos_nacionalizacion), ' ', self.concepto]) 


    class Meta:
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
            return self.objects.get(pk=id_expense)
        except ObjectDoesNotExist:
            loggin('w', 'La provision {id_expense} no existe'.format(id_expense=id_expense))
            return None

    @classmethod
    def get_all_by_order(self, nro_order):
        ''' Obtiene los gastos inciales de un pedido '''
        expenses =  self.objects.filter(nro_pedido = nro_order)
        order = Order.get_by_order(nro_order)        
        loggin('i', 'Obteniendo todos los gastos iniciales Pedido Consumo {}'.format(nro_order))
        if expenses.count() is 0:
            loggin('w', 'No existen gastos para el pedido {}'.format(nro_order))
            return []
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
            return []

        return provisions

    @classmethod
    def get_complete_expenses(self, nro_order)->list:
        '''Lista completa de gastos de un pedido'''
        expenses = list(self.get_all_by_order(nro_order))
        partials = Partial.get_by_order(nro_order)
        for p in partials:
            expenses.extend(list(self.get_by_parcial(p.id_parcial)))

        return expenses

    @classmethod
    def get_months_storage(self,  nro_order):
        """Retorna el analisis de almacenajes de un pedido 
        regimen 70, los datos los toma a partir de facturas de almacenaje
        ingresadas en el sistema

        Args:
            nro_order (string): numero de pedido a consultar
        """
        order = Order.get_by_order(nro_order)
        months = 0

        if order is None:
            return months

        if order.regimen == '10':
            return months

        expenses = Expense.get_complete_expenses(nro_order)
        for expense in expenses:
            if expense.concepto.startswith('DEPOSITO 20'):
                months += 1

        return months