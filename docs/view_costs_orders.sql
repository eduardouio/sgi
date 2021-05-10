-- regimen 10
select 
	  p.nombre  producto,
    ddp.cod_contable,
    p.cod_ice,
    p.cantidad_x_caja,
    p.capacidad_ml,
    ddp.grado_alcoholico,
    s.nombre,
	  pf.nro_pedido,
    '0' id_pacial,
	  o.fecha_arribo,
    o.fecha_ingreso_almacenera,
    (o.fecha_llegada_cliente - o.fecha_arribo) as dias_transito,
    0 dias_permanencia_almagro,
    o.fecha_llegada_cliente,
    o.regimen,
    o.pais_origen,
    o.ciudad_origen,
    o.incoterm,
    (ddp.nro_cajas * p.cantidad_x_caja) unidades,
    (ddp.costo_caja / p.cantidad_x_caja) costo_unidad,
    if(pf.tipo_cambio = 1, 'USD', 'EUR') as moneda,
    (ddp.fob / (ddp.nro_cajas * p.cantidad_x_caja)) fob,
    (ddp.cif / (ddp.nro_cajas * p.cantidad_x_caja)) cif,
    ddp.ex_aduana_unitario,
    o.base_fodinfa,
    o.base_iva,
    o.base_ice_advalorem,
    o.base_ice_especifico,
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