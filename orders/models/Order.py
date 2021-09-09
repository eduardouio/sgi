from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin

TYPE_CHARGE = (
    ('Carga Suelta', 'Carga Suelta'),
    ('Carga Contenerizada', 'Carga Contenerizada'),
    ('Otro', 'Otro'),
)

TYPE_FREIGHT = (
    ('Marítimo', 'Marítimo'),
    ('Aereo', 'Aereo'),
    ('Terrestre', 'Terrestre'),
    ('Otro', 'Otro'),
)


class Order(models.Model):
    nro_pedido = models.CharField(primary_key=True, max_length=6)
    regimen = models.CharField(max_length=2, default='00')
    flete_aduana = models.DecimalField(max_digits=10, decimal_places=4)
    seguro_aduana = models.DecimalField(max_digits=10, decimal_places=4)
    incoterm = models.CharField(max_length=4)
    pais_origen = models.CharField(max_length=45, blank=True, null=True)
    ciudad_origen = models.CharField(max_length=45, blank=True, null=True)
    fecha_embarque = models.DateField(blank=True, null=True)
    agente_embarque_forwarder = models.CharField(
        max_length=70,
        blank=True,
        null=True
    )
    tipo_carga = models.CharField(
        max_length=45,
        blank=True,
        null=True,
        choices=TYPE_CHARGE,
        default=None
    )
    tipo_flete = models.CharField(
        max_length=70,
        blank=True,
        null=True,
        choices=TYPE_FREIGHT,
        default=None
    )
    peso_carga = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=None
    )
    volumen_carga_cbm = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=None
    )
    nro_seguimiento_formarder = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=None
    )
    fecha_arribo = models.DateField(blank=True, null=True)
    dias_libres = models.PositiveIntegerField(default=21)
    fecha_salida_bodega_puerto = models.DateField(blank=True, null=True)
    fecha_ingreso_almacenera = models.DateField(blank=True, null=True)
    fecha_salida_almacenera = models.DateField(blank=True, null=True)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    fecha_llegada_cliente = models.DateField(blank=True, null=True)
    fecha_salida_autorizada_puerto = models.DateTimeField(
        blank=True,
        null=True
    )
    fecha_cierre = models.DateField(blank=True, null=True)
    fecha_salida_origen = models.DateField(blank=True, null=True)
    fecha_declaracion_inicial = models.DateField(blank=True, null=True)
    fecha_ingreso_puerta = models.DateField(blank=True, null=True)
    fecha_movilizacion_contenedor = models.DateField(blank=True, null=True)
    fecha_envio_documentos = models.DateField(blank=True, null=True)
    fecha_entrega_etiquetas_senae = models.DateField(blank=True, null=True)
    fecha_pegado_etiquetas = models.DateField(blank=True, null=True)
    fecha_aforo = models.DateField(blank=True, null=True)
    fecha_envio_de_documentos = models.DateField(blank=True, null=True)
    fecha_aprovacion_compra = models.DateField(blank=True, null=True)
    fecha_llegada_documentos = models.DateField(blank=True, null=True)
    fecha_aprovacion_dai = models.DateField(blank=True, null=True)
    fecha_emision_bl = models.DateField(blank=True, null=True)

    otros = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        null=True
    )
    comentarios = models.CharField(max_length=250, blank=True, null=True)
    observaciones = models.CharField(max_length=500, blank=True, null=True)
    nro_refrendo = models.CharField(max_length=22, blank=True, null=True)
    nro_aplicacion = models.CharField(max_length=8, blank=True, null=True)
    nro_poliza = models.CharField(max_length=8, blank=True, null=True)
    tipo_cambio_impuestosr10 = models.DecimalField(
        db_column='tipo_cambio_impuestosR10',
        max_digits=14,
        decimal_places=12,
        blank=True,
        null=True,
        default=1
    )
    tipo_cambio_almacenerar70 = models.DecimalField(
        db_column='tipo_cambio_almaceneraR70',
        max_digits=14,
        decimal_places=12,
        blank=True,
        null=True,
        default=1
    )
    exoneracion_arancel = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        default=0
    )
    nro_liquidacion = models.CharField(max_length=12, blank=True, null=True)
    fodinfa = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    fodinfa_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    ice_advalorem = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    ice_advalorem_reliquidado = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        blank=True,
        null=True
    )
    ice_advalorem_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    ice_especifico = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    ice_especifico_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    iva = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    iva_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    arancel_especifico_pagar = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True
    )
    arancel_especifico_pagar_pagado = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True
    )
    arancel_advalorem_pagar = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True
    )
    arancel_advalorem_pagar_pagado = models.DecimalField(
        max_digits=16,
        decimal_places=0,
        blank=True,
        null=True
    )
    liquidacion_con_tasa = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )
    base_arancel_advalorem = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    base_arancel_especifico = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0)
    base_ice_especifico = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    base_ice_advalorem = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    porcentaje_ice_advalorem = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0)
    base_iva = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0)
    base_fodinfa = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    base_etiquetas = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    tipo_cambio_go = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        default=1
    )
    id_user_cierre = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=0
    )
    gasto_origen = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        null=True,
        default=0
    )
    notas_cierre = models.CharField(max_length=200, blank=True, null=True)
    bg_have_close_parcial = models.IntegerField(blank=True, null=True)
    docentry = models.IntegerField(blank=True, null=True)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    url_dai_1 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_2 = models.CharField(max_length=600, blank=True, null=True)
    url_dai_3 = models.CharField(max_length=600, blank=True, null=True)
    path_dai_1 = models.FileField(
        upload_to='dais/',
        max_length=600,
        blank=True,
        null=True
    )
    path_dai_2 = models.FileField(
        upload_to='dais/',
        max_length=600,
        blank=True,
        null=True
    )
    path_dai_3 = models.FileField(
        upload_to='dais/',
        max_length=600,
        blank=True,
        null=True
    )
    url_liquidacion_1 = models.CharField(max_length=600, blank=True, null=True)
    url_liquidacion_2 = models.CharField(max_length=600, blank=True, null=True)
    url_liquidacion_3 = models.CharField(max_length=600, blank=True, null=True)
    # Indica el tipo de aforo asignado por la SENAE
    TYPE_INSPECTION = (
        ('AUTOMATICO', 'AUTOMATICO'),
        ('DOCUMENTAL', 'DOCUMENTAL'),
        ('FISICO', 'FISICO'),
    )
    tipo_aforo = models.CharField(
        max_length=50,
        choices=TYPE_INSPECTION,
        blank=True,
        null=True
    )
    # Estado en Aduana
    TYPE_STATUS_SENAE = (
        ('PENDIENTE', 'PENDIENTE'),
        ('EN PROCESO SENAE', 'EN PROCESO SENAE'),
        ('OBSERVADO', 'OBSERVADO'),
        ('SALIDA AUTORIZADA', 'SALIDA AUTORIZADA')
    )
    estado_senae = models.CharField(
        max_length=50,
        choices=TYPE_STATUS_SENAE,
        blank=True,
        null=True,
        default='PENDIENTE'
    )
    # Estado Embarque
    TYPE_STATUS_SHIPMENT = (
        ('RESERVA PENDIENTE', 'RESERVA PENDIENTE'),
        ('RESERA CONFIRMADA', 'RESERA CONFIRMADA'),
        ('EMBARCADO', 'EMBARCADO')
        ('LLEGADO', 'LLEGADO')
    )
    estado_embarque = models.CharField(
        max_length=70,
        choices=TYPE_STATUS_SHIPMENT,
        blank=True,
        null=True,
        default='RESERVA PENDIENTE'
    )
    # proforma proveedor de producto
    nro_proforma = models.CharField(max_length=25)
    path_liquidacion_1 = models.FileField(
        upload_to='liquidaciones/',
        max_length=600,
        blank=True,
        null=True
    )
    path_liquidacion_2 = models.FileField(
        upload_to='liquidaciones/',
        max_length=600,
        blank=True,
        null=True
    )
    path_liquidacion_3 = models.FileField(
        upload_to='liquidaciones/',
        max_length=600,
        blank=True,
        null=True
    )
    nro_bl = models.CharField(max_length=70, blank=True, null=True)
    nro_hbl_awb = models.CharField(max_length=70, blank=True, null=True)
    puerto_destino = models.CharField(max_length=70, blank=True, null=True)
    nro_matricula = models.CharField(max_length=11, blank=True, null=True)
    numero_de_carga_mrn = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    embarcador = models.CharField(max_length=70, blank=True, null=True)
    agente_aduana = models.CharField(max_length=100, blank=True, null=True)
    ruc_agente_aduana = models.CharField(max_length=13, blank=True, null=True)
    punto_lledada = models.CharField(max_length=60, blank=True, null=True)
    etiquetas_pegadas = models.IntegerField(blank=True, null=True)
    bg_have_tasa_control = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )
    bg_isliquidated = models.IntegerField(blank=True, null=True, default=0)
    bg_isclosed = models.IntegerField(blank=True, null=True, default=0)
    bg_haveexpenses = models.IntegerField(
        db_column='bg_haveExpenses',
        blank=True,
        null=True,
        default=0
    )
    have_etiquetas_fiscales = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )
    # nos indica si el pedido es trackeado por defecto se coloca en SI
    # si es traqueado se lo toma en cuenta para los reportes de movimientos
    bg_is_tracked = models.BooleanField(default=1, blank=True, null=True)
    # indica si el pedido esta definitivamente cerrado para otpimizar
    # la depuracion de pedidos activos
    bg_is_closed_checked = models.BooleanField(
        default=0, blank=True, null=True)
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )
    last_update = models.DateTimeField(blank=True, null=True)
    saldo_mayor = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    history = HistoricalRecords()

    def __str__(self):
        return ''.join([self.nro_pedido])

    class Meta:
        #managed = False
        managed = True
        db_table = 'pedido'
        ordering = ['nro_pedido']
        verbose_name_plural = 'Pedidos'

    @classmethod
    def get_by_order(self, nro_order):
        try:
            order = self.objects.get(pk=nro_order)
        except ObjectDoesNotExist:
            loggin('e', 'El pedido {nro_order} no existe'.format(
                nro_order=nro_order
            ))
            return None

        if order.proveedor == None or order.proveedor == '':
            order.proveedor = 'No Definido'

        if order.nro_refrendo == None or order.nro_refrendo == '':
            order.nro_refrendo = 'Pendiente'

        return order

    @property
    def diferencia_ice_senae(self):
        return 0

    @property
    def reliquidacion_ice(self):
        return (

        )

    @classmethod
    def get_all(self):
        return self.objects.all().exclude(nro_pedido='000-00')

    @classmethod
    def search(self, query):
        pass

    @classmethod
    def get_by_field(self, **args):
        pass

    @classmethod
    def get_arrived_cellar_by_date(self, year, month):
        pass

    @classmethod
    def get_open_orders(self):
        orders = self.objects.filter(bg_isclosed=0).exclude(
            nro_pedido='000-00'
        )
        if orders.count() == 0:
            loggin('e', 'No existen pedidos abiertos')
            return []

        loggin('i', 'Retornando todos los pedidos abiertos')
        return orders

    @classmethod
    def get_paid_taxes(self, nro_order):
        taxes = {
            'total_pagado': 0,
            'total_pagado_sin_iva': 0,
            'total_provisionado': 0,
        }

        order = self.get_by_order(nro_order)

        if order is None or order.regimen == '70' or order.bg_isliquidated == 0 or order.bg_isliquidated is None:
            loggin(
                'w',
                ('No se obtener los tributos del pedido {nro_order} pedido '
                 'inexistente o regimen = 70'.format(
                     nro_order=nro_order
                 )))
            return taxes

        return {
            'total_pagado': (
                order.arancel_advalorem_pagar_pagado
                + order.arancel_especifico_pagar_pagado
                + order.fodinfa_pagado
                + order.ice_advalorem_pagado
                + order.ice_especifico_pagado
            ),
            'total_pagado_sin_iva': (
                order.arancel_advalorem_pagar_pagado
                + order.arancel_especifico_pagar_pagado
                + order.fodinfa_pagado
                + order.ice_advalorem_pagado
                + order.ice_especifico_pagado
            ),
            'total_provisionado': (
                order.arancel_advalorem_pagar_pagado
                + order.arancel_especifico_pagar_pagado
                + order.fodinfa_pagado
                + order.ice_advalorem_pagado
                + order.ice_especifico_pagado
            )
        }
