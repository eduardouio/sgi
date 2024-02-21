# Generated by Django 2.2 on 2021-09-09 22:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suppliers', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id_gastos_nacionalizacion', models.AutoField(primary_key=True, serialize=False)),
                ('id_parcial', models.PositiveSmallIntegerField(default=0)),
                ('concepto', models.CharField(max_length=45)),
                ('tipo', models.CharField(blank=True, max_length=15, null=True)),
                ('valor_provisionado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valor_ajuste', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fecha', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('bg_closed', models.IntegerField(default=0)),
                ('bg_is_visible_gi', models.IntegerField(default=1)),
                ('bg_iscontabilizado', models.IntegerField(default=0)),
                ('bg_iscontabilizado_por', models.IntegerField(blank=True, default=0, null=True)),
                ('bg_isdrop', models.BooleanField(blank=True, default=False, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('identificacion_proveedor', models.ForeignKey(db_column='identificacion_proveedor', on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier')),
                ('nro_pedido', models.ForeignKey(db_column='nro_pedido', on_delete=django.db.models.deletion.PROTECT, to='orders.Order')),
            ],
            options={
                'verbose_name_plural': 'Gastos Nacionalizacion',
                'db_table': 'gastos_nacionalizacion',
                'ordering': ['concepto', 'nro_pedido', 'id_parcial', 'tipo'],
                'managed': True,
                'unique_together': {('nro_pedido', 'id_parcial', 'concepto')},
            },
        ),
        migrations.CreateModel(
            name='PaidInvoice',
            fields=[
                ('id_documento_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nro_factura', models.CharField(max_length=20)),
                ('fecha_emision', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('saldo', models.DecimalField(decimal_places=13, max_digits=20)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('comentarios_audit', models.TextField(blank=True, null=True)),
                ('bg_closed', models.IntegerField(default=0)),
                ('bg_audit', models.IntegerField(default=0)),
                ('bg_isrejected', models.IntegerField(default=0)),
                ('audit_date', models.DateTimeField(blank=True, null=True)),
                ('audit_user', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('tipo', models.CharField(max_length=8)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('identificacion_proveedor', models.ForeignKey(db_column='identificacion_proveedor', on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier')),
            ],
            options={
                'verbose_name_plural': 'Facturas Servicios',
                'db_table': 'documento_pago',
                'ordering': ['-id_documento_pago'],
                'managed': True,
                'unique_together': {('identificacion_proveedor', 'nro_factura')},
            },
        ),
        migrations.CreateModel(
            name='RateIncoterm',
            fields=[
                ('id_incoterm', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=12)),
                ('pais', models.CharField(max_length=45)),
                ('incoterms', models.CharField(max_length=4)),
                ('ciudad', models.CharField(max_length=45)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tarias Incoterms',
                'db_table': 'tarifa_incoterm',
                'ordering': ['tipo', 'pais', 'ciudad', 'incoterms'],
                'managed': True,
                'unique_together': {('pais', 'ciudad', 'incoterms', 'tipo')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalRateIncoterm',
            fields=[
                ('id_incoterm', models.IntegerField(blank=True, db_index=True)),
                ('tipo', models.CharField(max_length=12)),
                ('pais', models.CharField(max_length=45)),
                ('incoterms', models.CharField(max_length=4)),
                ('ciudad', models.CharField(max_length=45)),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=8)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical rate incoterm',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalRateExpense',
            fields=[
                ('id_tarifa_gastos', models.IntegerField(blank=True, db_index=True)),
                ('regimen', models.CharField(max_length=5)),
                ('tipo_gasto', models.CharField(max_length=21)),
                ('concepto', models.CharField(max_length=120)),
                ('valor', models.DecimalField(decimal_places=4, max_digits=8)),
                ('estado', models.IntegerField(default=1)),
                ('pais_origen', models.CharField(max_length=45)),
                ('porcentaje', models.DecimalField(decimal_places=4, max_digits=7)),
                ('comentarios', models.CharField(blank=True, max_length=550, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('identificacion_proveedor', models.ForeignKey(blank=True, db_column='identificacion_proveedor', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='suppliers.Supplier')),
            ],
            options={
                'verbose_name': 'historical rate expense',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPaidInvoiceDetail',
            fields=[
                ('id_detalle_documento_pago', models.IntegerField(blank=True, db_index=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valor_ajuste', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('bg_closed', models.IntegerField(default=0)),
                ('bg_isnotprovisioned', models.IntegerField(default=0)),
                ('bg_mayor', models.SmallIntegerField(default=0)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('id_documento_pago', models.ForeignKey(blank=True, db_column='id_documento_pago', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='paids.PaidInvoice')),
                ('id_gastos_nacionalizacion', models.ForeignKey(blank=True, db_column='id_gastos_nacionalizacion', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='paids.Expense')),
            ],
            options={
                'verbose_name': 'historical paid invoice detail',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPaidInvoice',
            fields=[
                ('id_documento_pago', models.IntegerField(blank=True, db_index=True)),
                ('nro_factura', models.CharField(max_length=20)),
                ('fecha_emision', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('saldo', models.DecimalField(decimal_places=13, max_digits=20)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('comentarios_audit', models.TextField(blank=True, null=True)),
                ('bg_closed', models.IntegerField(default=0)),
                ('bg_audit', models.IntegerField(default=0)),
                ('bg_isrejected', models.IntegerField(default=0)),
                ('audit_date', models.DateTimeField(blank=True, null=True)),
                ('audit_user', models.SmallIntegerField(blank=True, default=0, null=True)),
                ('tipo', models.CharField(max_length=8)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('identificacion_proveedor', models.ForeignKey(blank=True, db_column='identificacion_proveedor', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='suppliers.Supplier')),
            ],
            options={
                'verbose_name': 'historical paid invoice',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalExpense',
            fields=[
                ('id_gastos_nacionalizacion', models.IntegerField(blank=True, db_index=True)),
                ('id_parcial', models.PositiveSmallIntegerField(default=0)),
                ('concepto', models.CharField(max_length=45)),
                ('tipo', models.CharField(blank=True, max_length=15, null=True)),
                ('valor_provisionado', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valor_ajuste', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('fecha', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('bg_closed', models.IntegerField(default=0)),
                ('bg_is_visible_gi', models.IntegerField(default=1)),
                ('bg_iscontabilizado', models.IntegerField(default=0)),
                ('bg_iscontabilizado_por', models.IntegerField(blank=True, default=0, null=True)),
                ('bg_isdrop', models.BooleanField(blank=True, default=False, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('identificacion_proveedor', models.ForeignKey(blank=True, db_column='identificacion_proveedor', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='suppliers.Supplier')),
                ('nro_pedido', models.ForeignKey(blank=True, db_column='nro_pedido', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.Order')),
            ],
            options={
                'verbose_name': 'historical expense',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='RateExpense',
            fields=[
                ('id_tarifa_gastos', models.AutoField(primary_key=True, serialize=False)),
                ('regimen', models.CharField(max_length=5)),
                ('tipo_gasto', models.CharField(max_length=21)),
                ('concepto', models.CharField(max_length=120)),
                ('valor', models.DecimalField(decimal_places=4, max_digits=8)),
                ('estado', models.IntegerField(default=1)),
                ('pais_origen', models.CharField(max_length=45)),
                ('porcentaje', models.DecimalField(decimal_places=4, max_digits=7)),
                ('comentarios', models.CharField(blank=True, max_length=550, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('identificacion_proveedor', models.ForeignKey(db_column='identificacion_proveedor', on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier')),
            ],
            options={
                'verbose_name_plural': 'Tarias Gastos',
                'db_table': 'tarifa_gastos',
                'ordering': ['identificacion_proveedor', 'regimen', 'concepto', 'valor'],
                'managed': True,
                'unique_together': {('identificacion_proveedor', 'concepto', 'pais_origen', 'valor', 'tipo_gasto')},
            },
        ),
        migrations.CreateModel(
            name='PaidInvoiceDetail',
            fields=[
                ('id_detalle_documento_pago', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('valor_ajuste', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('bg_closed', models.IntegerField(default=0)),
                ('bg_isnotprovisioned', models.IntegerField(default=0)),
                ('bg_mayor', models.SmallIntegerField(default=0)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('id_documento_pago', models.ForeignKey(db_column='id_documento_pago', on_delete=django.db.models.deletion.PROTECT, to='paids.PaidInvoice')),
                ('id_gastos_nacionalizacion', models.ForeignKey(db_column='id_gastos_nacionalizacion', on_delete=django.db.models.deletion.PROTECT, to='paids.Expense')),
            ],
            options={
                'verbose_name_plural': 'Detalle Documento Pago',
                'db_table': 'detalle_documento_pago',
                'managed': True,
                'unique_together': {('id_documento_pago', 'id_gastos_nacionalizacion')},
            },
        ),
    ]