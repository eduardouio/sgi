from django.db import models
from paids.models.PaidInvoice import PaidInvoice
from paids.models.Expense import Expense
from logs.app_log import loggin

class PaidInvoiceDetail(models.Model):
    id_detalle_documento_pago = models.AutoField(primary_key=True)
    id_gastos_nacionalizacion = models.ForeignKey(Expense, models.PROTECT, db_column='id_gastos_nacionalizacion')
    id_documento_pago = models.ForeignKey(PaidInvoice, models.PROTECT, db_column='id_documento_pago')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    bg_closed = models.IntegerField(default=0)
    bg_isnotprovisioned = models.IntegerField(default=0)
    bg_mayor = models.SmallIntegerField(default=0)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id_detalle_documento_pago)

    class Meta:
        managed = False
        db_table = 'detalle_documento_pago'
        unique_together = (('id_documento_pago', 'id_gastos_nacionalizacion'),)
        verbose_name_plural = 'Detalle Documento Pago'

    @classmethod
    def get_by_expense(self, expense):
        paids_detail = self.objects.filter(id_gastos_nacionalizacion = expense.id_gastos_nacionalizacion)
        
        if paids_detail.count() == 0:
            loggin('w', 'No existe justificaciones para este gasto {expense_concept} {id_expense}'.format(expense_concept = expense.concepto, id_expense=expense.id_gastos_nacionalizacion))
            return []

        return paids_detail