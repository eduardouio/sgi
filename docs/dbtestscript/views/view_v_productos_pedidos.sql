CREATE VIEW `v_productos_pedidos` AS
    SELECT 
        `pf`.`nro_pedido` AS `nro_pedido`,
        `s`.`nombre` AS `nombre`,
        `pf`.`id_factura_proveedor` AS `id_factura_proveedor`,
        `o`.`nro_refrendo` AS `nro_refrendo`,
        `pr`.`nombre` AS `producto`,
        `dpf`.`capacidad_ml` AS `capacidad_ml`,
        `dpf`.`grado_alcoholico` AS `grado_alcoholico`,
        `dpf`.`nro_cajas` AS `nro_cajas`,
        `dpf`.`unidades` AS `unidades`,
        `o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`
    FROM
        ((((`detalle_pedido_factura` `dpf`
        LEFT JOIN `producto` `pr` ON ((`pr`.`cod_contable` = `dpf`.`cod_contable`)))
        LEFT JOIN `pedido_factura` `pf` ON ((`pf`.`id_factura_proveedor` = `dpf`.`id_pedido_factura`)))
        LEFT JOIN `proveedor` `s` ON ((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`)))
        LEFT JOIN `pedido` `o` ON ((`pf`.`nro_pedido` = `o`.`nro_pedido`)))