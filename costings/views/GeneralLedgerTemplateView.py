from django.views.generic import TemplateView

from lib_src import ExpenseSerializer, OrderProductSale, ExpensesReportSale
from orders.models import Order


#costos/mayor/
class GeneralLedgerTemplateView(TemplateView):
    """Imprime todos los ingresos de un mayor"""
    template_name = 'costings/ingresos_mayor.html'

    def get(self, requets, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        data = []
        orders = Order.objects.all()
        for item in orders:
            if item.nro_pedido == '000-00':
                continue

            expenses = ExpensesReportSale().get(item.nro_pedido)
            data.append(
                self.get_totals_from_orders(
                        item.nro_pedido,
                        OrderProductSale().get(item.nro_pedido),
                        expenses['init_expenses'],
                        expenses['partial_expenses']
                ))
            break
            
        context['data'] = {
            'orders' : data,
        }

        return self.render_to_response(context)
    

    def get_totals_from_orders(self, nro_order, product, init_expenses, partials):
        ''' Get sums from invoices and products '''
        complete_data = {
            'nro_pedido' : nro_order,
            'product' :  product['sums']['fob_tct'],
            'invoices' : init_expenses['valor_provisionado'],
        }

        if partials:
            for item in partials:
                pass

        
        return complete_data