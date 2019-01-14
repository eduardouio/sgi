from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models.OrderInvoice import OrderInvoice
from products.models.Product import Product


class OrderInvoiceDetail(models.Model):
    detalle_pedido_factura = models.AutoField(primary_key=True)
    id_pedido_factura = models.ForeignKey(OrderInvoice, models.PROTECT, db_column='id_pedido_factura')
    cod_contable = models.ForeignKey(Product, models.PROTECT, db_column='cod_contable')
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
    costo_botella = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_caja = models.DecimalField(max_digits=16, decimal_places=10)
    costo_caja_final = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    costo_unidad = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
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
    fecha_liquidacion = models.DateField(blank=True, null=True)
    gasto_origen = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    gasto_origen_tasa_trimestral = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    grado_alcoholico = models.FloatField(default=0)
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
    id_user = models.SmallIntegerField(default=0)
    indirectos = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva_total = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    iva_unidad = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    nro_cajas = models.SmallIntegerField(default=0)
    nro_factura_informativa = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
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
    history = HistoricalRecords()

    def __str__(self):
        return str(self.detalle_pedido_factura)

    class Meta:
        #managed = False
        managed = True
        db_table = 'detalle_pedido_factura'
        unique_together = (('id_pedido_factura', 'cod_contable', 'grado_alcoholico', 'date_create'),)
        ordering = ['id_pedido_factura','detalle_pedido_factura']
        verbose_name_plural = 'Detalle Facturas Pedido'


    @classmethod
    def get_by_id_order_invoice(self, id_order_invoice):
        loggin('i', 'Obteniendo la lista completa de los detalles de un pedido')
        order_items =  self.objects.filter(id_pedido_factura = id_order_invoice)

        if order_items.count() == 0:
            loggin('w', 'La factura de producto {id_order_invoice} no tiene items registrados'.format(id_order_invoice=id_order_invoice))
            return []

        for item in order_items:
            if not bool(item.product):
                item.product = item.cod_contable.nombre

        return order_items
    
    @classmethod
    def get_by_id(self, id_order_invoice_detail):
        try:
            return self.objects.get(pk = id_order_invoice_detail)
        except ObjectDoesNotExist:
            loggin(
                'e', 
                'El detalle {} de pedido factura que busca no existe'
                .format(id_order_invoice_detail)
                )
            return None

            

