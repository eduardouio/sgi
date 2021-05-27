CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`v_ice_parciales` AS
    SELECT 
        REPLACE(`p`.`nro_pedido`, '-', '/') AS `nro_pedido`,
        `pr`.`nombre` AS `nombre`,
        `pr`.`cod_ice` AS `cod_ice`,
        `p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,
        `o`.`pais_origen` AS `pais_origen`,
        `fid`.`nro_cajas` AS `nro_cajas`,
        `fid`.`unidades` AS `unidades`,
        `fid`.`fob_tasa_trimestral` AS `fob_tasa_trimestral`,
        '' AS `Name_exp_9`,
        `pr`.`capacidad_ml` AS `capacidad_ml`,
        `fid`.`grado_alcoholico` AS `grado_alcoholico`,
        `fid`.`ex_aduana_unitario` AS `ex_aduana_unitario`,
        `fid`.`ice_especifico_unitario` AS `ice_especifico_unitario`,
        `fid`.`ice_advalorem_unitario` AS `ice_advalorem_unitario`,
        `fid`.`ice_unitario` AS `ice_unitario`,
        `fid`.`total_ice` AS `total_ice`,
        `fid`.`costo_total` AS `costo_total`,
        `fid`.`costo_caja_final` AS `costo_caja_final`,
        SUBSTR(`fi`.`nro_refrendo`, 1, 3) AS `digitos`,
        SUBSTR(`fi`.`nro_refrendo`, 5, 4) AS `anio`,
        SUBSTR(`fi`.`nro_refrendo`, 10, 2) AS `reg`,
        SUBSTR(`fi`.`nro_refrendo`, 13, 8) AS `cons`
    FROM
        (((((`cordovezApp`.`parcial` `p`
        LEFT JOIN `cordovezApp`.`pedido` `o` ON ((`o`.`nro_pedido` = `p`.`nro_pedido`)))
        LEFT JOIN `cordovezApp`.`factura_informativa` `fi` ON ((`fi`.`id_parcial` = `p`.`id_parcial`)))
        LEFT JOIN `cordovezApp`.`factura_informativa_detalle` `fid` ON ((`fid`.`id_factura_informativa` = `fi`.`id_factura_informativa`)))
        LEFT JOIN `cordovezApp`.`detalle_pedido_factura` `dpf` ON ((`fid`.`detalle_pedido_factura` = `dpf`.`detalle_pedido_factura`)))
        LEFT JOIN `cordovezApp`.`producto` `pr` ON ((`pr`.`cod_contable` = `dpf`.`cod_contable`)))
    ORDER BY `p`.`fecha_llegada_cliente` , `p`.`nro_pedido`