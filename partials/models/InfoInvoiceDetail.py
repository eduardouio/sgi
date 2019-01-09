from django.db import models

from logs.app_log import loggin
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from partials.models.InfoInvoice import InfoInvoice
from simple_history.models import HistoricalRecords


class InfoInvoiceDetail(models.Model):
    id_factura_informativa_detalle = models.AutoField(primary_key=True)
    id_factura_informativa = models.ForeignKey(InfoInvoice, models.PROTECT, db_column='id_factura_informativa')
    detalle_pedido_factura = models.ForeignKey(OrderInvoiceDetail, models.PROTECT, db_column='detalle_pedido_factura')

    arancel_advalorem = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem_liberado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem_pagar = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_advalorem_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico_liberado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico_pagar = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    arancel_especifico_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    base_advalorem = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    base_ice_epecifico = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    cajas_importadas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    cantidad_x_caja = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    capacidad_ml = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    cif = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    cod_contable = models.CharField(max_length=20, blank=True, null=True)
    costo_botella = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_caja = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_caja_final = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_unidad = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    etiquetas_fiscales = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ex_aduana = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    ex_aduana_unitario = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    ex_aduana_antes = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    ex_aduana_antes_unitario = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    exaduana_sin_etiquetas = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    exaduana_sin_tasa = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    flete = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    flete_aduana = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fob = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fob_tasa_trimestral = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fob_percent = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    fodinfa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    gasto_origen = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    gasto_origen_tasa_trimestral = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    grado_alcoholico = models.DecimalField(max_digits=5, decimal_places=3)
    ice_advalorem = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_reliquidado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_diferencia = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_pagado = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_sin_etiquetas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_sin_tasa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_advalorem_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_especifico = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_especifico_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    ice_unitario = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    id_parcial = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    indirectos = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva_unidad = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    nro_cajas = models.DecimalField(max_digits=15, decimal_places=7)    
    nro_factura_informativa = models.CharField(max_length=10, blank=True, null=True)
    nro_pedido = models.CharField(max_length=10, blank=True, null=True)
    otros = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    peso = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    product = models.CharField(max_length=200, blank=True, null=True)
    prorrateo_parcial = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    prorrateo_pedido = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    prorrateos_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    seguro = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    seguro_aduana = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    tasa_control = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    total_ice = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    unidades = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    unidades_importadas = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nro_factura_informativa

    class Meta:
        #managed = False
        managed = True
        db_table = 'factura_informativa_detalle'
        unique_together = (('id_factura_informativa', 'detalle_pedido_factura', 'date_create'),)
        verbose_name_plural = 'Factura Informativa Detalle'
        ordering = ['id_factura_informativa']
    
    @classmethod
    def get_by_info_invoice(self, info_invoice):
        info_invoice_items = self.objects.filter(id_factura_informativa=info_invoice.id_factura_informativa)
        if info_invoice_items.count() == 0:
            loggin('w', 'La factura informativa {id_info_invoice} no tiene detalles'.format(id_info_invoice=info_invoice.id_factura_informativa))
            return None
        
        return info_invoice_items
