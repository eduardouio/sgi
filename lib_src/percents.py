"""
Obtiene los porcentuales de los parciales de un pedido
el 100% es el total del pedido mientras que cada parcial tiene
su proporcionalidad del porcentaje total

{
    order : str,
    fob_init_tct : float,
    consumed_fob_tct : float,
    percent_consumed_fob_tct: float,
    sale_fob_tct : float,
    persent_sale_fob : float,
    total_partials : int,
    partials : [
        fob_tct : float,
        percent_init_fob_tct: float,
        percent_sale_fob_tct : float,
    ]
    is_closed : bool,
    have_sale : bool  # i can use it like condition for close a order
}
"""
