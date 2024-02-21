SELECT
    `p`.`id_parcial` AS `id`,
    `p`.`nro_pedido` AS `nro_pedido`,
    `s`.`nombre` AS `nombre`,
    `p`.`id_parcial` AS `id_parcial`,
    `o`.`nro_matricula` AS `origen`,
    `fid`.`product` AS `product`,
    `fid`.`capacidad_ml` AS `capacidad_ml`,
    `fid`.`nro_cajas` AS `nro_cajas`,
    `fid`.`cantidad_x_caja` AS `cantidad_x_caja`,
    `fid`.`unidades` AS `unidades`,
    `fi`.`nro_refrendo` AS `nro_refrendo`,
    `p`.`nro_liquidacion` AS `nro_liquidacion`,
    `p`.`fecha_liquidacion` AS `fecha_liquidacion`,
    `p`.`fecha_entrega_etiquetas_senae` AS `fecha_entrega_etiquetas_senae`,
    `p`.`fecha_pegado_etiquetas` AS `fecha_pegado_etiquetas`,
    `p`.`fecha_aforo` AS `fecha_aforo`,
    `p`.`fecha_salida_autorizada_almagro` AS `fecha_salida_autorizada`,
    `p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,
    `p`.`bg_isclosed` AS `bg_isclosed`,
    `p`.`bg_isliquidated` AS `bg_isliquidated`
FROM
    (
        (
            (
                (
                    (
                        `cordovezApp`.`factura_informativa_detalle` `fid`
                    LEFT JOIN `cordovezApp`.`factura_informativa` `fi`
                    ON
                        (
                            (
                                `fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`
                            )
                        )
                    )
                LEFT JOIN `cordovezApp`.`parcial` `p`
                ON
                    ((`p`.`id_parcial` = `fi`.`id_parcial`))
                )
            LEFT JOIN `cordovezApp`.`pedido` `o`
            ON
                ((`p`.`nro_pedido` = `o`.`nro_pedido`))
            )
        LEFT JOIN `cordovezApp`.`pedido_factura` `pf`
        ON
            ((`pf`.`nro_pedido` = `o`.`nro_pedido`))
        )
    LEFT JOIN `cordovezApp`.`proveedor` `s`
    ON
        (
            (
                `s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`
            )
        )
    )
WHERE
    (`p`.`bg_isliquidated` = 1)
UNION
SELECT
    `o`.`nro_pedido` AS `id`,
    `o`.`nro_pedido` AS `nro_pedido`,
    `s`.`nombre` AS `nombre`,
    '0' AS `id_parcial`,
    'CONSUMO' AS `origen`,
    `dpf`.`product` AS `product`,
    `dpf`.`capacidad_ml` AS `capacidad_ml`,
    `dpf`.`nro_cajas` AS `nro_cajas`,
    `dpf`.`cantidad_x_caja` AS `cantidad_x_caja`,
    `dpf`.`unidades` AS `unidades`,
    `o`.`nro_refrendo` AS `nro_refrendo`,
    `o`.`nro_liquidacion` AS `nro_liquidacion`,
    `o`.`fecha_liquidacion` AS `fecha_liquidacion`,
    `o`.`fecha_entrega_etiquetas_senae` AS `fecha_entrega_etiquetas_senae`,
    `o`.`fecha_pegado_etiquetas` AS `fecha_pegado_etiquetas`,
    `o`.`fecha_aforo` AS `fecha_aforo`,
    `o`.`fecha_salida_autorizada_puerto` AS `fecha_salida_autorizada`,
    `o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,
    `o`.`bg_isclosed` AS `bg_isclosed`,
    `o`.`bg_isliquidated` AS `bg_isliquidated`
FROM
    (
        (
            (
                `cordovezApp`.`detalle_pedido_factura` `dpf`
            LEFT JOIN `cordovezApp`.`pedido_factura` `pf`
            ON
                (
                    (
                        `pf`.`id_pedido_factura` = `dpf`.`id_pedido_factura`
                    )
                )
            )
        LEFT JOIN `cordovezApp`.`proveedor` `s`
        ON
            (
                (
                    `s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`
                )
            )
        )
    LEFT JOIN `cordovezApp`.`pedido` `o`
    ON
        ((`o`.`nro_pedido` = `pf`.`nro_pedido`))
    )
WHERE
    (`o`.`bg_isliquidated` = 1)