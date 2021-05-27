CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`llegadas_pendientes_almagro` AS
    SELECT 
        `p`.`nro_pedido` AS `nro_pedido`,
        `s`.`nombre` AS `nombre`,
        `p`.`fecha_liquidacion` AS `fecha_liquidacion`,
        `fi`.`nro_factura_informativa` AS `nro_factura_informativa`,
        `fi`.`nro_refrendo` AS `nro_refrendo`,
        `p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`
    FROM
        (((`cordovezApp`.`parcial` `p`
        LEFT JOIN `cordovezApp`.`factura_informativa` `fi` ON ((`fi`.`id_parcial` = `p`.`id_parcial`)))
        LEFT JOIN `cordovezApp`.`pedido_factura` `pf` ON ((`p`.`nro_pedido` = `pf`.`nro_pedido`)))
        LEFT JOIN `cordovezApp`.`proveedor` `s` ON ((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`)))
    WHERE
        ((`p`.`bg_isliquidated` = 1)
            AND (`p`.`fecha_llegada_cliente` IS NULL))