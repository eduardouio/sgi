from .CompleteOrderInfo import CompleteOrderInfo
from paids.models import Expense

from .OrderProductSale import OrderProductSale


class ExpensesReportSale(object):
    """Retorna el saldo de las provisiones iniciales de un pedido
    """
    def __init__(self):
        self.last_partial = None
    
    def get(self, nro_order):
        
        return {
            'init_expenses' : self.get_init_expenses(nro_order),
            'ultimo_prorrateo': self.get_last_apportionment(nro_order),
            'ultimo_parcial' : self.last_partial,
            'gastos_parcial' : self.get_partial_expenses(),
        }
    
    def get_init_expenses(self, nro_order):
        '''Obtiene el porcentaje de saldo de los gastos iniciales'''
        expenses_order = Expense.get_all_by_order(nro_order)
        sale_order = OrderProductSale().get(nro_order)

        expenses = []
        for item in expenses_order:
            expenses.append({
                'gasto' : item.concepto,
                'valor_provisionado' : item.valor_provisionado,
                'valor_utilizado' : item.valor_provisionado * sale_order['sums']['porcentaje'],
                'valor_saldo' : item.valor_provisionado - (item.valor_provisionado * sale_order['sums']['porcentaje']),
            })

        sums = {
            'valor_provisionado': 0,
            'valor_utilizado': 0,
            'valor_saldo' : 0,
        }

        for item in expenses:
            sums['valor_provisionado'] += item['valor_provisionado']
            sums['valor_utilizado'] += item['valor_utilizado']
            sums['valor_saldo'] += item['valor_saldo']

        return {
            'expenses' : expenses,
            'valor_provisionado': sums['valor_provisionado'],
            'valor_utilizado': sums['valor_utilizado'],
            'valor_saldo' : sums['valor_saldo'],
        }

    
    def get_last_apportionment(self, nro_order):
        '''Obtiene los datos del ultimo prorrateo del sistema'''
        complete_order_info = CompleteOrderInfo().get_data(nro_order)

        if complete_order_info['partials']:
            self.last_partial = complete_order_info['partials'].last()

        return complete_order_info['last_apportionment']
    

    def get_partial_expenses(self):
        """ Retorna las provisiones de un parcial"""
        if self.last_partial is None:
            return []

        expenses =  Expense.get_by_parcial(self.last_partial.id_parcial)

        if expenses:
            return expenses
        
        return []