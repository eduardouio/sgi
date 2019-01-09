from django.db import models
from suppliers.models.Supplier import Supplier
from orders.models.Order import Order
from simple_history.models import HistoricalRecords
from logs.app_log import loggin

class RateExpense(models.Model):
    id_tarifa_gastos = models.AutoField(primary_key=True)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    regimen = models.CharField(max_length=5)
    tipo_gasto = models.CharField(max_length=21)
    concepto = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=8, decimal_places=4)
    estado = models.IntegerField(default=1)
    pais_origen = models.CharField(max_length=45)
    porcentaje = models.DecimalField(max_digits=7, decimal_places=4)
    comentarios = models.CharField(max_length=550, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return ''.join([self.concepto ,' ', self.regimen])

    class Meta:
        #managed = False
        managed = True     
        db_table = 'tarifa_gastos'
        unique_together = (('identificacion_proveedor', 'concepto', 'pais_origen', 'valor', 'tipo_gasto'),)
        ordering = ['identificacion_proveedor','regimen','concepto','valor']
        verbose_name_plural = 'Tarias Gastos'
    

    @classmethod
    def get_taxes_params(self):
        loggin('i', 'consultando parametros para calculo de impuestos')
        rates = self.objects.filter(tipo_gasto = 'IMPUESTO')
        if rates.count():
            return rates
        
        loggin('e', 'El sistema no tiene parametros para el calculo de tributos')
        return None








