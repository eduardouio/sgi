CREATE VIEW v_costs_analysis 
AS
-- regimen 10
select 
	p.nombre  producto,
	s.nombre proveedor,
    ddp.cod_contable,
    p.cod_ice,
    p.cantidad_x_caja,
    p.capacidad_ml,
    ddp.grado_alcoholico,
	  pf.nro_pedido,
    '0' id_parcial,
	  o.fecha_arribo,
    o.fecha_ingreso_almacenera,
    IFNULL(DATEDIFF(o.fecha_llegada_cliente, o.fecha_arribo),0) dias_transito_puerto,
    0 dias_permanencia_almagro,
    IFNULL(DATEDIFF(o.fecha_llegada_cliente, o.fecha_arribo),0) dias_transito,
    o.fecha_llegada_cliente,
    o.regimen,
    o.pais_origen,
    o.ciudad_origen,
    o.incoterm,
    (ddp.nro_cajas * p.cantidad_x_caja) unidades,
    (ddp.costo_caja / p.cantidad_x_caja) costo_unidad,
    if(pf.tipo_cambio = 1, 'USD', 'EUR') as moneda,
    pf.tipo_cambio,
    (ddp.fob / (ddp.nro_cajas * p.cantidad_x_caja)) fob,
    (ddp.cif / (ddp.nro_cajas * p.cantidad_x_caja)) cif,
    ddp.ex_aduana_unitario,
    o.base_fodinfa,
    o.base_iva,
    o.base_ice_advalorem,
    o.base_ice_especifico,
    o.exoneracion_arancel,
    (ddp.total_ice / (ddp.nro_cajas * p.cantidad_x_caja)) total_ice,
    (ddp.fodinfa / (ddp.nro_cajas * p.cantidad_x_caja)) fodinfa,
    (ddp.arancel_advalorem_pagar / (ddp.nro_cajas * p.cantidad_x_caja)) arancel_advalorem,
    (ddp.arancel_especifico_pagar / (ddp.nro_cajas * p.cantidad_x_caja)) arancel_especifico,
    ((
		ddp.total_ice
		+ ddp.fodinfa
		+ ddp.arancel_advalorem_pagar
		+ ddp.arancel_especifico_pagar
    ) / (ddp.nro_cajas * p.cantidad_x_caja)) tributos,
    ((ddp.costo_caja * pf.tipo_cambio)/ p.cantidad_x_caja) costo_sap,
    (
    (ddp.prorrateos_total - ddp.total_ice - ddp.fodinfa - ddp.arancel_advalorem_pagar - ddp.arancel_especifico_pagar) 
		/ (ddp.nro_cajas * p.cantidad_x_caja)) indirectos_pe,
    (
  (
    ddp.indirectos - ddp.total_ice - ddp.fodinfa - ddp.arancel_advalorem_pagar - ddp.arancel_especifico_pagar
  ) / (ddp.nro_cajas * p.cantidad_x_caja)
) indirectos_pr,
(
  (
    ddp.costo_total / ((ddp.nro_cajas * p.cantidad_x_caja))
  ) - (
    (
      ddp.total_ice + ddp.fodinfa + ddp.arancel_advalorem_pagar + ddp.arancel_especifico_pagar
    ) / (ddp.nro_cajas * p.cantidad_x_caja)
  ) - (
    (ddp.costo_caja * pf.tipo_cambio) / p.cantidad_x_caja
  )
) indirectos,
    (ddp.costo_total / ((ddp.nro_cajas * p.cantidad_x_caja))) costo_botella
from 
	detalle_pedido_factura ddp
