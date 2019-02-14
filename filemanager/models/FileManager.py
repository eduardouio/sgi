from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class FileManager(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    modelo = models.ForeignKey(ContentType, db_column='model', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    id_registro = models.CharField(max_length=10)
    archivo = models.FileField(upload_to='archivos/')
    nombre_fichero = models.CharField(max_length=125)
    obserbaciones = models.TextField(blank=True,null=True, default=None)
    date_create = models.DateTimeField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre_fichero 

    class Meta:
        db_table = 'gestor_archivos'
        verbose_name_plural = 'Gestion de Archivos'