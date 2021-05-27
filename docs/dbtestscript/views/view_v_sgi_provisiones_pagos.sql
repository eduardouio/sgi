CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`v_sgi_provisiones_pagos` AS
    SELECT 
        `gn`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,
        `gn`.`id_parcial` AS `id_parcial`,
        `gn`.`concepto` AS `concepto`,
        `gn`.`tipo` AS `tipo`,
        `gn`.`valor_provisionado` AS `valor_provisionado`,
        `gn`.`valor_ajuste` AS `valor_ajuste`,
        `gn`.`fecha` AS `fecha`,
        `gn`.`fecha_fin` AS `fecha_fin`,
        `gn`.`comentarios` AS `comentarios`,
        `gn`.`bg_closed` AS `bg_closed`,
        `gn`.`bg_is_visible_gi` AS `bg_is_visible_gi`,
        `gn`.`bg_iscontabilizado` AS `bg_iscontabilizado`,
        `gn`.`bg_iscontabilizado_por` AS `bg_iscontabilizado_por`,
        `gn`.`bg_isdrop` AS `bg_isdrop`,
        `gn`.`id_user` AS `id_user`,
        `gn`.`date_create` AS `date_create`,
        `gn`.`last_update` AS `last_update`,
        `gn`.`identificacion_proveedor` AS `identificacion_proveedor`,
        `gn`.`nro_pedido` AS `nro_pedido`,
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
        LEFT JOIN `cordovezApp`.`pedido` `o` ON ((IFNULL(`p`.`nro_pedido`, `gn`.`nro_pedido`) = `o`.`nro_pedido`)))
    ORDER BY `gn`.`tipo` , `gn`.`fecha` , `gn`.`concepto`