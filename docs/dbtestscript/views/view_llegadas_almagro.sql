CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`llegadas_almagro` AS
    SELECT 
        REPLACE(`o`.`nro_pedido`, '-', '/') AS `nro_pedido`,
        `pr`.`nombre` AS `nombre`,
        `pr`.`cod_ice` AS `cod_ice`,
        `o`.`fecha_ingreso_almacenera` AS `fecha_ingreso_almacenera`,
        `o`.`pais_origen` AS `pais_origen`,
        `dpf`.`nro_cajas` AS `nro_cajas`,
        `dpf`.`unidades` AS `unidades`,
        ((`dpf`.`costo_caja` * `dpf`.`nro_cajas`) * `pf`.`tipo_cambio`) AS `fob`,
        '' AS `Name_exp_9`,
        `pr`.`capacidad_ml` AS `capacidad_ml`,
        `dpf`.`grado_alcoholico` AS `grado_alcoholico`,
        `dpf`.`ex_aduana_unitario` AS `ex_aduana_unitario`,
        `dpf`.`ice_especifico_unitario` AS `ice_especifico_unitario`,
        `dpf`.`ice_advalorem_unitario` AS `ice_advalorem_unitario`,
        `dpf`.`ice_unitario` AS `ice_unitario`,
        `dpf`.`total_ice` AS `total_ice`,
        `dpf`.`costo_total` AS `costo_total`,
        `dpf`.`costo_caja_final` AS `costo_caja_final`,
        SUBSTR(`o`.`nro_refrendo`, 1, 3) AS `digitos`,
        SUBSTR(`o`.`nro_refrendo`, 5, 4) AS `anio`,
        SUBSTR(`o`.`nro_refrendo`, 10, 2) AS `reg`,
        SUBSTR(`o`.`nro_refrendo`, 13, 8) AS `cons`
    FROM
        (((`cordovezApp`.`pedido` `o`
        LEFT JOIN `cordovezApp`.`pedido_factura` `pf` ON ((`pf`.`nro_pedido` = `o`.`nro_pedido`)))
        LEFT JOIN `cordovezApp`.`detalle_pedido_factura` `dpf` ON ((`pf`.`id_pedido_factura` = `dpf`.`id_pedido_factura`)))
        LEFT JOIN `cordovezApp`.`producto` `pr` ON ((`pr`.`cod_contable` = `dpf`.`cod_contable`)))
    WHERE
        (`o`.`fecha_ingreso_almacenera` > '2019-10-00')
    ORDER BY `o`.`fecha_ingreso_almacenera` , `o`.`nro_pedido`