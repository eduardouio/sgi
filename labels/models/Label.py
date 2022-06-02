from django.db import models
from orders.models import OrderInvoiceDetail
from simple_history.models import HistoricalRecords


class Label(models.Model):
    """
        Las Etiquetas se asocian al todo el pedido, en caso de necesitar un
        detalle por parcial se tomara en cuenta la fecha de inscripcion de
        las etiquetas en el sistema

    Args:
        models (_type_): _description_
    """
    STATUS_CHOICES = (
        ('I', 'Inactive'),
        ('S', 'Sended'),
        ('A', 'Active'),
        ('D', 'Disabled'),
    )
    id_label = models.AutoField(primary_key=True)
    id_factura_detalle = models.ForeignKey(
        OrderInvoiceDetail,
        on_delete=models.CASCADE,
        db_column='detalle_pedido_factura'
    )
    initial_range = models.CharField(
        'Rango Inicial',
        max_length=15,
        unique=True
    )
    end_range = models.CharField(
        'Rango Final',
        max_length=15,
        unique=True
    )
    quantity = models.IntegerField('Cantidad', default=0)
    parcial = models.SmallIntegerField('Parcial', default=0)
    notas = models.TextField(default=None, null=True, blank=True)
    bg_status = models.CharField(
        'Estado',
        max_length=15,
        default='I',
        choices=STATUS_CHOICES
    )
    id_user = models.SmallIntegerField(default=0)
    date_created = models.DateTimeField(
        'Fecha de Creación',
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        'Ultima Actualización',
        auto_now=True,
    )

    last_jwt = models.TextField(default=None, null=True, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return '{}-{}'.format(
            self.initial_range,
            self.end_range
        )

    @classmethod
    def get_last_jwt(cls):
        """
            Obtiene el ultimo jwt de una etiqueta
        """
        last_label = cls.objects.all().last()
        if (last_label.last_jwt):
            return last_label.jwt

        return False
