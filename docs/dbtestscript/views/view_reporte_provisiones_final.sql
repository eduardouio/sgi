CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`reporte_provisiones_final` AS
    SELECT 
        `cordovezApp`.`provisiones_vs_pagos`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,
        `cordovezApp`.`provisiones_vs_pagos`.`concepto` AS `concepto`,
        `cordovezApp`.`provisiones_vs_pagos`.`tipo` AS `tipo`,
        `cordovezApp`.`provisiones_vs_pagos`.`fecha` AS `fecha`,
        `cordovezApp`.`provisiones_vs_pagos`.`nro_pedido1` AS `nro_pedido1`,
        `cordovezApp`.`provisiones_vs_pagos`.`incoterm` AS `incoterm`,
        `cordovezApp`.`provisiones_vs_pagos`.`nro_pedido` AS `nro_pedido`,
        `cordovezApp`.`provisiones_vs_pagos`.`parcial` AS `parcial`,
        `cordovezApp`.`provisiones_vs_pagos`.`valor_provisionado` AS `valor_provisionado`,
        `cordovezApp`.`provisiones_vs_pagos`.`pago` AS `pago`,
        `cordovezApp`.`provisiones_vs_pagos`.`saldo` AS `saldo`
    FROM
        `cordovezApp`.`provisiones_vs_pagos`
    WHERE
        ((`cordovezApp`.`provisiones_vs_pagos`.`saldo` <> 0)
            AND (`cordovezApp`.`provisiones_vs_pagos`.`concepto` <> 'ISD')
            AND (`cordovezApp`.`provisiones_vs_pagos`.`fecha` > '2020-01-01'))
    ORDER BY `cordovezApp`.`provisiones_vs_pagos`.`concepto`