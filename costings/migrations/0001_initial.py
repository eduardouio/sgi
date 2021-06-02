# Generated by Django 2.2 on 2021-05-31 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0004_auto_20210531_1453'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalLedger',
            fields=[
                ('id_mayor', models.IntegerField(blank=True, db_index=True)),
                ('tipo', models.CharField(max_length=50)),
                ('id_parcial', models.PositiveSmallIntegerField(default=0)),
                ('costo_inicial_producto', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('costo_producto', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('descargas', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('saldo_producto', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('precio_entrega', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('mayor_sap', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('provisiones_sap', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('mayor_sgi', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('provisiones_sgi', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('facturas_sgi', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('reliquidacion_ice', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('bg_mayor', models.SmallIntegerField(default=0)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('id_user', models.PositiveIntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('nro_pedido', models.ForeignKey(blank=True, db_column='nro_pedido', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orders.Order')),
            ],
            options={
                'verbose_name': 'historical ledger',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id_mayor', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('id_parcial', models.PositiveSmallIntegerField(default=0)),
                ('costo_inicial_producto', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('costo_producto', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('descargas', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('saldo_producto', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('precio_entrega', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('mayor_sap', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('provisiones_sap', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('mayor_sgi', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('provisiones_sgi', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('facturas_sgi', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('reliquidacion_ice', models.DecimalField(decimal_places=13, default=0, max_digits=20)),
                ('bg_mayor', models.SmallIntegerField(default=0)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('id_user', models.PositiveIntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('nro_pedido', models.ForeignKey(db_column='nro_pedido', on_delete=django.db.models.deletion.PROTECT, to='orders.Order')),
            ],
            options={
                'verbose_name_plural': 'Mayores Liquidaciones',
                'db_table': 'mayor',
                'ordering': ['nro_pedido', 'id_parcial', 'tipo'],
                'managed': True,
                'unique_together': {('nro_pedido', 'id_parcial', 'tipo')},
            },
        ),
    ]
