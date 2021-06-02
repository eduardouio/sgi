# Generated by Django 2.2 on 2021-05-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RightsSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('module_costs_rights', 'Permisos globales para costos'), ('module_importations_rights', 'Permisos globales para importaciones'), ('module_filemanager_rights', 'Permisos globales para archivos'), ('module_migrationSap_rights', 'Permisos globales para migraciones SAP'), ('module_orders_rights', 'Permisos globales para Pedidos'), ('module_paids_rights', 'Permisos globales para Pagos'), ('module_partials_rights', 'Permisos globales para Parciales'), ('module_products_rights', 'Permisos globales para productos'), ('module_suppliers_rights', 'Permisos globales para proveedores'), ('module_warenhouse_rights', 'Permisos globales para Bodega')),
                'managed': False,
            },
        ),
    ]
