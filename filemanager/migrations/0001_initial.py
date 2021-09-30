# Generated by Django 2.2 on 2021-09-09 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFileManager',
            fields=[
                ('id_archivo', models.IntegerField(blank=True, db_index=True)),
                ('id_registro', models.CharField(max_length=10)),
                ('archivo', models.TextField(max_length=100)),
                ('nombre_fichero', models.CharField(max_length=125)),
                ('observaciones', models.TextField(blank=True, default=None, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('bg_isvalid', models.BooleanField(default=True)),
                ('bg_isvisible', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modelo', models.ForeignKey(blank=True, db_column='model', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='contenttypes.ContentType')),
                ('usuario', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical file manager',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='FileManager',
            fields=[
                ('id_archivo', models.AutoField(primary_key=True, serialize=False)),
                ('id_registro', models.CharField(max_length=10)),
                ('archivo', models.FileField(upload_to='archivos/')),
                ('nombre_fichero', models.CharField(max_length=125)),
                ('observaciones', models.TextField(blank=True, default=None, null=True)),
                ('date_create', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('bg_isvalid', models.BooleanField(default=True)),
                ('bg_isvisible', models.BooleanField(default=True)),
                ('modelo', models.ForeignKey(db_column='model', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Gestion de Archivos',
                'db_table': 'gestor_archivos',
            },
        ),
    ]
