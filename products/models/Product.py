from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from simple_history.models import HistoricalRecords
from suppliers.models.Supplier import Supplier

STATUS_CHOICES = (
    ('Activo', 'Activo'),
    ('Cancelado', 'Cancelado'),
    ('Vencido', 'Vencido'),
    ('No Renovar', 'No Renovar'),
)

STATUS_PRODUCT = (
    (1, 'ACTIVO'),
    (0, 'INACTIVO'),
)

ARMY_CUSTODY = (
    (1, '1 CUSTODIA'),
    (2, '2 CUSTODIAS'),
)


class Product(models.Model):
    cod_contable = models.CharField(primary_key=True, max_length=20)
    identificacion_proveedor = models.ForeignKey(
        Supplier, models.PROTECT,
        db_column='identificacion_proveedor'
    )
    id_producto = models.PositiveIntegerField(unique=True)
    nro_registro_sanitario = models.CharField(max_length=25, default=None)
    fecha_emision_registro = models.DateField(
        blank=True,
        null=True,
        default=None
    )
    fecha_vencimiento_registro = models.DateField(
        blank=True,
        null=True,
        default=None
    )
    estado_registro = models.CharField(
        max_length=70,
        default='Activo',
        null=True,
        choices=STATUS_CHOICES
        )
    solicitud_aucp = models.CharField(max_length=50, default=None, null=True)
    grado_alcoholico = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )
    nombre = models.CharField(unique=True, max_length=70)
    nombre_extrangero = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        default=None
    )
    partida_arancelaria = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default=None
    )
    subpartida_arancelaria = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default=None
    )
    tnan_codigo = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default=None
    )
    cod_ice = models.CharField(max_length=39, default='SIN CODIDO ICE')
    capacidad_ml = models.SmallIntegerField(default=1)
    cantidad_x_caja = models.SmallIntegerField(default=1)
    costo_caja = models.DecimalField(
        max_digits=16,
        decimal_places=10,
        default=0.00
    )
    estado = models.IntegerField(default=1, choices=STATUS_PRODUCT)
    custodia_doble = models.IntegerField(default=0, choices=ARMY_CUSTODY)
    peso = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        default=0,
        blank=True,
        null=True
    )
    pais_origen = models.CharField(max_length=70, blank=True, null=True)
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    # se puede subir un solo archivo pdf para el registro sanitario
    registro_sanitario = models.FileField(
        upload_to='registro_sanitario/',
        blank=True,
        null=True,
        default=None
    )
    id_user = models.SmallIntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'producto'
        ordering = ['identificacion_proveedor', 'nombre']
        verbose_name_plural = 'Productos'

    @classmethod
    def get_by_cod_contable(self, cod_contable):
        try:
            return self.objects.get(pk=cod_contable)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_all(self):
        return self.objects.all()

    @classmethod
    def get_by_supplier(self, id_supplier):
        pass

    @classmethod
    def get_new_id_producto(cls):
        """Retorna el id autoincremental que le corresponde al producto nuevo
        """
        las_product = cls.objects.raw(
            'SELECT * FROM producto order by id_producto desc limit 1'
        )

        for product in las_product:
            return product.id_producto + 1
