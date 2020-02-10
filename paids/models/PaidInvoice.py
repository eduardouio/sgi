import pdb

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs import loggin
from paids.models import Expense
from suppliers.models import Supplier


class PaidInvoice(models.Model):
    id_documento_pago = models.AutoField(primary_key=True)
    identificacion_proveedor = models.ForeignKey(Supplier, models.PROTECT, db_column='identificacion_proveedor')
    nro_factura = models.CharField(max_length=20)
    fecha_emision = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    saldo = models.DecimalField(max_digits=20, decimal_places=13)
    comentarios = models.TextField(blank=True, null=True)
    comentarios_audit = models.TextField(blank=True, null=True)
    bg_closed = models.IntegerField(default=0)
    bg_audit = models.IntegerField(default=0)
    bg_isrejected = models.IntegerField(default=0)
    audit_date = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=8)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_documento_pago)

    class Meta:
        managed = True
        db_table = 'documento_pago'
        unique_together = (('identificacion_proveedor', 'nro_factura'),)
        ordering = ['nro_factura']
        verbose_name_plural = 'Facturas Servicios'
    

    @classmethod
    def  get_by_id(self, id_invoice):        
        try:
            invoice = self.objects.get(pk = id_invoice)
        except ObjectDoesNotExist:
            loggin('w', 'No se puede encontrar la factura {id_invoice}'.format(id_invoice=id_invoice))
            return None
        
        return invoice

    
    @classmethod
    def get_autorized_by_audit(self):
        ''' facturas aprobadas por auditoria'''
        autorized_invoices = self.objects.filter(bg_audit = 1)
        return autorized_invoices
    

    @classmethod
    def get_deny_by_audit(self):
        ''' Obtiene la lista de factura no apobadas por audotiria'''
        deny_invoices = self.objects.filter(bg_audit = 0)
        return deny_invoices