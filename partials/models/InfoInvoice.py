from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import QuerySet
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models.Order import Order
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from partials.models.Partial import Partial
from suppliers.models.Supplier import Supplier


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
    factura_informativa = models.FileField(blank=True,null=True, upload_to='factura_informativa/'),
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nro_factura_informativa

    class Meta:
        #managed = False
        managed = True
        db_table = 'factura_informativa'
        ordering = ['fecha_emision', 'id_parcial']
        verbose_name_plural = 'Facturas Infomativas'

    
    @property
    def total_value(self):
        return self.gasto_origen + self.valor
        

    @classmethod
    def get_by_id(self, id_info_invoice):
        try:
            return self.objects.get(pk=id_info_invoice)
        except ObjectDoesNotExist:
            loggin(
                'w', 
                'La factura informativa {} solicitado no existe'
                .format(id_info_invoice)
                )
            return None
        
    @classmethod
    def get_by_order(self, nro_order):
        parcials = Partial.get_by_order(nro_order) 
        infoinvoices = []
        
        if parcials.first() is None:
            loggin('w', 'El pedido {nro_order} no tiente facturas informativas'.format(nro_order=nro_order))
            return None

        for p in parcials:
            infoinvoices.append(self.objects.filter(id_parcial=p))

        return infoinvoices
    

    @classmethod
    def get_by_id_partial(self, id_partial):
        invoices = self.objects.filter(id_parcial = id_partial)

        if invoices.count() == 1:
            loggin(
                'i', 
                'Factura informativa del parcial {} recuperada'
                .format(id_partial)
                )
            return invoices.first()

        loggin(
            'e', 
            'El parcial {id_partial} no tiene facturas informativas, o tiene mas de una'
            .format(id_partial=id_partial)) 
        return None
