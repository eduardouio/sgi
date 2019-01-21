class Reliquidate(object):
    '''
        Realiza la reliquidacion de un pedido
    '''
    
    def __init__(self, *args, **kwargs):
        '''Retorna los valores de reliquidacion para un pedido
        
        Arguments:
        complete_order_info {dict} : informacion completa de un pedido
        '''
        self.complete_order_info = kwargs['complete_order_info']
        self.incoterm = None
        self.tasa_trim = 1
        self.origin_expenses = 0
        self.total_items = 0
    
    
    def get_data(self):
        return {
            'taxes' : [],
            'sums' : [],
            'data_general' : {}
        }
    

    def get_taxes(self):
        order_invoice = self.complete_order_info['order_invoice']
        



    def get_ice_advalorem(self):
        pass