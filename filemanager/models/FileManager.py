from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils import timezone
from simple_history.models import HistoricalRecords

from logs.app_log import loggin


class FileManager(models.Model):
    id_archivo = models.AutoField(primary_key=True)
    modelo = models.ForeignKey(ContentType, db_column='model', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_registro = models.CharField(max_length=10)
    archivo = models.FileField(upload_to='archivos/')
    nombre_fichero = models.CharField(max_length=125)
    observaciones = models.TextField(blank=True, null=True, default=None)
    date_create = models.DateTimeField(blank=True, null=True, default=timezone.now)
    last_update = models.DateTimeField(blank=True, null=True)
    bg_isvalid = models.BooleanField(default=True)
    bg_isvisible = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre_fichero 

    class Meta:
        db_table = 'gestor_archivos'
        verbose_name_plural = 'Gestion de Archivos'


    @classmethod
    def get_by_model_id(self,app_label, model_name, id_row):
        '''
            Obtiene los archivos relacionados con un modelo y un id
        '''
        model = ContentType.objects.get(app_label=app_label, model=model_name)
        results = self.objects.filter(modelo=model.pk, id_registro=str(id_row))

        if results.count():
            loggin('i', 'Recuperando archivos de modelo {} con id {}'.format(
                model_name, str(id)
            ))
            return results
        
        loggin(
            'w', 
            'El modelo {} con el id {} no tiene archivos'.
            format(model_name, id)
        )
        return []


# Se envia a eliminar el archivo cuando se elimine el registro
@receiver(post_delete, sender=FileManager)
def submission_delete(sender, instance, **kwargs):
    instance.archivo.delete(False)
