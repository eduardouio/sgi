from django.db import models
from suppliers.models import Supplier
from orders.models import Order

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

    def __str__(self):
        return ''.join([self.concepto ,' ', self.regimen])

    class Meta:
        managed = False
        db_table = 'tarifa_gastos'
        unique_together = (('identificacion_proveedor', 'concepto', 'pais_origen', 'valor', 'tipo_gasto'),)
        ordering = ['identificacion_proveedor','regimen','concepto','valor']
        verbose_name_plural = 'Tarias Gastos'


class RateIncoterm(models.Model):
    id_incoterm = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=12)
    pais = models.CharField(max_length=45)
    incoterms = models.CharField(max_length=4)
    ciudad = models.CharField(max_length=45)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return ''.join([self.tipo, ' ', self.pais, ' ', self.incoterms])

    class Meta:
        managed = False
        db_table = 'tarifa_incoterm'
        unique_together = (('pais', 'ciudad', 'incoterms', 'tipo'),)
        ordering = ['tipo','pais','ciudad','incoterms']
        verbose_name_plural = 'Tarias Incoterms'


class Expenses(models.Model):
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
        ordering = ['nro_pedido','id_parcial','tipo','concepto']
        verbose_name_plural = 'Gastos Nacionalizacion'


class PaidInvoice(models.Model):
    id_documento_pago = models.SmallIntegerField( primary_key=True)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    nro_factura = models.CharField(max_length=20)
    fecha_emision = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    saldo = models.DecimalField(max_digits=16, decimal_places=3)
    comentarios = models.CharField(max_length=250)
    bg_closed = models.IntegerField(default=0)
    tipo = models.CharField(max_length=8)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id_documento_pago)

    class Meta:
        managed = False
        db_table = 'documento_pago'
        unique_together = (('identificacion_proveedor', 'nro_factura'),)
        ordering = ['nro_factura']
        verbose_name_plural = 'Facturas Servicios'


class PaidInvoiceDetail(models.Model):
    id_detalle_documento_pago = models.AutoField(primary_key=True)
    id_gastos_nacionalizacion = models.ForeignKey(Expenses, models.PROTECT, db_column='id_gastos_nacionalizacion')
    id_documento_pago = models.ForeignKey(PaidInvoice, models.PROTECT, db_column='id_documento_pago')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    bg_closed = models.IntegerField(default=0)
    bg_isnotprovisioned = models.IntegerField(default=0)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id_detalle_documento_pago)

    class Meta:
        managed = False
        db_table = 'detalle_documento_pago'
        unique_together = (('id_documento_pago', 'id_gastos_nacionalizacion'),)
        verbose_name_plural = 'Detalle Documento Pago'
