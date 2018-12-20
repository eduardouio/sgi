from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from simple_history.models import HistoricalRecords

class Supplier(models.Model):
    identificacion_proveedor = models.CharField(primary_key=True, max_length=16)
    nombre = models.CharField(unique=True, max_length=60)
    tipo_provedor = models.CharField(max_length=13, default='NACIONAL')
    moneda_transaccion = models.CharField(max_length=10)
    categoria = models.CharField(max_length=250)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    id_user = models.SmallIntegerField(blank=True, null=True, default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre

    class Meta:
        #managed = False
        managed = True
        db_table = 'proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['tipo_provedor', 'nombre']
    
    @classmethod
    def get_all(self):
        return self.objects.all()

    @classmethod
    def get_by_ruc(self, id_supplier):
        try:
            return self.objects.get(pk=id_supplier)
        except ObjectDoesNotExist:
            return None 
