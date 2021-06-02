# Generated by Django 2.2 on 2021-05-31 22:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210531_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalorder',
            name='date_create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
