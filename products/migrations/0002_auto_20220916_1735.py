# Generated by Django 2.2 on 2022-09-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='solicitud_aucp',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='solicitud_aucp',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
