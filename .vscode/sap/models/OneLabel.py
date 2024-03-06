from django.db import models
from simple_history.models import HistoricalRecords
from products.models import Product


class OneLabel(models.Model):
    """ Tabla usada para activar etiquetas solas
    """
    
    STATUS_CHOICES = (
        ('I', 'Inactive'),
        ('S', 'Sended'),
        ('F', 'Signed'),
        ('A', 'Active'),
        ('D', 'Disabled'),
        ('R', 'Rejected'),
        ('E', 'Error'),
        ('V', 'Validated'),
    ) 
    id_one_label = models.AutoField(
        'id etqueta sola',
        primary_key=True
    )
    cod_contable = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    code_label = models.CharField(
        'codigo etiqueta',
        max_length=10
        )
    notas = models.TextField(
        'observaciones',
        default=None,
        null=True,
        blank=True
    )
    response = models.TextField(
        'Respuesta servidor',
        default=None,
        null=True,
        blank=True
    )
    message = models.CharField(
        'mensaje enviado',
        max_length=500,
        default=None,
        null=True,
        blank=True
    )
    sign = models.CharField(
        'firma mesaje',
        max_length=500,
        default=None,
        null=True,
        blank=True
    )
    message_status = models.TextField(
        'estado mensaje',
        default=None,
        null=True,
        blank=True
    )
    validated_date = models.DateTimeField(
        'validado el',
        default=None,
        blank=True,
        null=True
    )
    activated_date = models.DateTimeField(
        'activado el',
        default=None,
        blank=True,
        null=True
    )
    signed_date = models.DateTimeField(
        'firmado el',
        default=None,
        blank=True,
        null=True
    )
    bg_status = models.CharField(
        'Estado',
        max_length=15,
        default='I',
        choices=STATUS_CHOICES
    )
    id_user = models.SmallIntegerField(
        default=0
    )
    date_created = models.DateTimeField(
        'Fecha de Creación',
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        'Ultima Actualización',
        auto_now=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return '{} -> {}'.format(
            self.code_label,
            self.bg_status
        )
