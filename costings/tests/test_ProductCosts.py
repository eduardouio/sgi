from django.test import TestCase

from lib_src.ApportionmentExpenses import ApportionmentExpenses
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from lib_src.CompletePartialInfo import CompletePartialInfo
from lib_src.ProductsCosts import CostingsProduct
from logs.app_log import loggin


class TestProductCosts(TestCase):

    def setUp(self):
        loggin('t', '-------------------------------------')
        loggin('t', '----------TestProductCosts-----------')
        loggin('t', '-------------------------------------')
        self.order_info = CompleteOrderInfo().get_data('071-18')
        self.all_partials = []

        for p in self.order_info['partials']:
            self.all_partials.append(CompletePartialInfo().get_data(
                id_partial=p.id_parcial,
                type_change_trimestral= self.order_info['tipo_cambio_trimestral']
            ))

        self.apportionment_partial = ApportionmentExpenses(
            complete_order_info = self.order_info,
            all_partials = self.all_partials,
            ordinal_current_partial = 0
        ).get_apportionments()

        self.current_patial = self.all_partials[0] 

        self.costs_expected = [{
            "id_factura_informativa_detalle": "235",
            "detalle_pedido_factura" : "141",
            "arancel_advalorem_pagar": "0.000",
            "arancel_especifico_pagar": "0.000",
            "base_advalorem": "3.240",
            "base_advalorem_reliquidado": "0.000",
            "base_ice_epecifico": "7.220",
            "capacidad_ml": "750.000",
            "cif": "8103.270",
            "cod_contable": "0102209312",
            "costo_botella": "4.215",
            "costo_caja": "13.500000",
            "costo_caja_final": "25.293",
            "costo_total": "12646.491",
            "costo_unidad": "2.250",
            "etiquetas_fiscales": "390.000",
            "ex_aduana": "8533.7900000",
            "ex_aduana_unitario": "2.8450000",
            "ex_aduana_antes": "0.0000000",
            "ex_aduana_antes_unitario": "0.0000000",
            "flete": "236.229",
            "flete_aduana": "236.176",
            "fob": "7832.700",
            "fob_tasa_trimestral": "0.000",
            "fob_percent": "0.500",
            "fecha_liquidacion": "2018-00-00",
            "fodinfa": "40.520",
            "gasto_origen": "0.000",
            "gasto_origen_tasa_trimestral": "0.000",
            "grado_alcoholico": "11.50000",
            "ice_advalorem": "0.000",
            "ice_advalorem_reliquidado": "0.000",
            "ice_especifico": "1868.180",
            "ice_unitario": "0.000",
            "indirectos": "4208.991",
            "nro_cajas": "500.000",
            "prorrateo_parcial": "446.491",
            "prorrateo_pedido": "1853.800",
            "prorrateos_total": "2300.291",
            "seguro": "36.083",
            "seguro_aduana": "34.394",
            "tasa_control": "0.000",
            "total_ice": "1868.180",
            "unidades": "3000.000",
            "unidades_importadas": "3000.000"
            },

            {
            "id_factura_informativa_detalle": "236",
            "detalle_pedido_factura" : "142",
            "arancel_advalorem_pagar": "0.000",
            "arancel_especifico_pagar": "0.000",
            "base_advalorem": "3.240",
            "base_advalorem_reliquidado": "0.000",
            "base_ice_epecifico": "7.220",
            "capacidad_ml": "750.000",
            "cif": "8103.270",
            "cod_contable": "0102209312",
            "costo_botella": "4.215",
            "costo_caja": "13.500000",
            "costo_caja_final": "25.293",
            "costo_total": "12646.491",
            "costo_unidad": "2.250",
            "etiquetas_fiscales": "390.000",
            "ex_aduana": "8533.7900000",
            "ex_aduana_unitario": "2.8450000",
            "ex_aduana_antes": "0.0000000",
            "ex_aduana_antes_unitario": "0.0000000",
            "flete": "236.229",
            "flete_aduana": "236.176",
            "fob": "7832.700",
            "fob_tasa_trimestral": "0.000",
            "fob_percent": "0.500",
            "fecha_liquidacion": "2018-00-00",
            "fodinfa": "40.520",
            "gasto_origen": "0.000",
            "gasto_origen_tasa_trimestral": "0.000",
            "grado_alcoholico": "11.50000",
            "ice_advalorem": "0.000",
            "ice_advalorem_reliquidado": "0.000",
            "ice_advalorem_unitario": "0.000",
            "ice_especifico": "1868.180",
            "ice_especifico_unitario": "0.623",
            "ice_unitario": "0.000",
            "indirectos": "4208.991",
            "nro_cajas": "500.000",
            "prorrateo_parcial": "446.491",
            "prorrateo_pedido": "1853.800",
            "prorrateos_total": "2300.291",
            "seguro": "36.083",
            "seguro_aduana": "34.394",
            "tasa_control": "0.000",
            "total_ice": "1868.180",
            "unidades": "3000.000",
        }]
        return super().setUp()
        
        
    def test_class(self):
        loggin('t', 'Testeo inicial de la clase de Costeo de Producto')
        contings = CostingsProduct(
            order_info =  self.order_info,
            is_order =  False,
            all_partials =  self.all_partials,
            apportionments =  self.apportionment_partial,
            ordinal_current_partial =  1

        ).get()

        self.assertEqual(1,1)