left join pedido_factura pf on (pf.id_pedido_factura = ddp.id_pedido_factura)
left join proveedor as s on s.identificacion_proveedor = pf.identificacion_proveedor
left join producto p on (p.cod_contable = ddp.cod_contable)
left join pedido o on (pf.nro_pedido = o.nro_pedido)
where
o.regimen = '10'
and o.bg_isclosed = 1
and ddp.costo_caja_final > 0
UNION
-- parciales
select 
p.nombre producto,
s.nombre proveedor,
ddp.cod_contable,
p.cod_ice,
p.cantidad_x_caja,
p.capacidad_ml,
fid.grado_alcoholico,
pf.nro_pedido,
pc.id_parcial,
o.fecha_arribo,
o.fecha_ingreso_almacenera,
IFNULL(DATEDIFF(o.fecha_ingreso_almacenera, o.fecha_arribo),0) dias_transito_puerto,
IFNULL(DATEDIFF(pc.fecha_llegada_cliente, o.fecha_ingreso_almacenera),0) dias_permanencia_almagro,
IFNULL(DATEDIFF(pc.fecha_llegada_cliente, o.fecha_arribo),0) dias_transito,
pc.fecha_llegada_cliente,
o.regimen,
o.pais_origen,
o.ciudad_origen,
o.incoterm,
(fid.nro_cajas * p.cantidad_x_caja) unidades,
(ddp.costo_caja / p.cantidad_x_caja) costo_unidad,
if(pf.tipo_cambio = 1, 'USD', 'EUR') as moneda,
pf.tipo_cambio,
(fid.fob / (fid.nro_cajas * p.cantidad_x_caja)) fob,
(fid.cif / (fid.nro_cajas * p.cantidad_x_caja)) cif,
fid.ex_aduana_unitario,
pc.base_fodinfa,
pc.base_iva,
pc.base_ice_advalorem,
pc.base_ice_especifico,
pc.exoneracion_arancel,
(fid.total_ice / (fid.nro_cajas * p.cantidad_x_caja)) total_ice,
(fid.fodinfa / (fid.nro_cajas * p.cantidad_x_caja)) fodinfa,
(fid.arancel_advalorem_pagar / (fid.nro_cajas * p.cantidad_x_caja)) arancel_advalorem,
(fid.arancel_especifico_pagar / (fid.nro_cajas * p.cantidad_x_caja)) arancel_especifico,
((
		fid.total_ice
		+ fid.fodinfa
		+ fid.arancel_advalorem_pagar
		+ fid.arancel_especifico_pagar
    ) / (fid.nro_cajas * p.cantidad_x_caja)) tributos,
((ddp.costo_caja * pf.tipo_cambio)/ p.cantidad_x_caja) costo_sap,
((fid.prorrateos_total - fid.total_ice - fid.fodinfa - fid.arancel_advalorem_pagar - fid.arancel_especifico_pagar) 
		/ (fid.nro_cajas * p.cantidad_x_caja)
) indirectos_pe,
(
  (
    fid.indirectos - fid.total_ice - fid.fodinfa - fid.arancel_advalorem_pagar - fid.arancel_especifico_pagar
  ) / (fid.nro_cajas * p.cantidad_x_caja)
) indirectos_pr,
(
  (fid.costo_total / ((fid.nro_cajas * p.cantidad_x_caja))) 
  - 
  ((fid.total_ice + fid.fodinfa + fid.arancel_advalorem_pagar + fid.arancel_especifico_pagar) / (fid.nro_cajas * p.cantidad_x_caja))
  -
  ((ddp.costo_caja * pf.tipo_cambio)/ p.cantidad_x_caja)
) indirectos,
(fid.costo_total / ((fid.nro_cajas * p.cantidad_x_caja))) costo_botella
from factura_informativa_detalle fid
left join factura_informativa fi on (fi.id_factura_informativa = fid.id_factura_informativa)
left join parcial pc on (pc.id_parcial = fi.id_parcial)
left join pedido o on (o.nro_pedido = pc.nro_pedido)
left join detalle_pedido_factura ddp on (ddp.detalle_pedido_factura = fid.detalle_pedido_factura)
left join producto p on (p.cod_contable = ddp.cod_contable)
left join pedido_factura pf on(pf.id_pedido_factura = ddp.id_pedido_factura)
left join proveedor as s on s.identificacion_proveedor = pf.identificacion_proveedor
where pc.bg_isclosed = 1