CREATE VIEW `reporte_provisiones_final` AS
    SELECT 
        `provisiones_vs_pagos`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,
        `provisiones_vs_pagos`.`concepto` AS `concepto`,
        `provisiones_vs_pagos`.`tipo` AS `tipo`,
        `provisiones_vs_pagos`.`fecha` AS `fecha`,
        `provisiones_vs_pagos`.`nro_pedido1` AS `nro_pedido1`,
        `provisiones_vs_pagos`.`incoterm` AS `incoterm`,
        `provisiones_vs_pagos`.`nro_pedido` AS `nro_pedido`,
        `provisiones_vs_pagos`.`parcial` AS `parcial`,
        `provisiones_vs_pagos`.`valor_provisionado` AS `valor_provisionado`,
        `provisiones_vs_pagos`.`pago` AS `pago`,
        `provisiones_vs_pagos`.`saldo` AS `saldo`
    FROM
        `provisiones_vs_pagos`
    WHERE
        ((`provisiones_vs_pagos`.`saldo` <> 0)
            AND (`provisiones_vs_pagos`.`concepto` <> 'ISD')
            AND (`provisiones_vs_pagos`.`fecha` > '2020-01-01'))
    ORDER BY `provisiones_vs_pagos`.`concepto`