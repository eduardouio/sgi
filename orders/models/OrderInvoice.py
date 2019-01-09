from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from orders.models.Order import Order
from suppliers.models.Supplier import Supplier
from logs.app_log import loggin
from simple_history.models import HistoricalRecords

class OrderInvoice(models.Model):
    id_pedido_factura = models.AutoField(primary_key=True)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    nro_pedido = models.ForeignKey(Order, models.PROTECT, db_column='nro_pedido')
    id_factura_proveedor = models.CharField(max_length=16)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fob_tasa_trimestral = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    moneda = models.CharField(max_length=45)
    tipo_cambio = models.DecimalField(max_digits=16, decimal_places=12)
    vencimiento_pago = models.DateField(blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    bg_isclosed = models.IntegerField(blank=True, null=True,default=0)
    gasto_origen = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    gasto_origen_tasa_trimestral = models.DecimalField(max_digits=12, decimal_places=3, blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_factura_proveedor)

    class Meta:
        #managed = False
        managed = True
        db_table = 'pedido_factura'
        unique_together = (('identificacion_proveedor', 'id_factura_proveedor'),)
        verbose_name_plural = 'Facturas de Pedido'  

    @property
    def valor_tasa_trimestral(self):
        return (self.valor * self.tipo_cambio)


    @classmethod
    def get_by_id(self, id_invoice):
        try:
            return self.objects.get(pk=id_invoice)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_by_order(self, nro_order):
        order_invoice = self.objects.filter(nro_pedido = nro_order)
        if order_invoice.count() == 0:
            loggin('w', 'No existe facturas para el pedido {nro_order}'.format(nro_order=nro_order))
            return None
        
        if order_invoice.count() > 1:
            loggin('e', 'Existe mas de una factura para el pedido {nro_order}'.format(nro_order=nro_order))

        return order_invoice.first()