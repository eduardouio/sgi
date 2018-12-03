from django.db import models
from orders.models import Order, OrderInvoiceDetail
from suppliers.models import Supplier

class Partial(models.Model):
    id_parcial = models.PositiveSmallIntegerField(primary_key=True)
    nro_pedido = models.ForeignKey(Order,models.PROTECT, db_column='nro_pedido')
    tipo_cambio = models.DecimalField(max_digits=15, decimal_places=10, default=1)
    fecha_nacionalizacion = models.DateField(blank=True, null=True)    
    bg_isclosed = models.IntegerField(blank=True, null=True, default=0)
    fecha_salida_almacenera = models.DateField(blank=True, null=True)
    proximo_almacenaje_desde = models.DateField(blank=True, null=True)
    otros = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    exoneracion_arancel = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    bg_have_etiquetas_fiscales = models.IntegerField(default=0, blank=True, null=True)
    bg_isliquidated = models.IntegerField(blank=True, null=True)
    bg_have_tasa_control = models.IntegerField(blank=True, null=True)
    fodinfa = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    fodinfa_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_advalorem = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_advalorem_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_especifico = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    ice_especifico_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iva = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    iva_pagado = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar_pagado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    liquidacion_con_tasa = models.IntegerField(blank=True, null=True)
    base_arancel_advalorem = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_arancel_especifico = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_ice_especifico = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_ice_advalorem = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    porcentaje_ice_advalorem = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_iva = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_fodinfa = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    base_etiquetas = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)
    arancel_especifico_pagar = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    arancel_especifico_pagar_pagado = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    nro_liquidacion = models.CharField(max_length=22, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    id_user_cierre = models.PositiveSmallIntegerField(blank=True, null=True)
    fecha_llegada_cliente = models.DateField(blank=True, null=True)
    notas_cierre = models.CharField(max_length=200, blank=True, null=True)
    fecha_salida_autorizada_almagro = models.DateTimeField(blank=True, null=True)
    url_dai_1 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_2 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_3 = models.CharField(max_length=600, blank=True, null=True)
    path_dai_1 = models.FileField(upload_to='dais_parciales/', max_length=600, blank=True, null=True)
    path_dai_2 = models.FileField(upload_to='dais_parciales/', max_length=600, blank=True, null=True)
    path_dai_3 = models.FileField(upload_to='dais_parciales/', max_length=600, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id_parcial)

    class Meta:
        managed = False
        db_table = 'parcial'
        verbose_name_plural = 'Parciales'
        ordering = ['nro_pedido', 'id_parcial']



class Apportionment(models.Model):
    id_prorrateo = models.AutoField(primary_key=True)
    id_parcial = models.ForeignKey(Partial, models.PROTECT, db_column='id_parcial')
    porcentaje_parcial = models.DecimalField(max_digits=15, decimal_places=12)
    fob_parcial_razon_inicial = models.DecimalField(max_digits=17, decimal_places=3)
    fob_parcial_razon_saldo = models.DecimalField(max_digits=17, decimal_places=3)
    fob_proximo_parcial = models.DecimalField(max_digits=10, decimal_places=3)
    fob_inicial = models.DecimalField(max_digits=16, decimal_places=3)
    fob_saldo = models.DecimalField(max_digits=16, decimal_places=3)
    fob_parcial = models.DecimalField(max_digits=10, decimal_places=3)
    almacenaje_parcial = models.DecimalField(max_digits=15, decimal_places=10)
    almacenaje_anterior = models.DecimalField(max_digits=15, decimal_places=10)
    almacenaje_aplicado = models.DecimalField(max_digits=16, decimal_places=3)
    almacenaje_proximo_parcial = models.DecimalField(max_digits=16, decimal_places=3)
    prorrateo_flete_aduana = models.DecimalField(max_digits=15, decimal_places=10)
    prorrateo_seguro_aduana = models.DecimalField(max_digits=15, decimal_places=10)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id_prorrateo)

    class Meta:
        managed = False
        db_table = 'prorrateo'
        verbose_name_plural = 'Prorrateos De Parciales'
        ordering = ['id_parcial']


