CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`v_producto_pedidos_R10_llegados` AS
    SELECT 
        `pf`.`nro_pedido` AS `nro_pedido`,
        `s`.`nombre` AS `nombre`,
        `pf`.`id_factura_proveedor` AS `id_factura_proveedor`,
        `o`.`nro_refrendo` AS `nro_refrendo`,
        `p`.`nombre` AS `producto`,
        `dpf`.`capacidad_ml` AS `capacidad_ml`,
        `dpf`.`grado_alcoholico` AS `grado_alcoholico`,
        `dpf`.`nro_cajas` AS `nro_cajas`,
        `dpf`.`unidades` AS `unidades`,
        `o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`
    FROM
        ((((`cordovezApp`.`detalle_pedido_factura` `dpf`
        LEFT JOIN `cordovezApp`.`pedido_factura` `pf` ON ((`pf`.`id_pedido_factura` = `dpf`.`id_pedido_factura`)))
        LEFT JOIN `cordovezApp`.`proveedor` `s` ON ((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`)))
        LEFT JOIN `cordovezApp`.`pedido` `o` ON ((`o`.`nro_pedido` = `pf`.`nro_pedido`)))
        LEFT JOIN `cordovezApp`.`producto` `p` ON ((`p`.`cod_contable` = `dpf`.`cod_contable`)))
    WHERE
        `dpf`.`id_pedido_factura` IN (SELECT 
                `cordovezApp`.`pedido_factura`.`id_pedido_factura`
            FROM
                `cordovezApp`.`pedido_factura`
            WHERE
                `cordovezApp`.`pedido_factura`.`nro_pedido` IN (SELECT 
                        `cordovezApp`.`pedido`.`nro_pedido`
                    FROM
                        `cordovezApp`.`pedido`
                    WHERE
                        (`cordovezApp`.`pedido`.`regimen` = 10)))