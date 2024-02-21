CREATE VIEW `producto_en_transito` AS
    SELECT 
        CAST(SUBSTR(`p`.`nro_pedido`, 1, 3) AS UNSIGNED) AS `consecutivo`,
        CAST(SUBSTR(`p`.`nro_pedido`, 5, 2) AS UNSIGNED) AS `anio`,
        `p`.`nro_pedido` AS `nro_pedido`,
        `fi`.`nro_refrendo` AS `nro_refrendo`,
        `pro`.`nombre` AS `nombre`,
        `p`.`fecha_liquidacion` AS `fecha_liquidacion`,
        `p`.`bg_isliquidated` AS `bg_isliquidated`,
        `p`.`bg_isclosed` AS `bg_isclosed`,
        `p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,
        `fid`.`nro_cajas` AS `nro_cajas`,
        `pro`.`cantidad_x_caja` AS `cantidad_x_caja`,
        (`pro`.`cantidad_x_caja` * `fid`.`nro_cajas`) AS `Unidades`
    FROM
        ((((`factura_informativa_detalle` `fid`
        JOIN `factura_informativa` `fi` ON ((`fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`)))
        JOIN `parcial` `p` ON ((`fi`.`id_parcial` = `p`.`id_parcial`)))
        JOIN `detalle_pedido_factura` `dpf` ON ((`fid`.`detalle_pedido_factura` = `dpf`.`detalle_pedido_factura`)))
        JOIN `producto` `pro` ON ((`dpf`.`cod_contable` = `pro`.`cod_contable`)))
    WHERE
        ((`p`.`bg_isliquidated` = 1)
            AND (`p`.`fecha_llegada_cliente` IS NULL))