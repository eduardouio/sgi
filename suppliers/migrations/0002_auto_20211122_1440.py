# Generated by Django 2.2 on 2021-11-22 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'managed': False, 'ordering': ['tipo_provedor', 'nombre'], 'verbose_name_plural': 'Proveedores'},
        ),
    ]