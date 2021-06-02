# Generated by Django 2.2 on 2021-05-31 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('cod_contable', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('id_producto', models.PositiveIntegerField(unique=True)),
                ('nro_registro_sanitario', models.CharField(default=None, max_length=25)),
                ('fecha_emision_registro', models.DateField(blank=True, default=None, null=True)),
                ('fecha_vencimiento_registro', models.DateField(blank=True, default=None, null=True)),
                ('estado_registro', models.CharField(choices=[('Activo', 'Activo'), ('Cancelado', 'Cancelado'), ('Vencido', 'Vencido'), ('No Renovar', 'No Renovar')], default='Activo', max_length=70, null=True)),
                ('grado_alcoholico', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('nombre', models.CharField(max_length=70, unique=True)),
                ('nombre_extrangero', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('partida_arancelaria', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('subpartida_arancelaria', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('tnan_codigo', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('cod_ice', models.CharField(default='SIN CODIDO ICE', max_length=39)),
                ('capacidad_ml', models.SmallIntegerField(default=1)),
                ('cantidad_x_caja', models.SmallIntegerField(default=1)),
                ('costo_caja', models.DecimalField(decimal_places=10, default=0.0, max_digits=16)),
                ('estado', models.IntegerField(choices=[(1, 'ACTIVO'), (0, 'INACTIVO')], default=1)),
                ('custodia_doble', models.IntegerField(choices=[(1, '1 CUSTODIA'), (2, '2 CUSTODIAS')], default=0)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True)),
                ('pais_origen', models.CharField(blank=True, max_length=70, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('registro_sanitario', models.FileField(blank=True, default=None, null=True, upload_to='registro_sanitario/')),
                ('id_user', models.SmallIntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('identificacion_proveedor', models.ForeignKey(db_column='identificacion_proveedor', on_delete=django.db.models.deletion.PROTECT, to='suppliers.Supplier')),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
                'ordering': ['identificacion_proveedor', 'nombre'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalProduct',
            fields=[
                ('cod_contable', models.CharField(db_index=True, max_length=20)),
                ('id_producto', models.PositiveIntegerField(db_index=True)),
                ('nro_registro_sanitario', models.CharField(default=None, max_length=25)),
                ('fecha_emision_registro', models.DateField(blank=True, default=None, null=True)),
                ('fecha_vencimiento_registro', models.DateField(blank=True, default=None, null=True)),
                ('estado_registro', models.CharField(choices=[('Activo', 'Activo'), ('Cancelado', 'Cancelado'), ('Vencido', 'Vencido'), ('No Renovar', 'No Renovar')], default='Activo', max_length=70, null=True)),
                ('grado_alcoholico', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('nombre', models.CharField(db_index=True, max_length=70)),
                ('nombre_extrangero', models.CharField(blank=True, default=None, max_length=120, null=True)),
                ('partida_arancelaria', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('subpartida_arancelaria', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('tnan_codigo', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('cod_ice', models.CharField(default='SIN CODIDO ICE', max_length=39)),
                ('capacidad_ml', models.SmallIntegerField(default=1)),
                ('cantidad_x_caja', models.SmallIntegerField(default=1)),
                ('costo_caja', models.DecimalField(decimal_places=10, default=0.0, max_digits=16)),
                ('estado', models.IntegerField(choices=[(1, 'ACTIVO'), (0, 'INACTIVO')], default=1)),
                ('custodia_doble', models.IntegerField(choices=[(1, '1 CUSTODIA'), (2, '2 CUSTODIAS')], default=0)),
                ('peso', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=10, null=True)),
                ('pais_origen', models.CharField(blank=True, max_length=70, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('registro_sanitario', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('id_user', models.SmallIntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('identificacion_proveedor', models.ForeignKey(blank=True, db_column='identificacion_proveedor', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='suppliers.Supplier')),
            ],
            options={
                'verbose_name': 'historical product',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
