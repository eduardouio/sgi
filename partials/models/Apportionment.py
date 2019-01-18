from django.db import models
from partials.models.Partial import Partial
from logs.app_log import loggin
from simple_history.models import HistoricalRecords

class Apportionment(models.Model):
    id_prorrateo = models.AutoField(primary_key=True)
    id_parcial = models.ForeignKey(Partial, models.PROTECT, db_column='id_parcial')
    porcentaje_parcial = models.DecimalField(max_digits=15, decimal_places=12)
    fob_parcial_razon_inicial = models.DecimalField(max_digits=15, decimal_places=6)
    fob_parcial_razon_saldo = models.DecimalField(max_digits=15, decimal_places=6)
    fob_proximo_parcial = models.DecimalField(max_digits=15, decimal_places=6)
    fob_inicial = models.DecimalField(max_digits=15, decimal_places=6)
    fob_saldo = models.DecimalField(max_digits=15, decimal_places=6)
    fob_parcial = models.DecimalField(max_digits=15, decimal_places=6)
    almacenaje_parcial = models.DecimalField(max_digits=15, decimal_places=10)
    almacenaje_anterior = models.DecimalField(max_digits=15, decimal_places=10)
    almacenaje_aplicado = models.DecimalField(max_digits=16, decimal_places=3)
    almacenaje_proximo_parcial = models.DecimalField(max_digits=16, decimal_places=3)
    prorrateo_flete_aduana = models.DecimalField(max_digits=15, decimal_places=10)
    prorrateo_seguro_aduana = models.DecimalField(max_digits=15, decimal_places=10)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_prorrateo)

    class Meta:
        #managed = False
        managed = True
        db_table = 'prorrateo'
        verbose_name_plural = 'Prorrateos De Parciales'
        ordering = ['id_parcial']
    

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
        last_partial = Partial.get_last_partial(nro_order)
        if last_partial is None:
            return None
        
        return self.get_by_parcial(last_partial.id_parcial)