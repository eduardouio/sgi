"""
Retorna todas las facturas de un pedido, incluyendo las facturas de producto
asi como la de los parciales
el resultado debe ser presentado de la siguiente manera
{
'total' : {
    'invoiced' : float,
    'provisioned' : float,
    'diff' : float,
    }
'product' : {
    'invoice_value' : float,
    'type_change' : float,
    'invoiced': bool,
    'items_invoice' : list
    }
'init_expenses':{
    'invoice_value' : float,
    'provisions' : float,
    'diff' : float,
    }
'partials' : [
    'id_partial' : {
        'invoice_value' : float,
        'provisions' : float,
        'diff' : float,
    }]
}
"""
