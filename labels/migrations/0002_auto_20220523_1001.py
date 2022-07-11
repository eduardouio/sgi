# Generated by Django 2.1.3 on 2022-05-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallabel',
            name='last_jwt',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='label',
            name='last_jwt',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='historicallabel',
            name='end_range',
            field=models.CharField(max_length=15, verbose_name='Rango Final'),
        ),
        migrations.AlterField(
            model_name='historicallabel',
            name='initial_range',
            field=models.CharField(max_length=15, verbose_name='Rango Inicial'),
        ),
        migrations.AlterField(
            model_name='label',
            name='end_range',
            field=models.CharField(max_length=15, verbose_name='Rango Final'),
        ),
        migrations.AlterField(
            model_name='label',
            name='initial_range',
            field=models.CharField(max_length=15, verbose_name='Rango Inicial'),
        ),
    ]
