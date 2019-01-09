-- correr este codigo SQL antes de hacer la 
-- migracion de la base de datos anterior

alter table pedido add column id_pedido int not null AUTO_INCREMENT UNIQUE
alter table proveedor add column id_proveedor int not null AUTO_INCREMENT UNIQUE
alter table producto add column id_producto int not null AUTO_INCREMENT UNIQUE

-- Verificar en base de datos de Produccion

-- Datos a eliminar de parcial
delete FROM parcial where `id_parcial` = 17 or `id_parcial` = 18 or `id_parcial` = 23 or `id_parcial` = 32 or `id_parcial` = 39 or `id_parcial` = 40 or `id_parcial` = 107 or `id_parcial` = 108 or `id_parcial` = 91

-- Eliminamos gastos de nacionalizacion huerfanos
delete FROM `gastos_nacionalizacion` where `id_parcial` = 17 or `id_parcial` = 18 or `id_parcial` = 23 or `id_parcial` = 32 or `id_parcial` = 39 or `id_parcial` = 40 or `id_parcial` = 107 or `id_parcial` = 108 or `id_parcial` = 91


-- Tabla de proveedores
ALTER TABLE `cordovezApp`.`proveedor` 
ADD COLUMN  `id_proveedor` INT(11) NOT NULL AUTO_INCREMENT ,
ADD UNIQUE INDEX `id_proveedor_UNIQUE` (`id_proveedor` ASC);


-- tabla de productos
ALTER TABLE `cordovezApp`.`producto` 
ADD COLUMN `id_producto` INT(11) NOT NULL AUTO_INCREMENT ,
ADD UNIQUE INDEX `id_producto_UNIQUE` (`id_producto` ASC);


--pedidos
ALTER TABLE `cordovezApp`.`pedido` 
ADD COLUMN `id_pedido` INT(11) NOT NULL AUTO_INCREMENT ,
ADD UNIQUE INDEX `id_pedido_UNIQUE` (`id_pedido` ASC);
