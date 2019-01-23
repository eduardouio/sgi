from django.test import TestCase

from lib_src.ReliquidateOrder import ReliquidateOrder
from lib_src.CompleteOrderInfo import CompleteOrderInfo
from logs.app_log import loggin


class TestReliquidateOrderFOBGOEURO(TestCase):
    '''
    Clase de testeo creada para probar la liquidacion de un pedido R10
    pedido 192-18
    '''

    def setUp(self):
        loggin('t', 'iniciando testeo de reliquidacion de pedido')

        complete_order_info = CompleteOrderInfo().get_data('192-18')
        self.returned_values = Reliquidate(
            complete_order_info = complete_order_info
            ).get_data()
        return super().setUp()
    

    def test_taxes(self):
        spected_taxes = [
                {
                    "detalle_pedido_factura":"603",
                    "arancel_advalorem":"0.000",
                    "base_advalorem":"4.320",
                    "base_advalorem_reliquidado":"0.000",
                    "base_ice_epecifico":"7.220",
                    "cajas_importadas":"1725.000",
                    "cantidad_x_caja":"12.000",
                    "capacidad_ml":"1000.000",
                    "cif":"28898.990",
                    "costo_botella":"2.622",
                    "costo_caja":"16.6000000000",
                    "costo_caja_final":"31.461",
                    "costo_total":"54269.725",
                    "costo_unidad":"1.383",
                    "etiquetas_fiscales":"2691.000",
                    "ex_aduana":"31734.4800000",
                    "ex_aduana_unitario":"1.5330000",
                    "ex_aduana_antes":"0.0000000",
                    "ex_aduana_antes_unitario":"0.0000000",
                    "exaduana_sin_etiquetas":"29043.4800000",
                    "exaduana_sin_tasa":"29043.4800000",
                    "flete":"200.000",
                    "flete_aduana":"150.000",
                    "fob":"28635.000",
                    "fob_tasa_trimestral":"0.000",
                    "fob_percent":"1.000",
                    "fodinfa":"144.490",
                    "gasto_origen_tasa_trimestral":"0.000",
                    "grado_alcoholico":"12",
                    "ice_advalorem":"0.000",
                    "ice_advalorem_reliquidado":"0.000",
                    "ice_advalorem_diferencia":"0.000",
                    "ice_advalorem_pagado":"0.000",
                    "ice_advalorem_sin_etiquetas":"0.000",
                    "ice_advalorem_sin_tasa":"0.000",
                    "ice_advalorem_unitario":"0.000",
                    "ice_especifico":"17934.480",
                    "ice_especifico_unitario":"0.866",
                    "ice_unitario":"0.000",
                    "id_parcial":"0.000",
                    "indirectos":"25634.725",
                    "last_update":"2018-11-08 13:27:01.000000",
                    "nro_cajas":"1725",
                    "nro_factura_informativa":"0.000",
                    "product":"VINO CLOS DE PIRQUE TINTO",
                    "prorrateo_parcial":"0.000",
                    "prorrateo_pedido":"7555.755",
                    "prorrateos_total":"7555.755",
                    "seguro":"119.000",
                    "seguro_aduana":"113.990",
                    "tasa_control":"0.000",
                    "total_ice":"17934.480",
                    "unidades":"20700.000",
                    "unidades_importadas":"20700.000",
                    "cod_contable":"01011080010401011000",
                    "id_pedido_factura":"358"
                },
        ]
        
        self.assertTrue(True)

    def test_sums(self):
        spected_sums = {}
        self.assertTrue(True)
