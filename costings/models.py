from django.db import models

class Ledger(models.Model):
    id_mayor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    nro_pedido = models.CharField(max_length=6)
    id_parcial = models.PositiveSmallIntegerField(default=0)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    valor_inicial_facturado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    saldo_inicial_facturado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    valor_distribuido = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    valor_distribuido_facturado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    saldo_distribuido_facturado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    valor_por_distribuir = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'mayor'
        unique_together = (('nro_pedido', 'id_parcial', 'name'),)
        verbose_name_plural = 'Mayores Liquidaciones'
        ordering = ['nro_pedido', 'id_parcial','name','tipo']
    
    @classmethod
    def get_by_order(self):
        return None
