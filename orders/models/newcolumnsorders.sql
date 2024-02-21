alter table pedido
add column bg_is_tracked TINYINT(1) DEFAULT 1,
add column bg_is_closed_checked TINYINT(1) DEFAULT 0,
add column nro_hbl_awb VARCHAR(70) DEFAULT NULL,
add column puerto_destino VARCHAR(70) DEFAULT NULL,
add column fecha_emision_bl DATE DEFAULT NULL,
add column fecha_embarque DATE DEFAULT NULL,
add column agente_embarque_forwarder VARCHAR(70) DEFAULT NULL,
add column tipo_carga VARCHAR(45) DEFAULT NULL,
add column tipo_flete VARCHAR(70) DEFAULT NULL,
add column peso_carga INT(10) DEFAULT NULL,
add column volumen_carga_cbm INT(10) DEFAULT NULL,
add column nro_seguimiento_formarder VARCHAR(50) DEFAULT NULL;


alter table orders_historicalorder
add column bg_is_tracked TINYINT(1) DEFAULT 1,
add column bg_is_closed_checked TINYINT(1) DEFAULT 0,
add column nro_hbl_awb VARCHAR(70) DEFAULT NULL,
add column puerto_destino VARCHAR(70) DEFAULT NULL,
add column fecha_emision_bl DATE DEFAULT NULL,
add column fecha_embarque DATE DEFAULT NULL,
add column agente_embarque_forwarder VARCHAR(70) DEFAULT NULL,
add column tipo_carga VARCHAR(45) DEFAULT NULL,
add column tipo_flete VARCHAR(70) DEFAULT NULL,
add column peso_carga INT(10) DEFAULT NULL,
add column volumen_carga_cbm INT(10) DEFAULT NULL,
add column nro_seguimiento_formarder VARCHAR(50) DEFAULT NULL;