CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`provisiones_vs_pagos` AS
    SELECT 
        `gn`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,
        `gn`.`concepto` AS `concepto`,
        `gn`.`tipo` AS `tipo`,
        `gn`.`fecha` AS `fecha`,
        IFNULL(`p`.`nro_pedido`, `gn`.`nro_pedido`) AS `nro_pedido1`,
        `o`.`incoterm` AS `incoterm`,
        `o`.`nro_pedido` AS `nro_pedido`,
        `gn`.`id_parcial` AS `parcial`,
        `gn`.`valor_provisionado` AS `valor_provisionado`,
        (SELECT 
                IFNULL(SUM(`ddp`.`valor`), 0)
            FROM
                `cordovezApp`.`detalle_documento_pago` `ddp`
            WHERE
                (`ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`)) AS `pago`,
        (`gn`.`valor_provisionado` - (SELECT 
                IFNULL(SUM(`ddp`.`valor`), 0)
            FROM
                `cordovezApp`.`detalle_documento_pago` `ddp`
            WHERE
                (`ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`))) AS `saldo`
    FROM
        ((`cordovezApp`.`gastos_nacionalizacion` `gn`
        LEFT JOIN `cordovezApp`.`parcial` `p` ON (((`p`.`id_parcial` = `gn`.`id_parcial`)
            AND (`gn`.`id_parcial` <> 0))))
        LEFT JOIN `cordovezApp`.`pedido` `o` ON (((IFNULL(`p`.`nro_pedido`, `gn`.`nro_pedido`) = `o`.`nro_pedido`)
            AND (`gn`.`concepto` <> 'ISD')
            AND (`gn`.`concepto` <> 'TRANSPORTE')
            AND (`gn`.`concepto` <> 'MANO DE OBRA ETIQUETADO')
            AND (`gn`.`concepto` <> 'DESCARGA')
            AND (`gn`.`concepto` <> 'ISD')
            AND (`gn`.`fecha` > '2018-12-31'))))
    ORDER BY `gn`.`tipo` , `gn`.`fecha` , `gn`.`concepto`