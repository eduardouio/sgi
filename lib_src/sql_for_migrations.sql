-- correr este codigo SQL antes de hacer la 
-- migracion de la base de datos anterior

alter table pedido add column id_pedido int not null AUTO_INCREMENT UNIQUE
alter table proveedor add column id_proveedor int not null AUTO_INCREMENT UNIQUE
alter table producto add column id_producto int not null AUTO_INCREMENT UNIQUE
ALTER TABLE `factura_informativa_detalle` ADD `cantidad_x_caja` DECIMAL(12,3) NOT NULL DEFAULT '0' AFTER `seguro`;
