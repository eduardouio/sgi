from django.views.generic import TemplateView
from lib_src import ExpensesWithSale
from paids.models import PaidInvoice, PaidInvoiceDetail, Expense
from random import randint
from datetime import date
from logs.app_log import loggin
from suppliers.models import Supplier


#/reportes/provisiones/
class ExpensesReportTemplateView(TemplateView):
    template_name = 'reports/report-expenses.html'

    def get(self, request, *args, **kwargs):
        loggin('i', 'Recuperando provisiones pendientes')
        expenses = ExpensesWithSale().get_all_expeneses_with_sale()
        context = self.get_context_data(**kwargs)
        context['data'] = {
            'title_page': 'Reporte de Provisiones Pendientes',
            'expenses': expenses
        }
        #codigo usado para cerrar las provisiones pendientes
        self.closed_expenses(expenses)
        return self.render_to_response(context=context)
    
    def closed_expenses(self, expenses):
         for exp in expenses:
            expense = Expense.get_by_id_expense(exp['id_gastos_nacionalizacion'])
            supplier = Supplier.get_by_ruc('1790023516001')
            invoice = PaidInvoice(
                identificacion_proveedor=supplier,
                nro_factura='C' + str(randint(10000,999999)),
                fecha_emision=date.today(),
                valor=exp['saldo'],
                saldo=0,
                comentarios='Factura creada para cierre de ajuste',
                bg_closed=1,
                id_user=1,
            )
            invoice.save()
            invoice_detail = PaidInvoiceDetail(
                id_gastos_nacionalizacion=expense,
                id_documento_pago=invoice,
                valor=exp['saldo'],
                bg_closed=1,
                id_user=1,
                comentarios='cruce por ajuste de factura propia'
            )
            invoice_detail.save()
            expense.bg_closed=1
            expense.save()
