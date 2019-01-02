from django.db import models
from simple_history.models import HistoricalRecords    

class Migrations(models.Model):
    nro_pedido = models.CharField(primary_key=True, max_length=6)
    import_status = models.CharField(max_length=10)
    seguro_aduana = models.DecimalField(max_digits=10, decimal_places=3)
    flete_aduana = models.DecimalField(max_digits=10, decimal_places=3)
    pais_origen = models.CharField(max_length=50)
    ciudad_origen = models.CharField(max_length=50)
    moneda = models.CharField(max_length=25)
    tipo_cambio = models.DecimalField(max_digits=10, decimal_places=3)
    proveedor = models.CharField(max_length=150)
    identificacion_proveedor = models.CharField(max_length=15, blank=True, null=True)
    id_factura_proveedor = models.CharField(max_length=45, blank=True, null=True)
    identificacion_proveedor_factura = models.CharField(max_length=15, blank=True, null=True)
    fecha_emision_factura = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento_factura = models.DateTimeField(blank=True, null=True)
    valor_factura = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    observaciones_pedido = models.CharField(max_length=300, blank=True, null=True)
    observaciones_proveedor = models.CharField(max_length=300, blank=True, null=True)
    observaciones_factura = models.CharField(max_length=300, blank=True, null=True)
    regimen = models.CharField(max_length=2, blank=True, null=True)
    incoterm = models.CharField(max_length=3, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    fecha_importacion = models.DateTimeField(blank=True, null=True)
    bg_have_invoice = models.IntegerField(default=0)
    bg_have_order_items = models.IntegerField(default=0)
    bg_have_supplier = models.IntegerField(default=0)
    bg_have_invoice_items = models.IntegerField(default=0)
    bg_exist_in_local = models.IntegerField(default=0)
    bg_supplier_exist_in_local = models.IntegerField(default=0)
    bg_has_imported = models.IntegerField(default=0)
    bg_log = models.TextField(blank=True, null=True)
    bg_migrated_order = models.IntegerField(default=0)
    bg_migrated_order_detail = models.IntegerField(default=0)
    bg_migrated_order_invoice = models.IntegerField(default=0)
    bg_migrated_order_invoice_detail = models.IntegerField()
    last_update = models.DateTimeField(blank=True, null=True)
    gasto_origen = models.DecimalField(max_digits=11, decimal_places=3, blank=True, null=True)
    docentry = models.IntegerField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return ''.join([self.nro_pedido, ' -> ', self.proveedor ])

    class Meta:
        #managed = False
        managed = True
        db_table = 'migracion'
        verbose_name_plural = 'Cabeceras Migraciones SAP'
        ordering = ['nro_pedido']


class MigrationsDetail(models.Model):
    id_migracion_detalle = models.AutoField(primary_key=True)
    nro_pedido = models.ForeignKey(Migrations, models.PROTECT, db_column='nro_pedido')
    cod_contable = models.CharField(max_length=20)
    identificacion_proveedor = models.CharField(max_length=16)
    cod_ice = models.CharField(max_length=39)
    nombre = models.CharField(max_length=70)
    nro_cajas = models.IntegerField(blank=True, null=True)
    capacidad_ml = models.SmallIntegerField()
    cantidad_x_caja = models.SmallIntegerField()
    grado_alcoholico = models.FloatField()
    costo_caja = models.DecimalField(max_digits=16, decimal_places=10)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    bg_product_exist_in_local = models.IntegerField()
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_migracion_detalle)

    class Meta:
        #managed = False
        managed = True
        db_table = 'migracion_detalle'
        verbose_name_plural = 'Detalle Migraciones SAP'
        ordering = ['nro_pedido','id_migracion_detalle']
