-- correr este codigo SQL antes de hacer la 
-- migracion de la base de datos anterior

alter table pedido add column id_pedido int not null AUTO_INCREMENT UNIQUE;
alter table proveedor add column id_proveedor int not null AUTO_INCREMENT UNIQUE;
alter table producto add column id_producto int not null AUTO_INCREMENT UNIQUE;
ALTER TABLE `factura_informativa_detalle` ADD `cantidad_x_caja` DECIMAL(12,3) NOT NULL DEFAULT '0' AFTER `seguro`;


alter table orders_historicalorder add column id_pedido int not null AUTO_INCREMENT UNIQUE;
alter table suppliers_historicalsupplier add column id_proveedor int not null AUTO_INCREMENT UNIQUE;
alter table products_historicalproduct add column id_producto int not null AUTO_INCREMENT UNIQUE;
ALTER TABLE `partials_historicalinfoinvoicedetail` ADD `cantidad_x_caja` DECIMAL(12,3) NOT NULL DEFAULT '0' AFTER `seguro`;




create view facturas_proveedor_pendientes as
SELECT
    `pf`.`nro_pedido` AS `nro_pedido`,
    `pr`.`nombre` AS `nombre`,
    `pf`.`id_factura_proveedor` AS `id_factura_proveedor`,
    `pf`.`valor` AS `valor`
FROM
    (
        `pedido_factura` `pf`
    JOIN `proveedor` `pr`
    ON
        (
            (
                `pf`.`identificacion_proveedor` = `pr`.`identificacion_proveedor`
            )
        )
    )
WHERE
    (
        `pf`.`id_factura_proveedor` LIKE 'SF-%'
    );


create view producto_parcial_llegado as 
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
    (
        (
            (
                `factura_informativa_detalle` `fid`
            LEFT JOIN `factura_informativa` `fi`
            ON
                (
                    (
                        `fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`
                    )
                )
            )
        LEFT JOIN `parcial` `p`
        ON
            ((`p`.`id_parcial` = `fi`.`id_parcial`))
        )
    LEFT JOIN `pedido` `o`
    ON
        ((`p`.`nro_pedido` = `o`.`nro_pedido`))
    )
ORDER BY
    `p`.`fecha_llegada_cliente`,
    `fi`.`id_factura_informativa`;


create view provisiones_vs_pagos as
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
    (
    SELECT
        IFNULL(SUM(`ddp`.`valor`),
        0)
    FROM
        `detalle_documento_pago` `ddp`
    WHERE
        (
            `ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`
        )
) AS `pago`,
(
    `gn`.`valor_provisionado` -(
    SELECT
        IFNULL(SUM(`ddp`.`valor`),
        0)
    FROM
        `detalle_documento_pago` `ddp`
    WHERE
        (
            `ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`
        )
)
) AS `saldo`
FROM
    (
        (
            `gastos_nacionalizacion` `gn`
        LEFT JOIN `parcial` `p`
        ON
            (
                (
                    (`p`.`id_parcial` = `gn`.`id_parcial`) AND(`gn`.`id_parcial` <> 0)
                )
            )
        )
    LEFT JOIN `pedido` `o`
    ON
        (
            (
                (
                    IFNULL(`p`.`nro_pedido`, `gn`.`nro_pedido`) = `o`.`nro_pedido`
                ) AND(`gn`.`concepto` <> 'ISD') AND(`gn`.`concepto` <> 'TRANSPORTE') AND(
                    `gn`.`concepto` <> 'MANO DE OBRA ETIQUETADO'
                ) AND(`gn`.`concepto` <> 'DESCARGA') AND(`gn`.`concepto` <> 'ISD') AND(`gn`.`fecha` > '2018-12-31')
            )
        )
    )
ORDER BY
    `gn`.`tipo`,
    `gn`.`fecha`,
    `gn`.`concepto`;



create view stockActiveProductsInCustomsView as 

SELECT
    `pf`.`nro_pedido` AS `nro_pedido`,
    `ped`.`regimen` AS `regimen`,
    `dpf`.`id_pedido_factura` AS `id_pedido_factura`,
    `pf`.`id_factura_proveedor` AS `id_factura_proveedor`,
    `pf`.`identificacion_proveedor` AS `identificacion_proveedor`,
    `prov`.`nombre` AS `proveedor`,
    `dpf`.`detalle_pedido_factura` AS `detalle_pedido_factura`,
    `pro`.`nombre` AS `producto`,
    `dpf`.`costo_caja` AS `costo_caja`,
    `dpf`.`cod_contable` AS `cod_contable`,
    `dpf`.`grado_alcoholico` AS `grado_alcoholico`,
    `dpf`.`nro_cajas` AS `nro_cajas`,
    `pro`.`capacidad_ml` AS `capacidad_ml`,
    `pro`.`cantidad_x_caja` AS `cantidad_x_caja`
