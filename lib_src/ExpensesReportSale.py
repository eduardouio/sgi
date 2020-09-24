from logs import loggin
from paids.models import Expense

from .CompleteOrderInfo import CompleteOrderInfo
from .OrderProductSale import OrderProductSale


class ExpensesReportSale(object):
    """Retorna el saldo de las provisiones iniciales de un pedido
    """
    def __init__(self, nro_order):
        self.nro_order = nro_order
        self.last_partial = None
        self.all_partials = None
    
    def get_sale(self):
        init_expenses = self.get_init_expenses()
        last_apportionment = self.get_last_apportionment()
        last_partial_expenses = self.get_last_partial_expenses()
        saldo = {'saldo' : (
            init_expenses['por_prorratear_gi'] + 
            last_apportionment['almacenjae_pendiente'] + 
            last_apportionment['gasto_origen_prox_parcial'] +
            last_partial_expenses['saldo_inicial_lp'])}
        return { **init_expenses, **last_apportionment, **last_partial_expenses, **saldo }
    
    def get_init_expenses(self):
        '''Obtiene el porcentaje de saldo de los gastos iniciales'''
        expenses_order = Expense.get_all_by_order(self.nro_order)
        order_product_sale = OrderProductSale(self.nro_order)
        sale_order = order_product_sale.get_sale()
        init_expenses_percent = (
            sale_order['sums']['fob_tct_nacionalizado'] 
            / sale_order['sums']['fob_tct_inicial'])

        values = {
            'saldo_inicial_gi': 0,
            'valor_prorrateado_gi' : 0,
            'por_prorratear_gi' : 0,
            }

        for item in expenses_order:
            values['saldo_inicial_gi'] += item.valor_provisionado

        values['valor_prorrateado_gi'] = float((init_expenses_percent * values['saldo_inicial_gi'])).__round__(2)
        values['por_prorratear_gi'] = (float(values['saldo_inicial_gi']) - values['valor_prorrateado_gi']).__round__(2)
        return values

    
    def get_last_apportionment(self):
        '''Obtiene los datos del ultimo prorrateo del sistema'''
        complete_order_info = CompleteOrderInfo().get_data(self.nro_order)
        self.all_partials = complete_order_info['partials']

        if complete_order_info['partials']:
            self.last_partial = complete_order_info['partials'].last()
        lst_apport = complete_order_info['last_apportionment']

        if lst_apport:
            return {
                'almacenjae_pendiente' : float(lst_apport.almacenaje_proximo_parcial).__round__(2),
                'fob_prox_parcial' : float(lst_apport.fob_proximo_parcial).__round__(2),
                'gasto_origen_prox_parcial' : float(lst_apport.gastos_origen_proximo_parcial).__round__(2),
            }
        
        return {
            'almacenjae_pendiente' : 0,
            'fob_prox_parcial' : 0,
            'gasto_origen_prox_parcial' : 0,
        }
    

    def get_last_partial_expenses(self):
        """ Retorna las provisiones de un parcial"""
        partial_expenses = {
            'saldo_inicial_lp': 0,
            'id_parcial' : 0
        }

        if self.last_partial is None:
            return partial_expenses
        partial_expenses['id_parcial'] = self.last_partial.id_parcial

        if self.last_partial.bg_isclosed:
            return partial_expenses

        expenses =  Expense.get_by_parcial(self.last_partial.id_parcial)

        if expenses:
            for exp in expenses:
                partial_expenses['saldo_inicial_lp'] += float(exp.valor_provisionado)
        
        return partial_expenses