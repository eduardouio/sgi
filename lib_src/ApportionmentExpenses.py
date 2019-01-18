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

    def __init__(self, **kwargs):
        '''
        Arguments:
            complete_order_info {dict}: Informacion completa del pedido
            all_partials {list}: Lista de parciales del pedido
            id_current_partial {int}: identificador del parcial a liquidar
        '''
        loggin(
            'i', 
            'Iniciando librerria de prorrateo de costos par liquidacion del pacial {}'
            .format(kwargs['ordinal_current_partial'])
            )

        self.complete_order_info = kwargs['complete_order_info']
        self.all_partials = kwargs['all_partials']
        self.ordinal_current_partial = kwargs['ordinal_current_partial']
        self.apportionment_detail = []
        self.apportioment_header = {}
        self.indirect_costs = 0
        self.tc_trimestral = 1
        self.current_partial_data = self.all_partials[self.ordinal_current_partial -1 ]
    

    def get_data(self):
        '''
            Retorna los valores de costos indirectos para un parcial 
        '''
        return {
            'fobs' : self.get_fobs(),
            'droped_expenses' : {},
            'init_expenses' : {},
            'partial_expenses': {},
            'taxes' : {},
            'tc_trimestral' : self.tc_trimestral,
            'indirect_costs' : self.indirect_costs,
            'apportionment_header' : self.apportioment_header,
        }
    

    def get_fobs(self):
        fobs = {
            'fob_inicial': 0,
            'fob_parcial': 0,
            'fob_parcial_razon_inicial': 0,
            'fob_parcial_razon_saldo': 0,
            'fob_saldo': 0,
            'fob_proximo_parcial': 0,
        }
        
        fobs['fob_inicial'] = float(self.complete_order_info['order_invoice']['totals']['value'])
        fobs['fob_parcial'] = float(self.current_partial_data['info_invoice']['totals']['value'])
        fobs['fob_parcial_razon_inicial'] = round(
                                                    float(fobs['fob_parcial']) 
                                                    / float(fobs['fob_inicial'])
                                                ,6)
        fobs['fob_saldo'] = fobs['fob_inicial'] - fobs['fob_parcial']
        fobs['fob_parcial_razon_saldo'] = round((fobs['fob_parcial'] / fobs['fob_inicial']),6)
        
        
        if self.ordinal_current_partial > 1:
           pass

        fobs['fob_proximo_parcial'] =  8605.800000
        return fobs


    def _get_warenhouses(self):
        return 0
    

    def _get_init_expenses_apportionment(self):
        return 0


    def _get_partial_expenses(self):
        return 0
    

    def _get_droped_expenses(self):
        return 0