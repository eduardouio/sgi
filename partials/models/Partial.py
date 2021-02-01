from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin
from orders.models.Order import Order


class Partial(models.Model):
    id_parcial = models.AutoField(primary_key=True)
    nro_pedido = models.ForeignKey(
        Order,
        models.PROTECT,
        db_column='nro_pedido'
    )
    fecha_nacionalizacion = models.DateField(blank=True, null=True)
    fecha_declaracion_inicial = models.DateField(blank=True, null=True)
    fecha_entrega_etiquetas_senae = models.DateField(blank=True, null=True)
    fecha_pegado_etiquetas = models.DateField(blank=True, null=True)
    fecha_solicitud_salida_almagro = models.DateField(blank=True, null=True)
    fecha_aforo = models.DateField(blank=True, null=True)
    fecha_llegada_documentos = models.DateField(blank=True, null=True)
    fecha_envio_de_documentos = models.DateField(blank=True, null=True)
    fecha_envio_documentos = models.DateField(blank=True, null=True)
    fecha_aprovacion_dai = models.DateField(blank=True, null=True)
    fecha_salida_almacenera = models.DateField(blank=True, null=True)
    fecha_liquidacion = models.DateField(blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    fecha_llegada_cliente = models.DateField(blank=True, null=True)
    fecha_salida_autorizada_almagro = models.DateTimeField(
        blank=True,
        null=True
    )
    proximo_almacenaje_desde = models.DateField(blank=True, null=True)
    otros = models.DecimalField(
        max_digits=8,
        decimal_places=3,
        blank=True,
        default=0
    )
    observaciones = models.CharField(max_length=250, blank=True, null=True)
    tipo_cambio = models.DecimalField(
        max_digits=15,
        decimal_places=10,
        default=1
    )
    nro_refrendo = models.CharField(max_length=22, blank=True, null=True)
    exoneracion_arancel = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0
    )
    fodinfa = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    fodinfa_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    ice_advalorem = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    ice_advalorem_reliquidado = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=0
    )
    ice_advalorem_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    ice_especifico = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    ice_especifico_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    iva = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    iva_pagado = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        default=0
    )
    arancel_advalorem_pagar = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    arancel_advalorem_pagar_pagado = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    arancel_especifico_pagar_pagado = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    arancel_especifico_pagar = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_arancel_advalorem = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_arancel_especifico = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_ice_especifico = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_ice_advalorem = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    porcentaje_ice_advalorem = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_iva = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_fodinfa = models.DecimalField(
        max_digits=16,
        decimal_places=3,
        blank=True,
        default=0
    )
    base_etiquetas = models.DecimalField(
        max_digits=16,
        decimal_places=8,
        blank=True,
        default=0
    )
    nro_liquidacion = models.CharField(max_length=22, blank=True, null=True)
    notas_cierre = models.CharField(max_length=200, blank=True, null=True)
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
    agente_aduana = models.CharField(max_length=100, blank=True, null=True)
    ruc_agente_aduana = models.CharField(max_length=13, blank=True, null=True)
    etiquetas_pegadas = models.IntegerField(blank=True, null=True)
    punto_lledada = models.CharField(max_length=60, blank=True, null=True)
    liquidacion_con_tasa = models.IntegerField(blank=True, null=True)
    bg_isclosed = models.IntegerField(blank=True, null=True, default=0)
    bg_have_etiquetas_fiscales = models.IntegerField(
        default=0,
        blank=True,
        null=True
    )
    bg_isliquidated = models.IntegerField(blank=True, null=True)
    bg_have_tasa_control = models.IntegerField(blank=True, null=True)
    id_user_cierre = models.PositiveSmallIntegerField(blank=True, null=True)
    saldo_mayor = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True
    )
    id_user = models.SmallIntegerField(default=0)
    date_create = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now
    )
    last_update = models.DateTimeField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.id_parcial)

    class Meta:
        managed = True
        db_table = 'parcial'
        verbose_name_plural = 'Parciales'
        ordering = ['id_parcial']

    @property
    def ordinal_parcial(self):
        return self.get_ordinal_number(self.id_parcial)

    @property
    def partial_url(self):
        return ''.join(
            [
                self.nro_pedido_id,
                '/',
                str(self.ordinal_parcial),
                '/'
            ]
        )

    @classmethod
    def get_by_order(self, nro_order):
        parcials = self.objects.filter(nro_pedido=nro_order).order_by(
            'id_parcial'
        )
        if parcials.count() == 0:
            loggin('w', 'No existe informacion para el parcial indicado')
            return self.objects.none()

        return parcials

    @classmethod
    def get_by_id(self, id_partial):
        try:
            partial = self.objects.get(pk=id_partial)
        except ObjectDoesNotExist:
            loggin('w', 'El Parcial {} no existe'.format(id_partial))
            return None

        return partial

    @classmethod
    def get_last_partial(self, nro_order):
        partials = self.get_by_order(nro_order)

        if partials is None:
            return None

        return partials.last()

    @classmethod
    def get_last_close_partial(self, nro_order, id_partial=None):
        '''Retorna el ultimo parcial liquidado, si el pedido es R10 o no
        tiene parciales retorna None

        Arguments:
            nro_order {string} -- Pedido del que se quiere obtener

        Keyword Arguments:
            id_partial {int} -- opcional, retorta el parcial anterior liquidado
                                si no retorna el ultimo del pedido
                                (default: {None})

        Returns:
            {QuerySet} | {None}
        '''
        partials = None

        if id_partial:
            partials = self.objects.filter(
                nro_pedido=nro_order,
                bg_isclosed=1,
                id_parcial__lte=id_partial
            )
        else:
            partials = self.objects.filter(nro_pedido=nro_order, bg_isclosed=1)

        if partials.count() == 0:
            loggin('i', 'El pedido {}, no tiene parciales cerrados'.format(
                nro_order
        ))
            return None

        return partials.last()

    @classmethod
    def get_ordinal_number(self, id_partial):
        ''' Ordinal from parcial '''
        current_partial = self.get_by_id(id_partial)
        if current_partial is None:
            return 0

        all_partials = self.get_by_order(current_partial.nro_pedido)
        ordinal = 1
        for p in all_partials:
            if p.id_parcial == current_partial.id_parcial:
                return ordinal
            ordinal += 1

    @classmethod
    def get_order_by_parcial(self, id_parcial):
        try:
            parcial = self.objects.get(pk = id_parcial)
        except:
            loggin('e', 'El parcial no existe {}'.format(id_parcial))
            return None

        if parcial is None:
            loggin(
                'w',
                ('No se puede recupear la order de un parcial '
                    'que no existe {}').format(id_parcial)
            )
            return None

        return Order.get_by_order(parcial.nro_pedido_id)

    @classmethod
    def get_paid_taxes(self, id_partial):
        taxes = {
            'total_pagado': 0,
            'total_pagado_sin_iva': 0,
            'total_provisionado': 0
            }

        partial = self.get_by_id(id_partial)
        if partial is None or partial.bg_isliquidated == 0:
            loggin(
                'i',
                ('No se puede reotornar impuestos si el parcial'
                    ' {} no existe').format(id_partial)
            )
            return taxes

        return {
            'total_pagado': (
                    partial.arancel_advalorem_pagar_pagado
                    + partial.arancel_especifico_pagar_pagado
                    + partial.fodinfa_pagado
                    + partial.ice_advalorem_pagado
                    + partial.ice_especifico_pagado
            ),
            'total_pagado_sin_iva': (
                    partial.arancel_advalorem_pagar_pagado
                    + partial.arancel_especifico_pagar_pagado
                    + partial.fodinfa_pagado
                    + partial.ice_advalorem_pagado
                    + partial.ice_especifico_pagado
            ),
            'total_provisionado': (
                    partial.arancel_advalorem_pagar_pagado
                    + partial.arancel_especifico_pagar_pagado
                    + partial.fodinfa_pagado
                    + partial.ice_advalorem_pagado
                    + partial.ice_especifico_pagado
            )
        }
