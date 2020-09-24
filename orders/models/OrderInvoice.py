from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models.Order import Order
from suppliers.models.Supplier import Supplier


class OrderInvoice(models.Model):
    id_pedido_factura = models.AutoField(primary_key=True)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    nro_pedido = models.ForeignKey(Order, models.PROTECT, db_column='nro_pedido')
    id_factura_proveedor = models.CharField(max_length=16)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    fecha_emision = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=20, decimal_places=13, blank=True, null=True)
    fob_tasa_trimestral = models.DecimalField(max_digits=20, decimal_places=13, blank=True, null=True)
    moneda = models.CharField(max_length=45, default="DOLARES")
    tipo_cambio = models.DecimalField(max_digits=20, decimal_places=13, default=1)
    vencimiento_pago = models.DateField(blank=True, null=True, default=None)
    fecha_pago = models.DateField(blank=True, null=True, default=None)
    id_user = models.SmallIntegerField(blank=True, null=True, default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    bg_isclosed = models.IntegerField(blank=True, null=True,default=0)
    bg_audit = models.IntegerField(default=0)
    bg_isrejected = models.IntegerField(default=0)
    audit_date = models.DateTimeField(blank=True, null=True)
    audit_user = models.SmallIntegerField(default=0, blank=True, null=True)
    gasto_origen = models.DecimalField(max_digits=20, decimal_places=13,default=0)
    gasto_origen_tasa_trimestral = models.DecimalField(max_digits=20, decimal_places=13, blank=True, null=True)
    factura_proveedor = models.FileField(blank=True,null=True, upload_to='factura_proveedor/'),
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
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
    def user(self):
        '''Retorna el objeto usuario del auditor'''
        if self.audit_user:
            try:
                return User.objects.get(pk=self.audit_user)
            except ObjectDoesNotExist:
                return None

        return None

    @property
    def valor_tasa_trimestral(self):
        return (self.valor * self.tipo_cambio)

    @property
    def days(self):
        today = date.today()
        diff_date = today - self.fecha_emision
        return diff_date.days

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

    @classmethod
    def get_authorized_by_audit(cls):
        '''Facturas Aprobadas'''
        result = cls.objects.filter(bg_audit=1)
        result.exclude(id_factura_proveedor__startswith = 'SF-')
        return result

    @classmethod
    def get_deny_by_audit(cls):
        '''Facturas pendientes de aprobacion'''
        result = cls.objects.filter(bg_audit=0)
        return result.exclude(id_factura_proveedor__startswith = 'SF-')
