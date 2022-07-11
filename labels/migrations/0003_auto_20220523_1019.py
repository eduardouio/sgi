# Generated by Django 2.1.3 on 2022-05-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_auto_20220523_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallabel',
            name='end_range',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Rango Final'),
        ),
        migrations.AlterField(
            model_name='historicallabel',
            name='initial_range',
            field=models.CharField(db_index=True, max_length=15, verbose_name='Rango Inicial'),
        ),
        migrations.AlterField(
            model_name='label',
            name='end_range',
            field=models.CharField(max_length=15, unique=True, verbose_name='Rango Final'),
        ),
        migrations.AlterField(
            model_name='label',
            name='initial_range',
            field=models.CharField(max_length=15, unique=True, verbose_name='Rango Inicial'),
        ),
    ]
