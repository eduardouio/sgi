from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from partials.models.Partial import Partial


class Apportionment(models.Model):
    id_prorrateo = models.AutoField(primary_key=True)
    id_parcial = models.ForeignKey(Partial, models.PROTECT, db_column='id_parcial')
    porcentaje_parcial = models.DecimalField(max_digits=15, decimal_places=12,default=0)
    fob_parcial_razon_inicial = models.DecimalField(max_digits=15, decimal_places=10,default=0)
    fob_parcial_razon_saldo = models.DecimalField(max_digits=15, decimal_places=10,default=0)
    fob_proximo_parcial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    fob_inicial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    fob_saldo = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    fob_parcial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    almacenaje_parcial = models.DecimalField(max_digits=15, decimal_places=10,default=0)
    almacenaje_anterior = models.DecimalField(max_digits=15, decimal_places=10,default=0)
    almacenaje_aplicado = models.DecimalField(max_digits=16, decimal_places=3,default=0)
    almacenaje_proximo_parcial = models.DecimalField(max_digits=16, decimal_places=3,default=0)
    prorrateo_flete_aduana = models.DecimalField(max_digits=16, decimal_places=10,default=0)
    prorrateo_seguro_aduana = models.DecimalField(max_digits=16, decimal_places=10,default=0)
    gastos_drop_parcial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_drop_parcial_anterior = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_drop_parcial_aplicado = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_drop_parcial_proximo_parcial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_origen_incial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_origen_anterior_parcial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_origen_aplicado = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    gastos_origen_proximo_parcial = models.DecimalField(max_digits=15, decimal_places=6,default=0)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_prorrateo)

    class Meta:
        managed = True
        db_table = 'prorrateo'
        verbose_name_plural = 'Prorrateos De Parciales'
        ordering = ['id_parcial']
    
    @classmethod
    def get_by_id(self, id_apportionment):
        try:
            return self.objects.get(pk=id_apportionment)
        except ObjectDoesNotExist:
            loggin(
                'w', 
                'El prorrateo {} no existe'
                .format(id_apportionment)
                )
            return None
    

    @classmethod
    def get_by_parcial(self,id_partial):
        apportiment = self.objects.filter(id_parcial = id_partial)

        if apportiment.count() == 1:
            loggin(
                's', 
                'Prorrateo del parcial {} recuperado'
                .format(id_partial)
                )

            return apportiment.first()

        loggin(
            'e', 
            'El parcial {} no tiene prorrateos, o tiene mas de uno'
            .format(id_partial)
            )
            
        return None
    

    @classmethod
    def get_last_apportionment(self, nro_order):
        loggin('i', 'obteniendo el ultimo prorrateo de un pedido')
        last_partial = Partial.get_last_close_partial(nro_order)
        
        if last_partial is None:
            return None
        
        return self.get_by_parcial(last_partial.id_parcial)
    

    @classmethod
    def delete_from_parcial(self, id_partial):
        apportioments = self.objects.filter(id_parcial=id_partial)
        if apportioments.count() == 0:
            loggin('i', 'Parcial {} sin prorrateos'. format(id_partial))
            return True
        
        for appt in apportioments:
            appt.delete()
        
        loggin('i', 'Eliminacion de prorrateos parcial {}'.format(id_partial))
        return True
