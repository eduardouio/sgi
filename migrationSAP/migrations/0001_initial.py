# Generated by Django 2.2 on 2021-09-09 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Migrations',
            fields=[
                ('nro_pedido', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('import_status', models.CharField(max_length=10)),
                ('seguro_aduana', models.DecimalField(decimal_places=3, max_digits=10)),
                ('flete_aduana', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pais_origen', models.CharField(max_length=50)),
                ('ciudad_origen', models.CharField(max_length=50)),
                ('moneda', models.CharField(max_length=25)),
                ('tipo_cambio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('proveedor', models.CharField(max_length=150)),
                ('identificacion_proveedor', models.CharField(blank=True, max_length=15, null=True)),
                ('id_factura_proveedor', models.CharField(blank=True, max_length=45, null=True)),
                ('identificacion_proveedor_factura', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_emision_factura', models.DateTimeField(blank=True, null=True)),
                ('fecha_vencimiento_factura', models.DateTimeField(blank=True, null=True)),
                ('valor_factura', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('observaciones_pedido', models.CharField(blank=True, max_length=300, null=True)),
                ('observaciones_proveedor', models.CharField(blank=True, max_length=300, null=True)),
                ('observaciones_factura', models.CharField(blank=True, max_length=300, null=True)),
                ('regimen', models.CharField(blank=True, max_length=2, null=True)),
                ('incoterm', models.CharField(blank=True, max_length=3, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('fecha_importacion', models.DateTimeField(blank=True, null=True)),
                ('bg_have_invoice', models.IntegerField(default=0)),
                ('bg_have_order_items', models.IntegerField(default=0)),
                ('bg_have_supplier', models.IntegerField(default=0)),
                ('bg_have_invoice_items', models.IntegerField(default=0)),
                ('bg_exist_in_local', models.IntegerField(default=0)),
                ('bg_supplier_exist_in_local', models.IntegerField(default=0)),
                ('bg_has_imported', models.IntegerField(default=0)),
                ('bg_log', models.TextField(blank=True, null=True)),
                ('bg_migrated_order', models.IntegerField(default=0)),
                ('bg_migrated_order_detail', models.IntegerField(default=0)),
                ('bg_migrated_order_invoice', models.IntegerField(default=0)),
                ('bg_migrated_order_invoice_detail', models.IntegerField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('gasto_origen', models.DecimalField(blank=True, decimal_places=3, max_digits=11, null=True)),
                ('docentry', models.IntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cabeceras Migraciones SAP',
                'db_table': 'migracion',
                'ordering': ['nro_pedido'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MigrationsDetail',
            fields=[
                ('id_migracion_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cod_contable', models.CharField(max_length=20)),
                ('identificacion_proveedor', models.CharField(max_length=16)),
                ('cod_ice', models.CharField(max_length=39)),
                ('nombre', models.CharField(max_length=70)),
                ('nro_cajas', models.IntegerField(blank=True, null=True)),
                ('capacidad_ml', models.SmallIntegerField()),
                ('cantidad_x_caja', models.SmallIntegerField()),
                ('grado_alcoholico', models.FloatField()),
                ('costo_caja', models.DecimalField(decimal_places=10, max_digits=16)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('bg_product_exist_in_local', models.IntegerField()),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('nro_pedido', models.ForeignKey(db_column='nro_pedido', on_delete=django.db.models.deletion.PROTECT, to='migrationSAP.Migrations')),
            ],
            options={
                'verbose_name_plural': 'Detalle Migraciones SAP',
                'db_table': 'migracion_detalle',
                'ordering': ['nro_pedido', 'id_migracion_detalle'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalMigrationsDetail',
            fields=[
                ('id_migracion_detalle', models.IntegerField(blank=True, db_index=True)),
                ('cod_contable', models.CharField(max_length=20)),
                ('identificacion_proveedor', models.CharField(max_length=16)),
                ('cod_ice', models.CharField(max_length=39)),
                ('nombre', models.CharField(max_length=70)),
                ('nro_cajas', models.IntegerField(blank=True, null=True)),
                ('capacidad_ml', models.SmallIntegerField()),
                ('cantidad_x_caja', models.SmallIntegerField()),
                ('grado_alcoholico', models.FloatField()),
                ('costo_caja', models.DecimalField(decimal_places=10, max_digits=16)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('bg_product_exist_in_local', models.IntegerField()),
                ('id_user', models.SmallIntegerField(default=0)),
                ('date_create', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('nro_pedido', models.ForeignKey(blank=True, db_column='nro_pedido', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='migrationSAP.Migrations')),
            ],
            options={
                'verbose_name': 'historical migrations detail',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMigrations',
            fields=[
                ('nro_pedido', models.CharField(db_index=True, max_length=6)),
                ('import_status', models.CharField(max_length=10)),
                ('seguro_aduana', models.DecimalField(decimal_places=3, max_digits=10)),
                ('flete_aduana', models.DecimalField(decimal_places=3, max_digits=10)),
                ('pais_origen', models.CharField(max_length=50)),
                ('ciudad_origen', models.CharField(max_length=50)),
                ('moneda', models.CharField(max_length=25)),
                ('tipo_cambio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('proveedor', models.CharField(max_length=150)),
                ('identificacion_proveedor', models.CharField(blank=True, max_length=15, null=True)),
                ('id_factura_proveedor', models.CharField(blank=True, max_length=45, null=True)),
                ('identificacion_proveedor_factura', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_emision_factura', models.DateTimeField(blank=True, null=True)),
                ('fecha_vencimiento_factura', models.DateTimeField(blank=True, null=True)),
                ('valor_factura', models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True)),
                ('observaciones_pedido', models.CharField(blank=True, max_length=300, null=True)),
                ('observaciones_proveedor', models.CharField(blank=True, max_length=300, null=True)),
                ('observaciones_factura', models.CharField(blank=True, max_length=300, null=True)),
                ('regimen', models.CharField(blank=True, max_length=2, null=True)),
                ('incoterm', models.CharField(blank=True, max_length=3, null=True)),
                ('id_user', models.SmallIntegerField(default=0)),
                ('fecha_importacion', models.DateTimeField(blank=True, null=True)),
                ('bg_have_invoice', models.IntegerField(default=0)),
                ('bg_have_order_items', models.IntegerField(default=0)),
                ('bg_have_supplier', models.IntegerField(default=0)),
                ('bg_have_invoice_items', models.IntegerField(default=0)),
                ('bg_exist_in_local', models.IntegerField(default=0)),
                ('bg_supplier_exist_in_local', models.IntegerField(default=0)),
                ('bg_has_imported', models.IntegerField(default=0)),
                ('bg_log', models.TextField(blank=True, null=True)),
                ('bg_migrated_order', models.IntegerField(default=0)),
                ('bg_migrated_order_detail', models.IntegerField(default=0)),
                ('bg_migrated_order_invoice', models.IntegerField(default=0)),
                ('bg_migrated_order_invoice_detail', models.IntegerField()),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('gasto_origen', models.DecimalField(blank=True, decimal_places=3, max_digits=11, null=True)),
                ('docentry', models.IntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical migrations',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
