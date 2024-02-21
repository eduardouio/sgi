CREATE VIEW `stockActiveProductsInCustomsView` AS
    SELECT 
        `pf`.`nro_pedido` AS `nro_pedido`,
        `ped`.`regimen` AS `regimen`,
        `dpf`.`id_pedido_factura` AS `id_pedido_factura`,
        `pf`.`id_factura_proveedor` AS `id_factura_proveedor`,
        `pf`.`identificacion_proveedor` AS `identificacion_proveedor`,
        `prov`.`nombre` AS `proveedor`,
        `dpf`.`detalle_pedido_factura` AS `detalle_pedido_factura`,
        `pro`.`nombre` AS `producto`,
        `dpf`.`costo_caja` AS `costo_caja`,
        `dpf`.`cod_contable` AS `cod_contable`,
        `dpf`.`grado_alcoholico` AS `grado_alcoholico`,
        `dpf`.`nro_cajas` AS `nro_cajas`,
        `pro`.`capacidad_ml` AS `capacidad_ml`,
        `pro`.`cantidad_x_caja` AS `cantidad_x_caja`
    FROM
        ((((`detalle_pedido_factura` `dpf`
        LEFT JOIN `producto` `pro` ON ((`dpf`.`cod_contable` = `pro`.`cod_contable`)))
        LEFT JOIN `pedido_factura` `pf` ON ((`dpf`.`id_pedido_factura` = `pf`.`id_pedido_factura`)))
        LEFT JOIN `pedido` `ped` ON ((`pf`.`nro_pedido` = `ped`.`nro_pedido`)))
        LEFT JOIN `proveedor` `prov` ON ((`pf`.`identificacion_proveedor` = `prov`.`identificacion_proveedor`)))
    WHERE
        (`dpf`.`nro_cajas` > 0)
    ORDER BY `pf`.`nro_pedido`