from orders.models.Order import Order
from orders.models.OrderInvoice import OrderInvoice
from orders.models.OrderInvoiceDetail import OrderInvoiceDetail
from lib_src.moocks.pedido import  pedidos
from lib_src.moocks.pedido_factura import  pedido_facturas
from django.db import connection

def populate_all(module=all):
	if module == 'orders':
		return _populate_orders()
    
def _populate_orders():
    for o in pedidos:
        Order.objects.create(
        nro_pedido = o['nro_pedido'],
        regimen = o['regimen'],
        flete_aduana = o['flete_aduana'],
        seguro_aduana = o['seguro_aduana'],
        incoterm = o['incoterm'],
        pais_origen = o['pais_origen'],
        ciudad_origen = o['ciudad_origen'],
        fecha_arribo = o['fecha_arribo'],
        dias_libres = o['dias_libres'],
        fecha_salida_bodega_puerto = o['fecha_salida_bodega_puerto'],
        fecha_ingreso_almacenera = o['fecha_ingreso_almacenera'],
        fecha_salida_almacenera = o['fecha_salida_almacenera'],
        comentarios = o['comentarios'],
        observaciones = o['observaciones'],
        nro_refrendo = o['nro_refrendo'],
        tipo_cambio_impuestosr10 = o['tipo_cambio_impuestosr10'],
        tipo_cambio_almacenerar70 = o['tipo_cambio_impuestosr70'],
        otros = o['otros'],
        id_user = o['id_user'],
        date_create = o['date_create'],
        last_update = o['last_update'],
        bg_isclosed = o['bg_isclosed'],
        bg_haveexpenses = o['bg_haveexpenses'],
        have_etiquetas_fiscales = o['have_etiquetas_fiscales'],
        exoneracion_arancel = o['exoneracion_arancel'],
        bg_have_tasa_control = o['bg_have_tasa_control'],
        bg_isliquidated = o['bg_isliquidated'],
        fodinfa = o['fodinfa'],
        fodinfa_pagado = o['fodinfa_pagado'],
        ice_advalorem = o['ice_advalorem'],
        ice_advalorem_pagado = o['ice_advalorem_pagado'],
        ice_especifico = o['ice_especifico'],
        ice_especifico_pagado = o['ice_especifico_pagado'],
        iva = o['iva'],
        iva_pagado = o['iva_pagado'],
        arancel_especifico_pagar = o['arancel_especifico_pagar'],
        arancel_especifico_pagar_pagado = o['arancel_especifico_pagar_pagado'],
        fecha_liquidacion = o['fecha_liquidacion'],
        nro_liquidacion = o['nro_liquidacion'],
        arancel_advalorem_pagar = o['arancel_advalorem_pagar'],
        arancel_advalorem_pagar_pagado = o['arancel_advalorem_pagar_pagado'],
        liquidacion_con_tasa = o['liquidacion_con_tasa'],
        base_arancel_advalorem = o['base_arancel_advalorem'],
        base_arancel_especifico = o['base_arancel_especifico'],
        base_ice_especifico = o['base_ice_especifico'],
        base_ice_advalorem = o['base_ice_advalorem'],
        porcentaje_ice_advalorem = o['porcentaje_ice_advalorem'],
        base_iva = o['base_iva'],
        base_fodinfa = o['base_fodinfa'],
        base_etiquetas = o['base_etiquetas'],
        fecha_cierre = o['fecha_cierre'],
        id_user_cierre = o['id_user_cierre'],
        tipo_cambio_go = o['tipo_cambio_go'],
        gasto_origen = o['gasto_origen'],
        fecha_llegada_cliente = o['fecha_llegada_cliente'],
        notas_cierre = o['notas_cierre'],
        fecha_salida_autorizada_puerto = o['fecha_salida_autorizada_puerto'],
        bg_have_close_parcial = o['bg_have_close_parcial'],
        docentry = o['docentry'],
        proveedor = o['proveedor'],
        url_dai_1 = o['url_dai_1'],
        url_dai_2 = o['url_dai_2'],
        url_dai_3 = o['url_dai_3'],
        path_dai_1 = o['path_dai_1'],
        path_dai_2 = o['path_dai_2'],
        path_dai_3 = o['path_dai_3']
        )
        
def create_schema(delete=False):
    if delete:
        with connection.schema_editor() as schema_editor:
            schema_editor.delete_model(Order)
        return True
                                        
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(Order)
    
    return True