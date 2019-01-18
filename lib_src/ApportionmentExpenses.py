from logs.app_log import loggin

class ApportionmentExpenses(object):
    '''
    [sumary]
    Obtiene el prorrateo de gastos que se aplican al pedido, pasando por los
        gastos iniciales prorrateo de acuerdo a fob parcial y luego fob item
        gastos parcial prorrateo al cien al parcial y luego al fob del item
        gastos de arrastre de acuerdo al saldo del fob general (warenhouse y gastos omitidos en los GI)
    Esta es una libreria dependiente sin acceso a la DB
    '''

    def __init__(self, **args):
        '''
        Arguments:
            complete_order_info {dict}: Informacion completa del pedido
            all_partials {list}: Lista de parciales del pedido
            id_current_partial {int}: identificador del parcial a liquidar
        '''
        loggin(
            'i', 
            'Iniciando librerria de prorrateo de costos par liquidacion del pacial {}'
            .format(args['id_current_partial'])
            )

        self.complete_order_info = args['complete_order_info']
        self.partials = args['all_partials']
        self.id_current_partial = args['current_ordinal_partial']
        self.apportionment_detail = []
        self.apportioment_header = {}
        self.indirect_costs = 0
        self.tc_trimestral = 1
    

    def get_data(self):
        '''
            Retorna los valores de costos indirectos para un parcial 
        '''
        return {
            'fobs_partials' : self._get_fobs_partial(),
            'droped_expenses' : {},
            'init_expenses' : {},
            'partial_expenses': {},
            'taxes' : {},
            'tc_trimestral' : self.tc_trimestral,
            'indirect_costs' : self.indirect_costs,
            'apportionment_header' : self.apportioment_header,
        }
    

    def _get_fobs_partial(self):
        return 0
    

    def _get_warenhouses(self):
        return 0
    

    def _get_init_expenses_apportionment(self):
        return 0


    def _get_partial_expenses(self):
        return 0
    

    def _get_droped_expenses(self):
        return 0