from django.test import TestCase
from paids.models import Expense


class ExpenseTEST(TestCase):

    def setUp(self):
        return super().setUp()

    def test_get_by_id_expense(self):
        spected_data = [
            {'id_gastos_nacionalizacion' : 16 , 'concepto' : 'FLETE', 'valor_provisionado': 1620.00},
            {'id_gastos_nacionalizacion' : 19 , 'concepto' : 'ALMACENAJE INICIAL', 'valor_provisionado': 257.98},
            {'id_gastos_nacionalizacion' : 26 , 'concepto' : 'TRANSPORTE INTERNO NORMALUIO-GYE', 'valor_provisionado': 660.00},
            {'id_gastos_nacionalizacion' : 34 , 'concepto' : 'ETIQUETAS FISCALES', 'valor_provisionado': 2691.00},
        ]

        for item in spected_data:
            data = Expense.get_by_id_expense(item['id_gastos_nacionalizacion'])
            self.assertEqual(data.id_gastos_nacionalizacion, 
                                            item['id_gastos_nacionalizacion'])
            self.assertEqual(data.concepto, item['concepto'])
            self.assertEqual(float(data.valor_provisionado), item['valor_provisionado'])

        # gasto no existente
        data = Expense.get_by_id_expense(0)
        self.assertIsNone(data)

    def test_get_all_by_order(self):
        # gastos del pedido 125-19
        spected_data = [
            {'id_gastos_nacionalizacion' : 10489,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'ISD','valor_provisionado' : 1676.80},
            {'id_gastos_nacionalizacion' : 10491,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'POLIZA SEGURO','valor_provisionado' : 147.90},
            {'id_gastos_nacionalizacion' : 11344,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'FLETE','valor_provisionado' : 187.00},
            {'id_gastos_nacionalizacion' : 11345,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'GASTOS LOCALES','valor_provisionado' : 485.00},
            {'id_gastos_nacionalizacion' : 11346,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'THC','valor_provisionado' : 192.00},
            {'id_gastos_nacionalizacion' : 11363,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'ALMACENAJE INICIAL','valor_provisionado' : 656.52},
            {'id_gastos_nacionalizacion' : 11536,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'HORAS EXTRAS','valor_provisionado' : 40.00},
            {'id_gastos_nacionalizacion' : 11560,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'AGENTE INICIAL FISICO','valor_provisionado' : 251.40},
            {'id_gastos_nacionalizacion' : 11561,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'CANDADO SATELITAL','valor_provisionado' : 70.00},
            {'id_gastos_nacionalizacion' : 11562,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'CUSTODIA ARMADA','valor_provisionado' : 400.00},
            {'id_gastos_nacionalizacion' : 11563,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'DESCARGA ALMAGRO','valor_provisionado' : 55.00},
            {'id_gastos_nacionalizacion' : 11564,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'DEVOLUCION DE CONTENEDOR','valor_provisionado' : 29.00},
            {'id_gastos_nacionalizacion' : 11565,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'TRANSPORTE INTERNO NORMALUIO-GYE','valor_provisionado' : 640.00},            
        ]
        
        data = Expense.get_all_by_order('125-19')
        self.assertEqual(data.count(), spected_data.__len__())
        for exp in data:
            for spected in spected_data:
                if exp.id_gastos_nacionalizacion == spected['id_gastos_nacionalizacion']:
                    self.assertEqual(spected['id_parcial'], exp.id_parcial)
                    self.assertEqual(spected['nro_pedido'], exp.nro_pedido_id)
                    self.assertEqual(spected['concepto'], exp.concepto)
                    self.assertEqual(spected['valor_provisionado'], float(exp.valor_provisionado))
                    break
        
        #pedido no existe
        data = Expense.get_all_by_order('dont-exist')
        self.assertEqual(data, [])

    def test_get_by_partial(self):
        spected_data = [
            {'id_gastos_nacionalizacion' : 11594,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'DEPOSITO 2019Jun-2019Jul', 'valor_provisionado':173.00},
            {'id_gastos_nacionalizacion' : 11595,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'ETIQUETAS FISCALES', 'valor_provisionado':639.60},
            {'id_gastos_nacionalizacion' : 11596,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'ETIQUETADO ESPACIO ALMAGRO', 'valor_provisionado':10.99},
            {'id_gastos_nacionalizacion' : 11597,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'AGENTE ADUANA', 'valor_provisionado':198.00},
            {'id_gastos_nacionalizacion' : 11651,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'TRANSPORTE', 'valor_provisionado':123.00},
            {'id_gastos_nacionalizacion' : 11653,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'MANO DE OBRA ETIQUETADO', 'valor_provisionado':147.60},
            {'id_gastos_nacionalizacion' : 11654,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'DESCARGA', 'valor_provisionado': 61.00},
        ]

        data = Expense.get_by_parcial(442)
        self.assertEqual(data.count(), spected_data.__len__())
        for exp in data:
            for spected in spected_data:
                if exp.id_gastos_nacionalizacion == spected['id_gastos_nacionalizacion']:
                    self.assertEqual(spected['id_parcial'], exp.id_parcial)
                    self.assertEqual(spected['nro_pedido'], exp.nro_pedido_id)
                    self.assertEqual(spected['concepto'], exp.concepto)
                    self.assertEqual(spected['valor_provisionado'], float(exp.valor_provisionado))
                    break
        
        # parcial no existe
        data = Expense.get_by_parcial(999999)
        self.assertEqual([],data)

    def test_get_complete_expenses(self):
        spected_data = [
            {'id_gastos_nacionalizacion' : 10489,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'ISD','valor_provisionado' : 1676.80},
            {'id_gastos_nacionalizacion' : 10491,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'POLIZA SEGURO','valor_provisionado' : 147.90},
            {'id_gastos_nacionalizacion' : 11344,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'FLETE','valor_provisionado' : 187.00},
            {'id_gastos_nacionalizacion' : 11345,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'GASTOS LOCALES','valor_provisionado' : 485.00},
            {'id_gastos_nacionalizacion' : 11346,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'THC','valor_provisionado' : 192.00},
            {'id_gastos_nacionalizacion' : 11363,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'ALMACENAJE INICIAL','valor_provisionado' : 656.52},
            {'id_gastos_nacionalizacion' : 11536,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'HORAS EXTRAS','valor_provisionado' : 40.00},
            {'id_gastos_nacionalizacion' : 11560,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'AGENTE INICIAL FISICO','valor_provisionado' : 251.40},
            {'id_gastos_nacionalizacion' : 11561,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'CANDADO SATELITAL','valor_provisionado' : 70.00},
            {'id_gastos_nacionalizacion' : 11562,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'CUSTODIA ARMADA','valor_provisionado' : 400.00},
            {'id_gastos_nacionalizacion' : 11563,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'DESCARGA ALMAGRO','valor_provisionado' : 55.00},
            {'id_gastos_nacionalizacion' : 11564,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'DEVOLUCION DE CONTENEDOR','valor_provisionado' : 29.00},
            {'id_gastos_nacionalizacion' : 11565,'id_parcial' : 0 ,'nro_pedido' : '125-19','concepto' : 'TRANSPORTE INTERNO NORMALUIO-GYE','valor_provisionado' : 640.00},
            {'id_gastos_nacionalizacion' : 11594,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'DEPOSITO 2019Jun-2019Jul', 'valor_provisionado':173.00},
            {'id_gastos_nacionalizacion' : 11595,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'ETIQUETAS FISCALES', 'valor_provisionado':639.60},
            {'id_gastos_nacionalizacion' : 11596,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'ETIQUETADO ESPACIO ALMAGRO', 'valor_provisionado':10.99},
            {'id_gastos_nacionalizacion' : 11597,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'AGENTE ADUANA', 'valor_provisionado':198.00},
            {'id_gastos_nacionalizacion' : 11651,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'TRANSPORTE', 'valor_provisionado':123.00},
            {'id_gastos_nacionalizacion' : 11653,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'MANO DE OBRA ETIQUETADO', 'valor_provisionado':147.60},
            {'id_gastos_nacionalizacion' : 11654,'id_parcial' : 442,'nro_pedido': '000-00', 'concepto': 'DESCARGA', 'valor_provisionado': 61.00},
            {'id_gastos_nacionalizacion' : 12254,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'DEPOSITO 2019Jul-2019Ago','valor_provisionado' : 165.00},
            {'id_gastos_nacionalizacion' : 13243,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'ETIQUETAS FISCALES','valor_provisionado' : 1113.84},
            {'id_gastos_nacionalizacion' : 13244,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'ETIQUETADO ESPACIO ALMAGRO','valor_provisionado' : 10.49},
            {'id_gastos_nacionalizacion' : 13245,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'AGENTE ADUANA','valor_provisionado' : 198.00},
            {'id_gastos_nacionalizacion' : 13869,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'DEPOSITO 2019Ago-2019Sep','valor_provisionado' : 165.00},
            {'id_gastos_nacionalizacion' : 14199,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'TRANSPORTE','valor_provisionado' : 200.00},
            {'id_gastos_nacionalizacion' : 14200,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'MANO DE OBRA ETIQUETADO','valor_provisionado' : 257.04},
            {'id_gastos_nacionalizacion' : 14201,'id_parcial' : 467,'nro_pedido' : '000-00','concepto' : 'DESCARGA','valor_provisionado' : 100.00},
        ]

        data = Expense.get_complete_expenses('125-19')
        self.assertEqual(data.__len__(), spected_data.__len__())
        for exp in data:
            for spected in spected_data:
                if exp.id_gastos_nacionalizacion == spected['id_gastos_nacionalizacion']:
                    self.assertEqual(spected['id_parcial'], exp.id_parcial)
                    self.assertEqual(spected['nro_pedido'], exp.nro_pedido_id)
                    self.assertEqual(spected['concepto'], exp.concepto)
                    self.assertEqual(spected['valor_provisionado'], float(exp.valor_provisionado))
                    break

        # pedido no existe
        data = Expense.get_all_by_order('dont-exist')
        self.assertEqual(data, [])
    
    def test_get_months_storage(self):
        self.assertEqual(0, Expense.get_months_storage('no-exist'))
        self.assertEqual(1, Expense.get_months_storage('190-20'))
        self.assertEqual(17, Expense.get_months_storage('147-19'))
        self.assertEqual(3, Expense.get_months_storage('125-19'))
        self.assertEqual(13, Expense.get_months_storage('310-19'))
        self.assertEqual(13, Expense.get_months_storage('352-19'))
        
        