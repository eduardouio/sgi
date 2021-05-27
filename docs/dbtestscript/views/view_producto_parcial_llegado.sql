CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `cordovezApp`.`producto_parcial_llegado` AS
    SELECT 
        `fid`.`id_factura_informativa` AS `id_factura_informativa`,
        `p`.`nro_pedido` AS `nro_pedido`,
        `o`.`proveedor` AS `proveedor`,
        `fi`.`nro_factura_informativa` AS `nro_factura_informativa`,
        `fi`.`nro_refrendo` AS `nro_refrendo`,
        `fid`.`product` AS `product`,
        `fid`.`capacidad_ml` AS `capacidad_ml`,
        `fid`.`grado_alcoholico` AS `grado_alcoholico`,
        `fid`.`nro_cajas` AS `nro_cajas`,
        `fid`.`unidades` AS `unidades`,
        `p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`
    FROM
        (((`cordovezApp`.`factura_informativa_detalle` `fid`
        LEFT JOIN `cordovezApp`.`factura_informativa` `fi` ON ((`fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`)))
        LEFT JOIN `cordovezApp`.`parcial` `p` ON ((`p`.`id_parcial` = `fi`.`id_parcial`)))
        LEFT JOIN `cordovezApp`.`pedido` `o` ON ((`p`.`nro_pedido` = `o`.`nro_pedido`)))
    ORDER BY `p`.`fecha_llegada_cliente` , `fi`.`id_factura_informativa`