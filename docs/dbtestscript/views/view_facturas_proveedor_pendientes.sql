CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`facturas_proveedor_pendientes` AS
    SELECT 
        `pf`.`nro_pedido` AS `nro_pedido`,
        `pr`.`nombre` AS `nombre`,
        `pf`.`id_factura_proveedor` AS `id_factura_proveedor`,
        `pf`.`valor` AS `valor`
    FROM
        (`cordovezApp`.`pedido_factura` `pf`
        JOIN `cordovezApp`.`proveedor` `pr` ON ((`pf`.`identificacion_proveedor` = `pr`.`identificacion_proveedor`)))
    WHERE
        (`pf`.`id_factura_proveedor` LIKE 'SF%')