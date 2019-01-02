#-*-coding=utf8-*-
import json

R70 = [
{"cod_contable":"01011010320805010750","nombre":"VINO BLANCO PAMPAS EXPRESION ARGENTINA CHARDONNAY","regimen":"70","nro_pedido":"007-18","id_factura_informativa":"12","cod_ice":"3031-53-015831-013-000750-66-101-000027","capacidad_ml":"750","ex_aduana_unitario":"2.260"},
{"cod_contable":"01022110330101020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6","regimen":"70","nro_pedido":"006-18","id_factura_informativa":"8","cod_ice":"3031-56-002075-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.939"},
{"cod_contable":"01022110330101020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6","regimen":"70","nro_pedido":"005-18","id_factura_informativa":"17","cod_ice":"3031-56-002075-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.953"},
{"cod_contable":"01022110330101020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6","regimen":"70","nro_pedido":"005-18","id_factura_informativa":"9","cod_ice":"3031-56-002075-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.045"},
{"cod_contable":"01022110330101020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6","regimen":"70","nro_pedido":"006-18","id_factura_informativa":"18","cod_ice":"3031-56-002075-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.946"},
{"cod_contable":"01022110330101020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"2","cod_ice":"3031-56-002075-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.052"},
{"cod_contable":"01022110330101020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"1","cod_ice":"3031-56-002075-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.051"},
{"cod_contable":"01022110330103020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT ROSE CAJA 6","regimen":"70","nro_pedido":"005-18","id_factura_informativa":"14","cod_ice":"3031-56-002076-013-000750-66-211-000026","capacidad_ml":"750","ex_aduana_unitario":"3.009"},
{"cod_contable":"01022110330103020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT ROSE CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"6","cod_ice":"3031-56-002076-013-000750-66-211-000026","capacidad_ml":"750","ex_aduana_unitario":"3.156"},
{"cod_contable":"01022110330103020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT ROSE CAJA 6","regimen":"70","nro_pedido":"006-18","id_factura_informativa":"8","cod_ice":"3031-56-002076-013-000750-66-211-000026","capacidad_ml":"750","ex_aduana_unitario":"3.003"},
{"cod_contable":"01022110330103020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT ROSE CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"2","cod_ice":"3031-56-002076-013-000750-66-211-000026","capacidad_ml":"750","ex_aduana_unitario":"3.116"},
{"cod_contable":"01022110330103020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT ROSE CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"1","cod_ice":"3031-56-002076-013-000750-66-211-000026","capacidad_ml":"750","ex_aduana_unitario":"3.115"},
{"cod_contable":"01022110330103020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY BRUT ROSE CAJA 6","regimen":"70","nro_pedido":"005-18","id_factura_informativa":"17","cod_ice":"3031-56-002076-013-000750-66-211-000026","capacidad_ml":"750","ex_aduana_unitario":"3.013"},
{"cod_contable":"01022110330102020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY DEMI SEC CAJA 6","regimen":"70","nro_pedido":"005-18","id_factura_informativa":"17","cod_ice":"3031-56-002077-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.953"},
{"cod_contable":"01022110330102020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY DEMI SEC CAJA 6","regimen":"70","nro_pedido":"006-18","id_factura_informativa":"18","cod_ice":"3031-56-002077-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.946"},
{"cod_contable":"01022110330102020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY DEMI SEC CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"2","cod_ice":"3031-56-002077-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.053"},
{"cod_contable":"01022110330102020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY DEMI SEC CAJA 6","regimen":"70","nro_pedido":"001-18","id_factura_informativa":"1","cod_ice":"3031-56-002077-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.051"},
{"cod_contable":"01022110330102020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY DEMI SEC CAJA 6","regimen":"70","nro_pedido":"005-18","id_factura_informativa":"9","cod_ice":"3031-56-002077-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.045"},
{"cod_contable":"01022110330102020750","nombre":"VINO ESPUMANTE VEUVE DU VERNAY DEMI SEC CAJA 6","regimen":"70","nro_pedido":"006-18","id_factura_informativa":"8","cod_ice":"3031-56-002077-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.939"},
{"cod_contable":"01022110330109010750","nombre":"VINO ESPUMOSO ICE DEMISEC","regimen":"70","nro_pedido":"004-18","id_factura_informativa":"4","cod_ice":"3031-56-025188-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.043"},
{"cod_contable":"01022110330109010750","nombre":"VINO ESPUMOSO ICE DEMISEC","regimen":"70","nro_pedido":"004-18","id_factura_informativa":"15","cod_ice":"3031-56-025188-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"2.983"},
{"cod_contable":"01022110330109010750","nombre":"VINO ESPUMOSO ICE DEMISEC","regimen":"70","nro_pedido":"004-18","id_factura_informativa":"11","cod_ice":"3031-56-025188-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.078"},
{"cod_contable":"01022110330108010750","nombre":"VINO ESPUMOSO ICE ROSE","regimen":"70","nro_pedido":"004-18","id_factura_informativa":"4","cod_ice":"3031-56-025189-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.106"},
{"cod_contable":"01022110330108010750","nombre":"VINO ESPUMOSO ICE ROSE","regimen":"70","nro_pedido":"004-18","id_factura_informativa":"15","cod_ice":"3031-56-025189-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.045"},
{"cod_contable":"01022110330108010750","nombre":"VINO ESPUMOSO ICE ROSE","regimen":"70","nro_pedido":"004-18","id_factura_informativa":"11","cod_ice":"3031-56-025189-013-000750-66-211-000024","capacidad_ml":"750","ex_aduana_unitario":"3.142"},
{"cod_contable":"01011010320803010750","nombre":"VINO TINTO PAMPAS EXPRESION ARGENTINA CABERNET SAUVIGNON","regimen":"70","nro_pedido":"003-18","id_factura_informativa":"3","cod_ice":"3031-53-015830-013-000750-66-101-000027","capacidad_ml":"750","ex_aduana_unitario":"2.287"},
{"cod_contable":"01011010320803010750","nombre":"VINO TINTO PAMPAS EXPRESION ARGENTINA CABERNET SAUVIGNON","regimen":"70","nro_pedido":"003-18","id_factura_informativa":"13","cod_ice":"3031-53-015830-013-000750-66-101-000027","capacidad_ml":"750","ex_aduana_unitario":"2.287"},
{"cod_contable":"01011010320806010750","nombre":"VINO TINTO PAMPAS EXPRESION ARGENTINA MALBEC","regimen":"70","nro_pedido":"003-18","id_factura_informativa":"16","cod_ice":"3031-53-015829-013-000750-66-101-000027","capacidad_ml":"750","ex_aduana_unitario":"2.287"},
{"cod_contable":"01011010320806010750","nombre":"VINO TINTO PAMPAS EXPRESION ARGENTINA MALBEC","regimen":"70","nro_pedido":"003-18","id_factura_informativa":"13","cod_ice":"3031-53-015829-013-000750-66-101-000027","capacidad_ml":"750","ex_aduana_unitario":"2.287"},
{"cod_contable":"01011010320806010750","nombre":"VINO TINTO PAMPAS EXPRESION ARGENTINA MALBEC","regimen":"70","nro_pedido":"003-18","id_factura_informativa":"3","cod_ice":"3031-53-015829-013-000750-66-101-000027","capacidad_ml":"750","ex_aduana_unitario":"2.287"}
]
filterR70 = []

for item in R70:
    if filterR70.__len__() == 0:
        filterR70.append(item)
    
    have = False

    for i in filterR70:
        if item['cod_contable'] == i['cod_contable']:
            have = True
    
    if have is False:
        filterR70.append(item)
    
print(json.dumps(filterR70))