class ApportionmentDetail(models.Model):
    id_prorrateo_detalle = models.AutoField(primary_key=True)
    id_prorrateo = models.ForeignKey(Apportionment, models.PROTECT, db_column='id_prorrateo')
    id_gastos_nacionalizacion = models.PositiveIntegerField()
    tipo = models.CharField(max_length=13)
    concepto = models.CharField(max_length=90)
    valor_prorrateado = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    valor_provisionado = models.DecimalField(max_digits=17, decimal_places=3)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id_prorrateo)

    class Meta:
        managed = False
        db_table = 'prorrateo_detalle'
        unique_together = (('id_gastos_nacionalizacion', 'id_prorrateo'),)
        verbose_name_plural = 'Detalle de Prorrateos'
        ordering = ['id_prorrateo', 'concepto']


class InfoInvoice(models.Model):
    id_factura_informativa = models.AutoField(primary_key=True)
    id_parcial = models.ForeignKey(Partial, models.PROTECT, db_column='id_parcial')
    nro_factura_informativa = models.CharField(unique=True, max_length=8)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    fecha_emision = models.DateField()
    flete_aduana = models.DecimalField(max_digits=8, decimal_places=2)
    seguro_aduana = models.DecimalField(max_digits=8, decimal_places=2)
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=45)
    nro_refrendo = models.CharField(max_length=22, blank=True, null=True)
    tipo_cambio = models.DecimalField(max_digits=16, decimal_places=12)    
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    bg_isclosed = models.IntegerField(default=0)
    gasto_origen = models.DecimalField(max_digits=10, decimal_places=3)
    bg_gst_origen_por_factura = models.IntegerField()
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nro_factura_informativa

    class Meta:
        managed = False
        db_table = 'factura_informativa'
        ordering = ['fecha_emision', 'id_parcial']
        verbose_name_plural = 'Facturas Infomativas'


class InfoInvoiceDetail(models.Model):
    id_factura_informativa_detalle = models.AutoField(primary_key=True)
    id_factura_informativa = models.ForeignKey(InfoInvoice, models.PROTECT, db_column='id_factura_informativa')
    grado_alcoholico = models.DecimalField(max_digits=5, decimal_places=3)
    detalle_pedido_factura = models.ForeignKey(OrderInvoiceDetail, models.PROTECT, db_column='detalle_pedido_factura')
    nro_cajas = models.DecimalField(max_digits=15, decimal_places=7)    
    product = models.CharField(max_length=200, blank=True, null=True)
    cod_contable = models.CharField(max_length=20, blank=True, null=True)
    nro_factura_informativa = models.CharField(max_length=10, blank=True, null=True)
    cantidad_x_caja = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    cajas_importadas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    unidades_importadas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    unidades = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_caja = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_unidad = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    peso = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    capacidad_ml = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fob = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fob_percent = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    seguro_aduana = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    flete_aduana = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    seguro = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    flete = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    gasto_origen = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    cif = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fecha_liquidacion = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nro_pedido = models.CharField(max_length=10, blank=True, null=True)
    id_parcial = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    otros = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    prorrateo_parcial = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    prorrateo_pedido = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    prorrateos_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    tasa_control = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fodinfa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva_unidad = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ex_aduana = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ex_aduana_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    exaduana_sin_etiquetas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    exaduana_sin_tasa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    base_advalorem = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    base_ice_epecifico = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_especifico = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_especifico_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_sin_tasa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_sin_etiquetas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico_liberado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem_liberado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico_pagar = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    etiquetas_fiscales = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    total_ice = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_pagado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_diferencia = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    indirectos = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_caja_final = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_botella = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ex_aduana_antes = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nro_factura_informativa

    class Meta:
        managed = False
        db_table = 'factura_informativa_detalle'
        unique_together = (('id_factura_informativa', 'detalle_pedido_factura', 'date_create'),)
        verbose_name_plural = 'Factura Informativa Detalle'
        ordering = ['id_factura_informativa']