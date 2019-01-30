from django.db import models
from partials.models.Apportionment import Apportionment
from logs.app_log import loggin
from simple_history.models import HistoricalRecords

class ApportionmentDetail(models.Model):
    id_prorrateo_detalle = models.AutoField(primary_key=True)
    id_prorrateo = models.ForeignKey(Apportionment, models.CASCADE, db_column='id_prorrateo')
    id_gastos_nacionalizacion = models.PositiveIntegerField()
    tipo = models.CharField(max_length=13)
    concepto = models.CharField(max_length=90)
    valor_prorrateado = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    valor_provisionado = models.DecimalField(max_digits=17, decimal_places=3)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_prorrateo)

    class Meta:
        #managed = False
        managed = True
        db_table = 'prorrateo_detalle'
        unique_together = (('id_gastos_nacionalizacion', 'id_prorrateo'),)
        verbose_name_plural = 'Detalle de Prorrateos'
        ordering = ['id_prorrateo', 'concepto']


    @classmethod
    def get_by_apportionment(self, id_apportionment):
        details = self.objects.filter(id_prorrateo = id_apportionment)
        if details.count() == 0:
            loggin('w', 'El prorrateo {id_prorrateo} no tiene detalles'.format(id_prorrateo=id_apportionment))
            return None
        
        return details
    

    @classmethod
    def get_all_apportionments_by_parcial(self, id_partial):
        apportionment = {}
        apportionment['apportionment'] = Apportionment.get_by_parcial(id_partial)
        
        if apportionment['apportionment'] is None:
            loggin('i', 'El parcial {} no tiene prorrateos'.format(id_partial))
            return None
        
        apportionment['apportionment_detail'] = self.get_by_apportionment(
            apportionment['apportionment'].id_prorrateo
            )
        
        apportionment['total_provisionado']  = 0
        apportionment['total_aplicado']  = 0
        
        return apportionment