FROM
    (
        (
            (
                (
                    `detalle_pedido_factura` `dpf`
                LEFT JOIN `producto` `pro`
                ON
                    (
                        (
                            `dpf`.`cod_contable` = `pro`.`cod_contable`
                        )
                    )
                )
            LEFT JOIN `pedido_factura` `pf`
            ON
                (
                    (
                        `dpf`.`id_pedido_factura` = `pf`.`id_pedido_factura`
                    )
                )
            )
        LEFT JOIN `pedido` `ped`
        ON
            (
                (`pf`.`nro_pedido` = `ped`.`nro_pedido`)
            )
        )
    LEFT JOIN `proveedor` `prov`
    ON
        (
            (
                `pf`.`identificacion_proveedor` = `prov`.`identificacion_proveedor`
            )
        )
    )
WHERE
    (`dpf`.`nro_cajas` > 0)
ORDER BY
    `pf`.`nro_pedido`;


INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$120000$gNt7lujazrOh$3koiXN49pfWan4CiX6H6tx6vdBiQGVNfuhiypX33YZI=', '2019-06-10 19:42:38.212150', 1, 'eduardo', '', '', 'eduardouio7@gmail.com', 1, 1, '2019-02-14 20:15:12.711458'),
(3, 'pbkdf2_sha256$120000$dbuIVatfksLF$3ckQIQ0J6bL/fcjUZms6KDfkEn72ajiahxN5lPlKxy0=', '2019-06-05 22:20:41.622541', 0, 'acardenas', 'Adrian', 'Cardenas', 'acardenas@vinesa.com.ec', 1, 1, '2019-02-25 19:40:03.000000'),
(23, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'aleon', 'ALEXANDRA', 'LEON', 'info6@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(24, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'avargas', 'ALEXANDRA', 'VARGAS', 'info7@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(25, 'pbkdf2_sha256$120000$xdflKeeTzahc$RxvLQLdCUloVMt5bBWQPdP4eEDNUcJV/fPBOKaCstW8=', '2019-05-28 14:48:13.745368', 0, 'cfelix', 'CECILIA', 'FELIX', 'cfelix@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(26, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'dmaza', 'DANIEL', 'MAZA', 'bodega1@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(27, 'pbkdf2_sha256$120000$T4LLGCOrEdwL$PiVEAHIHRQH1L84Fkc+WIZit0M0D3eHeEIbH6XsXokc=', '2019-03-07 15:43:58.135108', 0, 'esala', 'ELIZABETH', 'SALA', 'info20@vinesa.com', 1, 1, '2019-02-25 14:49:15.000000'),
(28, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'evillota', 'EDUARDO', 'VILLOTA', 'eduardouio7@gmail.com', 1, 1, '2019-02-25 14:49:15.000000'),
(29, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'fcordovez', 'FELIPE', 'CORDOVEZ', 'fcordovez@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(30, 'pbkdf2_sha256$120000$5ZYK8VYnbXMt$5itItpUnl0QOlCFnAs6vXS379JnUJsPLlPu2rVNzf68=', '2019-05-30 19:47:03.097044', 0, 'galarcon', 'GABRIELA', 'ALARCON', 'galarcon@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(31, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'jcarrillo', 'JEANNETH', 'CARRILLO', 'jcarrillo@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(32, 'pbkdf2_sha256$120000$jcArDzfftxWr$UChCAlefOCHrvMxMMf5ZivAG4aERfA06ULIlWl0Ks/s=', '2019-04-04 21:45:05.022838', 0, 'jcruz', 'JONATHAN', 'CRUZ', 'info9@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(33, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'jpacheco', ' JEFERSON', 'PACHECO', 'jpacheco@vinesa.com', 1, 1, '2019-02-25 14:49:15.000000'),
(34, 'pbkdf2_sha256$120000$nHY04zL5iJOX$RrYXyGXckyLiZAwcTQyDfMavgiWUAAO4Fvcdy3kQNeM=', '2019-06-10 17:30:24.317668', 0, 'klema', 'KARLA', 'LEMA', 'klema@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(35, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'ktoapanta', 'KAROL', 'TOAPANTA', 'info19@vinesa.com.', 1, 1, '2019-02-25 14:49:15.000000'),
(36, 'pbkdf2_sha256$120000$5aVT9pAbPnmy$d5gcJ6symB7dKJ7Ptax/AekyPEnmHkRXKVQLSJj/6cU=', '2019-06-07 18:48:55.413689', 0, 'msanti', 'MARIA ELENA', 'SANTI', 'msanti@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(37, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'mteran', 'MARIA ELENA', 'TERAN', 'mteran@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(38, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'randrade', 'RUTH', 'ANDRADE', 'Randrade@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(39, 'pbkdf2_sha256$120000$Ni51JSLWmsCd$B2AcoYLqyAV3LY2s9JI3+MvtbbUX4YW8yF5lJG+aO4w=', NULL, 0, 'vponce', 'VERONICA', 'PONCE', 'info2@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(40, 'pbkdf2_sha256$120000$O6Zo07rWOCaD$UlqM3ib3qu4gP38NmwEdx2ZBkeNtxyOhI8QKna0x5f4=', '2019-05-30 19:52:02.431513', 0, 'ypaccha', 'YOVANA', 'PACHA', 'infoc1@vinesa.com.ec', 1, 1, '2019-02-25 14:49:15.000000'),
(41, 'pbkdf2_sha256$120000$fJRZYIBRoXAX$lVVbaWtXKh+CNMKEf0MvO1HDbmhWXvPMkD4TIp59otk=', '2019-06-10 17:29:37.746290', 0, 'amolina', 'Ana Cristina', 'Molina', '', 1, 1, '2019-03-21 17:53:29.000000'),
(42, 'pbkdf2_sha256$120000$WadsjFXRpFcT$slVVmdRPFxfGEgOOiMMrhBRokomBFmmQS/sYKCuPOxo=', NULL, 0, 'emendoza', '', '', '', 1, 1, '2019-03-25 21:45:17.000000');



INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'contabilidad');


INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 3, 1),
(5, 25, 1),
(8, 27, 1),
(6, 30, 1),
(7, 32, 1),
(2, 34, 1),
(3, 36, 1),
(4, 40, 1),
(9, 41, 1),
(10, 42, 1);


INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(2, 1, 1),
(3, 1, 2),
(4, 1, 3),
(5, 1, 4),
(6, 1, 14),
(7, 1, 16),
(69, 1, 21),
(71, 1, 22),
(73, 1, 23),
(74, 1, 24),
(8, 1, 33),
(9, 1, 34),
(10, 1, 35),
(11, 1, 36),
(12, 1, 37),
(13, 1, 38),
(14, 1, 39),
(15, 1, 40),
(76, 1, 42),
(78, 1, 44),
(80, 1, 46),
(82, 1, 48),
(17, 1, 50),
(19, 1, 52),
(20, 1, 54),
(21, 1, 56),
(22, 1, 58),
(23, 1, 60),
(24, 1, 62),
(25, 1, 64),
(26, 1, 66),
(28, 1, 68),
(30, 1, 70),
(31, 1, 72),
(32, 1, 74),
(33, 1, 76),
(34, 1, 78),
(35, 1, 80),
(36, 1, 82),
(37, 1, 84),
(38, 1, 86),
(39, 1, 88),
(40, 1, 98),
(41, 1, 100),
(42, 1, 102),
(43, 1, 104),
(44, 1, 113),
(45, 1, 114),
(46, 1, 115),
(47, 1, 116),
(48, 1, 117),
(49, 1, 118),
(50, 1, 119),
(51, 1, 120),
(52, 1, 121),
(53, 1, 122),
(54, 1, 123),
(55, 1, 124),
(56, 1, 125),
(57, 1, 126),
(58, 1, 127),
(1, 1, 128),
(59, 1, 130),
(60, 1, 132),
(61, 1, 134),
(62, 1, 136),
(63, 1, 138),
(64, 1, 140),
(65, 1, 142),
(66, 1, 144),
(67, 1, 146),
(68, 1, 148),
(70, 1, 150),
(72, 1, 152),
(75, 1, 170),
(77, 1, 172),
(79, 1, 174),
(81, 1, 176),
(16, 1, 178),
(18, 1, 180),
(27, 1, 196),
(29, 1, 198);