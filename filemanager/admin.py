from django.contrib import admin
from filemanager.models import FileManager

class FileManagerAdmin(admin.ModelAdmin):
    list_display = (
        'modelo',
        'usuario',
        'id_registro',
        'archivo',
        'nombre_fichero',
        'obserbaciones',
        'date_create',
        'last_update',
        'bg_isvalid',
        'bg_isvisible',
    )


admin.site.register (FileManager, FileManagerAdmin)
