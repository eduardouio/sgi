from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class RateIncoterm(models.Model):
    id_incoterm = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=12)
    pais = models.CharField(max_length=45)
    incoterms = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=45)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return ''.join([self.tipo, ' ', self.pais, ' ', self.incoterms])

    class Meta:
        #managed = False
        managed = True
        db_table = 'tarifa_incoterm'
        unique_together = (('pais', 'ciudad', 'incoterms', 'tipo'),)
        ordering = ['tipo','pais','ciudad','incoterms']
        verbose_name_plural = 'Tarias Incoterms'
