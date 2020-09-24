"""
Entrega los costos de descarga para cada uno de los pacriales o del pedido
completo, si es un pedido R10 se simula un parcial y se coloca la informacio
del de la descarga
{
    order : str,
    partials : [
        'p1' : {
            id_partial : int,
            fob_partial_tct : int,
            indirects : float,
            total_costs : float,
        }
    ]
}
"""
