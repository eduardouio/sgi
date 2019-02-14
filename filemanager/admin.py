from django.contrib import admin
from filemanager.models import FileManager

class FileManagerAdmin(admin.ModelAdmin):
    pass


admin.site.register (FileManager, FileManagerAdmin)
