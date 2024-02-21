from django.contrib import admin
from filemanager.models import FileManager


class FileManagerAdmin(admin.ModelAdmin):
    list_display = (
        'modelo',
        'usuario',
        'id_registro',
        'archivo',
        'nombre_fichero',
        'observaciones',
        'date_create',
        'last_update',
        'bg_isvalid',
        'bg_isvisible',
    )

    search_fields = [
        'nombre_fichero',
        'modelo',
        'usuario',
        'id_registro',
    ]


admin.site.register (FileManager, FileManagerAdmin)
