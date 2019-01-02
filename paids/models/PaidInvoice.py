from django.db import models
from suppliers.models.Supplier import Supplier
from logs.app_log import loggin
from simple_history.models import HistoricalRecords
from django.core.exceptions import ObjectDoesNotExist

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
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_documento_pago)

    class Meta:
        #managed = False
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