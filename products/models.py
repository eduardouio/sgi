from django.db import models
from suppliers.models import Supplier

class Product(models.Model):
    cod_contable = models.CharField(primary_key=True, max_length=20)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    nombre = models.CharField(unique=True, max_length=70)
    cod_ice = models.CharField(max_length=39, default='000000000000000000000000000000000000000')
    capacidad_ml = models.SmallIntegerField()
    cantidad_x_caja = models.SmallIntegerField()
    grado_alcoholico = models.DecimalField(max_digits=12, decimal_places=3, default=0.00)
    costo_caja = models.DecimalField(max_digits=16, decimal_places=10, default=0.00)
    estado = models.IntegerField(default=1)
    custodia_doble = models.IntegerField(default=0)
    peso = models.DecimalField(max_digits=10, decimal_places=3)
    pais_origen = models.CharField(max_length=70, blank=True, null=True)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    id_user = models.SmallIntegerField()
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'producto'
        ordering = ['identificacion_proveedor', 'nombre']
        verbose_name_plural = 'Productos'
