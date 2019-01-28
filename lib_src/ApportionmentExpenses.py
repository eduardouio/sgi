from logs.app_log import loggin
from partials.models.Apportionment import Apportionment
from partials.models.ApportionmentDetail import ApportionmentDetail
from decimal import Decimal

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
            'Iniciando libreria de prorrateos parcial {}'
            .format(kwargs['ordinal_current_partial'])
            )

        self.complete_order_info = kwargs['complete_order_info']
        self.all_partials = kwargs['all_partials']
        self.ordinal_current_partial = int(kwargs['ordinal_current_partial'])
        self.apportionment_detail = []
        self.indirect_costs = 0
        self.fob_razon_inicial = 0,
        self.fob_razon_saldo = 0,
        self.current_partial_data = self.all_partials[self.ordinal_current_partial -1 ]
    

    def make_apportionment(self):
        '''
           Registra en la base los prorrateos 
        '''
        if self.current_partial_data['partial'].bg_isclosed == 1:
            loggin(
                'i', 
                'El parcial {} se encuentra cerrado se omite el prorrateo'
                .format(self.current_partial_data['partial'].id_parcial)
                )
            return False
            
        Apportionment.delete_from_parcial(self.current_partial_data['partial'].id_parcial)
        apportionment_headers = self.set_fobs()
        apportionment_headers.update(self.set_warenhouses())
        apportionment_headers.update(self.set_droped_expenses())
        apportionment_headers['prorrateo_flete_aduana'] = (
            self.complete_order_info['order'].seguro_aduana
            * apportionment_headers['fob_parcial']
        ),
        apportionment_headers['prorrateo_seguro_aduana'] = (
            self.complete_order_info['order'].flete_aduana
            * apportionment_headers['fob_parcial']
        )
        loggin('w', '-------------------------------')
        loggin('t', apportionment_headers)
        loggin('w', '-------------------------------')

        new_apportionment = Apportionment.objects.create_apportionment(apportionment_headers)
        new_apportionment.save()
        
        apportionmet_detail = self.set_apportionment_expenses()
        #for app_det in apportionmet_detail:
        #    new_app_det = ApportionmentDetail(app_det)
        #    new_app_det.id_prorrateo = new_apportionment.id_prorrateo
        
        #loggin('i', 'Nuevo prorrateo registrado id {}'.format(new_apportionment.id_prorrateo))
        return True


    def set_fobs(self):
        loggin('w', self.current_partial_data['partial'])
        fobs = {
            'id_parcial' : self.current_partial_data['partial'],
            'fob_inicial': 0,
            'fob_parcial': 0,
            'fob_parcial_razon_inicial': 0,
            'porcentaje_parcial' : 0,
            'fob_parcial_razon_saldo': 0,
            'fob_saldo': 0,
            'fob_proximo_parcial': 0,
        }

        fobs['fob_inicial'] = self.complete_order_info['order_invoice']['totals']['value']
        fobs['fob_parcial'] = self.current_partial_data['info_invoice']['totals']['value']
        
        if self.ordinal_current_partial > 1:
            fobs['saldo'] = self.complete_order_info['last_apportionment'].fob_proximo_parcial
        else:
            fobs['fob_saldo'] = fobs['fob_inicial']

        fobs['fob_parcial_razon_saldo'] = fobs['fob_parcial'] / fobs['fob_inicial']
        fobs['fob_parcial_razon_inicial'] = fobs['fob_parcial'] / fobs['fob_inicial']
        fobs['porcentaje_parcial'] = fobs['fob_parcial_razon_inicial']
        fobs['fob_proximo_parcial'] =  fobs['fob_saldo'] - fobs['fob_parcial']
        self.fob_razon_inicial = round(fobs['fob_parcial_razon_inicial'],10)
        self.fob_razon_saldo = round(fobs['fob_parcial_razon_saldo'],10)

        return fobs


    def set_warenhouses(self):
        warenhousing = {
            'almacenaje_parcial' : 0,
            'almacenaje_anterior' : 0,
            'almacenaje_aplicado' : 0,
            'almacenaje_proximo_parcial' : 0,
            }
        
        if self.current_partial_data['status']['partial_expenses'] is False:
            return warenhousing
        
        for w in self.current_partial_data['expenses']:
            if w.concepto.find('DEPOSITO 201') == 0:
                warenhousing['almacenaje_parcial'] += float(w.valor_provisionado)                
        
        if self.ordinal_current_partial > 1:
            warenhousing['almacenaje_anterior'] = self.complete_order_info['last_apportionment'].almacenaje_proximo_parcial
        
        warenhouseng_sale = Decimal((
            warenhousing['almacenaje_parcial']
            + warenhousing['almacenaje_anterior']
        ))

        warenhousing['almacenaje_aplicado'] = warenhouseng_sale * self.fob_razon_saldo
        warenhousing['almacenaje_proximo_parcial'] =  warenhouseng_sale - warenhousing['almacenaje_aplicado']

        return warenhousing
        

    def set_apportionment_expenses(self):                
        apportionment_expenses = []

        if self.complete_order_info['status']['init_expenses']:    
            for expense in self.complete_order_info['expenses']:
                apportionment_expenses.append({
                    'id_gastos_nacionalizacion': expense.id_gastos_nacionalizacion,
                    'tipo':'gasto_inicial',
                    'concepto': expense.concepto,
                    'valor_prorrateado': expense.valor_provisionado * self.fob_razon_inicial,
                    'valor_provisionado': expense.valor_provisionado,
                })
        
        if self.current_partial_data['status']['partial_expenses']:
            for expense in self.current_partial_data['expenses']:
                if (expense.concepto.find('DEPOSITO 201') == -1) and expense.bg_isdrop == 0:
                    apportionment_expenses.append({
                        'id_gastos_nacionalizacion': expense.id_gastos_nacionalizacion,
                        'tipo':'gasto_inicial',
                        'concepto': expense.concepto,
                        'valor_prorrateado': expense.valor_provisionado,
                        'valor_provisionado': expense.valor_provisionado,
                    })
                
        return apportionment_expenses
    

    def set_droped_expenses(self):
        droped_expenses = {
            'gastos_drop_parcial' : 0,
            'gastos_drop_parcial_anterior' : 0,
            'gastos_drop_parcial_aplicado' : 0,
            'gastos_drop_parcial_proximo_parcial' :0,
        }

        if self.ordinal_current_partial == 1:
            return droped_expenses
        
        bg_have_droped_expenses = False

        if self.current_partial_data['status']['partial_expenses']:
            for expense in self.current_partial_data['expenses']:
                if expense.bg_isdrop == 1:
                    bg_have_droped_expenses = True
                    droped_expenses['gastos_drop_parcial'] += float(expense.valor_provisionado)
                    droped_expenses['gastos_drop_parcial_anterior'] =  self.complete_order_info['last_apportionment'].gastos_drop_proximo_parcial
        
        if bg_have_droped_expenses:
            total_droped = (
                droped_expenses['gastos_drop_parcial']
                + droped_expenses['gastos_drop_parcial_anterior']
            )
            
            droped_expenses['gastos_drop_parcial_aplicado'] = (
                total_droped
                * self.fob_razon_saldo
            )

            droped_expenses['gastos_drop_parcial_proximo_parcial'] = (
                total_droped -  droped_expenses['gastos_drop_parcial_aplicado']
                )
        
        return droped_expenses