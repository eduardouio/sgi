from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models.OrderInvoice import OrderInvoice
from products.models.Product import Product


class OrderInvoiceDetail(models.Model):
    detalle_pedido_factura = models.AutoField(primary_key=True)
    id_pedido_factura = models.ForeignKey(OrderInvoice, models.PROTECT, db_column='id_pedido_factura')
    cod_contable = models.ForeignKey(Product, models.PROTECT, db_column='cod_contable')
    arancel_advalorem = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_advalorem_liberado = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_advalorem_pagar = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_advalorem_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_especifico = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_especifico_liberado = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_especifico_pagar = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    arancel_especifico_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    base_advalorem = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    base_advalorem_reliquidado = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    base_ice_epecifico = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    cajas_importadas = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    cantidad_x_caja = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    capacidad_ml = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    cif = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    costo_botella = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    costo_caja = models.DecimalField(max_digits=20, decimal_places=13)
    costo_caja_final = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    costo_total = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    costo_unidad = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    etiquetas_fiscales = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ex_aduana = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ex_aduana_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ex_aduana_antes = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ex_aduana_antes_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    exaduana_sin_etiquetas = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    exaduana_sin_tasa = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    flete = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    flete_aduana = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    fob = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    fob_tasa_trimestral = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    fob_percent = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    fodinfa = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    gasto_origen = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    gasto_origen_tasa_trimestral = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    grado_alcoholico = models.FloatField(default=0)
    ice_advalorem = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_advalorem_reliquidado = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_advalorem_diferencia = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_advalorem_pagado = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_advalorem_sin_etiquetas = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_advalorem_sin_tasa = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_advalorem_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_especifico = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_especifico_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    ice_unitario = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    id_parcial = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    id_user = models.SmallIntegerField(default=0)
    indirectos = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    iva_total = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    iva_unidad = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    last_update = models.DateTimeField(blank=True, null=True)
    nro_cajas = models.SmallIntegerField(default=0)
    nro_factura_informativa = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    nro_pedido = models.CharField(max_length=10, blank=True, null=True)
    otros = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    peso = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    product = models.CharField(max_length=200, blank=True, null=True)
    prorrateo_parcial = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    prorrateo_pedido = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    prorrateos_total = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    seguro = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    seguro_aduana = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    tasa_control = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    total_ice = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    unidades = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    unidades_importadas = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.detalle_pedido_factura)

    class Meta:
        managed = True
        db_table = 'detalle_pedido_factura'
        unique_together = (
            ('id_pedido_factura', 
            'cod_contable', 
            'grado_alcoholico', 
            'date_create'),
            )
        ordering = ['id_pedido_factura','detalle_pedido_factura']
        verbose_name_plural = 'Detalle Facturas Pedido'


    @classmethod
    def get_by_id_order_invoice(self, id_order_invoice):
        loggin(
            'i', 
            'Obteniendo la lista completa de los detalles de un pedido'
            )
        order_items =  self.objects.filter(id_pedido_factura = id_order_invoice)

        if order_items.count() == 0:
            loggin(
                'w', 'La factura {id_order_invoice} no tiene items'
                .format(id_order_invoice=id_order_invoice))

            return []

        for item in order_items:
            if not bool(item.product):
                item.product = item.cod_contable.nombre
            if item.unidades == 0 :
                item.unidades = (item.nro_cajas * item.cantidad_x_caja)

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
    
    @classmethod
    def get_by_order(self, nro_order):
        """Otiene los productos de un pedido 
        
        Arguments:
            nro_order {string} -- Nro de pedido
        """
        order_invoice = OrderInvoice.get_by_order(nro_order)
        if order_invoice is None:
            loggin('e', 
            'le pedido {}, no tiene facturas registradas'.format(nro_order))
            return None
        
        return self.get_by_id_order_invoice(order_invoice.id_pedido_factura)


