from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from paids.models import Expense, PaidInvoice


class PaidInvoiceDetail(models.Model):
    id_detalle_documento_pago = models.AutoField(primary_key=True)
    id_gastos_nacionalizacion = models.ForeignKey(Expense, models.PROTECT, db_column='id_gastos_nacionalizacion')
    id_documento_pago = models.ForeignKey(PaidInvoice, models.PROTECT, db_column='id_documento_pago')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    valor_ajuste = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bg_closed = models.IntegerField(default=0)
    bg_isnotprovisioned = models.IntegerField(default=0)
    bg_mayor = models.SmallIntegerField(default=0)
    id_user = models.SmallIntegerField(default=0)
    comentarios = models.TextField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_detalle_documento_pago)

    class Meta:
        managed = True
        db_table = 'detalle_documento_pago'
        unique_together = (('id_documento_pago', 'id_gastos_nacionalizacion'),)
        verbose_name_plural = 'Detalle Documento Pago'

    
    @classmethod
    def get_by_id(self, id_paid_detail):
        try:
            return self.objects.get(pk=id_paid_detail)
        except ObjectDoesNotExist:
            loggin('i', 'El detalle de la factura no existe')
            return None


    @classmethod
    def get_by_expense(self, expense, id_expense=0):
        '''Justificaciones de una provision'''
        if expense:
            paids_detail = self.objects.filter(id_gastos_nacionalizacion = expense.id_gastos_nacionalizacion)
            if paids_detail.count() == 0:
                loggin('w', 'No existe justificaciones para este gasto {expense_concept} {id_expense}'.format(expense_concept = expense.concepto, id_expense=expense.id_gastos_nacionalizacion))
                return []
            return paids_detail
        else:
            paids_detail = self.objects.filter(id_gastos_nacionalizacion = id_expense)
            return list(paids_detail)


    @classmethod
    def get_by_paid_invoice(self, id_paid_invoice):        
        details = self.objects.filter(id_documento_pago = id_paid_invoice)
        if details.count() == 0:
            loggin('w', 'El documento pago {id_paid_invoice} no tiene detalles que presentar'.format(id_paid_invoice = id_paid_invoice))
            return None
        
        return details
    
    
    @classmethod
    def get_invoices_from_expense(self, id_expense):
        '''Lista de facturas para un gasto de nacionalizacion'''
        detail_invoices = self.get_by_expense(False, id_expense)
        invoices = []
        for item in detail_invoices:
            invoices.extend([item.id_documento_pago])

        return invoices

        
    @classmethod
    def get_from_order(self, nro_order):
        '''Listado de facturas de un pedido'''
        order_expenses = Expense.get_complete_expenses(nro_order)
        invoices = []
        index_invoices = set()
        for expense in order_expenses:
            detail = self.get_by_expense(False, expense.id_gastos_nacionalizacion)
            for det in detail:
                index_invoices.add(det.id_documento_pago_id) 
                invoices.extend([det.id_documento_pago])
        
        index_invoices = sorted(index_invoices)
        unique_invoices = []
        for idx in index_invoices:
            for invoice in invoices:
                if invoice.id_documento_pago == idx:
                    unique_invoices.extend([invoice])
                    break
        
        return unique_invoices