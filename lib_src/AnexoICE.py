from lib_src import ReportICE
from decimal import Decimal


class AnexoICE(object):
    ''' Reporte mensual del ICE detallado en unidades'''

    def __init__(self, year, month):
        ''' Anejo para ICE
        year (int) 
        mont (int)
        '''
        self.year = year
        self.month = month

    def get(self):
        ice_report = ReportICE(self.year, self.month)
        data = ice_report.get()
        report = []
        for item in data['parciales']:
            base_inponible = 0
            ice_advalorem_calculado = 0
            if item.ex_aduana_unitario > item.base_advalorem:
                base_inponible = (
                    item.ex_aduana_unitario - item.base_advalorem
                ) * item.unidades
                ice_advalorem_calculado = (
                    item.ex_aduana_unitario - item.base_advalorem
                    ) * Decimal(0.75)
            report.append({
                'product': item.detalle_pedido_factura.cod_contable.nombre,
                'nro_pedido': item.id_factura_informativa.id_parcial.nro_pedido,
                'cajas': item.nro_cajas,
                'unidades': item.unidades,
                'fob': item.fob_tasa_trimestral,
                'capacidad': item.capacidad_ml,
                'grado_alcoholico': item.grado_alcoholico,
                'exaduana': item.ex_aduana_unitario,
                'base_advalorem': item.base_advalorem,
                'ice_especifico_unitario': item.base_ice_epecifico,
                'ice_especifico': item.ice_especifico,
                'ice_advalorem_unitario': ice_advalorem_calculado,
                'ice_advalorem_calculado': (item.ice_advalorem_pagado / item.unidades),
                'ice_advalorem_pagado': item.ice_advalorem_pagado,
                'total_ice': item.total_ice,
                'volumen_bruto_ice': (item.capacidad_ml / 1000 
                    * item.grado_alcoholico/100) * item.unidades,
                'base_imponible': base_inponible,
            })
        for item in data['consumo']:
            base_inponible = 0
            ice_advalorem_calculado = 0
            if item.ex_aduana_unitario > item.base_advalorem:
                base_inponible = (
                    item.ex_aduana_unitario - item.base_advalorem
                ) * item.unidades
                ice_advalorem_calculado = (
                    item.ex_aduana_unitario - item.base_advalorem
                    ) * Decimal(0.75)
            report.append({
                'product': item.cod_contable.nombre,
                'nro_pedido': item.id_pedido_factura.nro_pedido,
                'cajas': item.nro_cajas,
                'unidades': item.unidades,
                'fob': item.fob_tasa_trimestral,
                'capacidad': item.capacidad_ml,
                'grado_alcoholico': item.grado_alcoholico,
                'exaduana': item.ex_aduana_unitario,
                'base_advalorem': item.base_advalorem,
                'ice_especifico_unitario': item.base_ice_epecifico,
                'ice_especifico': item.ice_especifico,
                'ice_advalorem_unitario': ice_advalorem_calculado,
                'ice_advalorem_calculado': (item.ice_advalorem_pagado / item.unidades),
                'ice_advalorem_pagado': item.ice_advalorem_pagado,
                'total_ice': item.total_ice,
                'volumen_bruto_ice': Decimal(item.capacidad_ml / 1000) 
                    * Decimal(item.grado_alcoholico / 100)  * item.unidades,
                'base_imponible': base_inponible,
            })
        return report
