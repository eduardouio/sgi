from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.fields import FloatField
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from partials.models.InfoInvoice import InfoInvoice


class InfoInvoiceDetail(models.Model):
    id_factura_informativa_detalle = models.AutoField(primary_key=True)
    id_factura_informativa = models.ForeignKey(InfoInvoice, models.PROTECT, db_column='id_factura_informativa')
    detalle_pedido_factura = models.ForeignKey(OrderInvoiceDetail, models.PROTECT, db_column='detalle_pedido_factura')
    arancel_advalorem = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_advalorem_liberado = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_advalorem_pagar = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_advalorem_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_especifico = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_especifico_liberado = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_especifico_pagar = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    arancel_especifico_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    base_advalorem = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    base_advalorem_reliquidado = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    base_ice_epecifico = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    cajas_importadas = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    cantidad_x_caja = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    capacidad_ml = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    cif = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    cod_contable = models.CharField(max_length=20, blank=True, null=True)
    costo_botella = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    costo_caja = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    costo_caja_final = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    costo_total = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    costo_unidad = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    etiquetas_fiscales = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ex_aduana = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ex_aduana_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ex_aduana_antes = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ex_aduana_antes_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    exaduana_sin_etiquetas = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    exaduana_sin_tasa = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    flete = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    flete_aduana = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    fob = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    fob_tasa_trimestral = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    fob_percent = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    fodinfa = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    gasto_origen = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    gasto_origen_tasa_trimestral = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    grado_alcoholico = models.DecimalField(max_digits=12, decimal_places=5, default=0)
    ice_advalorem = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_advalorem_reliquidado = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_advalorem_diferencia = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_advalorem_pagado = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_advalorem_sin_etiquetas = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_advalorem_sin_tasa = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_advalorem_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_especifico = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_especifico_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    ice_unitario = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    id_parcial = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    indirectos = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    iva_total = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    iva_unidad = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    nro_cajas = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    nro_factura_informativa = models.CharField(max_length=10, blank=True, null=True)
    nro_pedido = models.CharField(max_length=10, blank=True, null=True)
    otros = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    peso = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    product = models.CharField(max_length=200, blank=True, null=True)
    prorrateo_parcial = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    prorrateo_pedido = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    prorrateos_total = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    seguro = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    seguro_aduana = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    tasa_control = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    total_ice = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    unidades = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    unidades_importadas = models.DecimalField(max_digits=20, decimal_places=13, default=0)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_factura_informativa)

    class Meta:
        #managed = False
        managed = True
        db_table = 'factura_informativa_detalle'
        unique_together = (('id_factura_informativa', 'detalle_pedido_factura', 'date_create'),)
        verbose_name_plural = 'Factura Informativa Detalle'
        ordering = ['id_factura_informativa']


    @property
    def cantidad_x_caja(self):
        return self.detalle_pedido_factura.cantidad_x_caja

    @classmethod
    def get_by_info_invoice(self, id_info_invoice):
        info_invoice_items = self.objects.filter(id_factura_informativa=id_info_invoice)
        if info_invoice_items.count() == 0:
            loggin(
                'w', 
                'La factura informativa {} no tiene detalles'
                .format(id_info_invoice)
                )
            return self.objects.none()
        

        return info_invoice_items