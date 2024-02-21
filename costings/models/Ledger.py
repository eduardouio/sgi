from django.db import models
from django.utils import timezone

from logs.app_log import loggin
from orders.models.Order import Order
from simple_history.models import HistoricalRecords


class Ledger(models.Model):
    id_mayor = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    nro_pedido = models.ForeignKey(
        Order,
        models.PROTECT,
        db_column='nro_pedido'
    )
    id_parcial = models.PositiveSmallIntegerField(default=0)
    costo_inicial_producto = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    costo_producto = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    descargas = models.DecimalField(
        max_digits=20, 
        decimal_places=13,
        default=0
    )
    saldo_producto = models.DecimalField(
        max_digits=20, 
        decimal_places=13,
        default=0
    ) # prox parcial
    precio_entrega = models.DecimalField(
        max_digits=20, 
        decimal_places=13,
        default=0
    )
    mayor_sap = models.DecimalField(
        max_digits=20, 
        decimal_places=13,
        default=0
    )
    provisiones_sap = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    mayor_sgi = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    provisiones_sgi = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    facturas_sgi = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    reliquidacion_ice = models.DecimalField(
        max_digits=20,
        decimal_places=13,
        default=0
    )
    # columna adicional para registrar en el mayor el impuesto
    bg_mayor = models.SmallIntegerField(default=0)
    last_update = models.DateTimeField(blank=True, null=True)
    id_user = models.PositiveIntegerField(blank=True, null=True)
    history = HistoricalRecords()
    date_create = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )

    def __str__(self):
        return ' '.join(
            [self.nro_pedido.nro_pedido, '->', str(self.id_parcial)]
        )

    class Meta:
        managed = True
        db_table = 'mayor'
        unique_together = (('nro_pedido', 'id_parcial', 'tipo'),)
        verbose_name_plural = 'Mayores Liquidaciones'
        ordering = ['nro_pedido', 'id_parcial','tipo']

    @classmethod
    def get_by_order(self, nro_order):
        ''' Get last complete ledger for order '''

        order = Order.get_by_order(nro_order)
        if order is None:
            return None

        if(order.regimen == '70'):
            loggin('e', 'No existe mayor de un pedido R70 {}'.format(
                order.nro_pedido))
            return None

        items = self.objects.filter(nro_pedido=order.nro_pedido)
        if items.count() == 0:
            loggin('w', 'El pedido {} no tiene mayor'.format(order.nro_pedido))
            return None

        return items.first()

    @classmethod
    def get_by_parcial(self, id_partial):
        '''Return ledger from partial include init expenses'''
        items = self.objects.filter(id_parcial=id_partial)
        if items.count() == 0:
            loggin(
                'w', 
                'El parcial {} no registra un mayor'
                .format(id_partial)
                )
            return None
        loggin('i', 'retornando mayor para el parcial {}'.format(id_partial))
        return items.first()

    @classmethod
    def get_by_order_and_partial(self, nro_order, id_partial):
        """Obtiene un mayor desde el pedido y parcial

        Arguments:
            nro_order {str}
            id_partial {int}
        """
        items = self.objects.filter(
            nro_pedido=nro_order,
            id_parcial=id_partial
        )
        if items.count() == 0:
            loggin(
                'w',
                'No existe un mayor para el pedido {} parcial {}'
                .format(nro_order, id_partial)
            )
            return None

        return items.first()