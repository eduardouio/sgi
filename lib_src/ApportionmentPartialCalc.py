from partials.models.Apportionment import Apportionment
from partials.models.ApportionmentDetail import ApportionmentDetail
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from paids.models.Expense import Expense
from logs.app_log import loggin

class ApportionmentPartialCalc(object):
    '''
    Return apportioment calculate from partial
    '''    
    def __init__(self):
        loggin('i', 'ApportionmentPartialCalc has init')
        self.id_partial = None
        
    
    def get_data(self, id_partial):
        '''
        Calc costo of initial expenses an warenhouse
        Args:
            id_partial (int): identificado de parcial a prorratear

        Return:
            dict : Diccionario relacionado con la informacion del prorrateo 
        '''
        self.id_partial = id_partial

        return {
            'fob_parcial' : self.get_fob_partial(),
            'prorrateos_inciales' : None,
            'warenhouses' : None,
        }
    

    def get_fob_partial():
        fobs_partial =  {
            'fob_inicial' : 0.0,
            'fob_saldo' : 0.0,
            'fob_parcial' : 0.0,
            'fob_parcial_razon_inicial' : 0.0,
            'fob_parcial_razon_saldo' : 0.0,
            'fob_proximo_parcial' : 0.0,
            'prorrateo_seguro_aduana' : 0.0,
            'prorrateo_flete_aduana' : 0.0,
            }     
        
        return fobs_partial

        

