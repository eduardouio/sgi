--
-- Correr estas consultas luego de realizar la migracion de la base de datos
--

alter table factura_informativa_detalle add column cantidad_x_caja decimal(12,3) default null;
alter table partials_historicalinfoinvoicedetail add column cantidad_x_caja decimal(12,3) default null;

alter table pedido add column id_pedido int not null unique auto_increment; 
alter table orders_historicalorder add column id_pedido int default null;

alter table proveedor add column id_proveedor int not null unique auto_increment; 
alter table suppliers_historicalsupplier add column id_proveedor int not null; 
