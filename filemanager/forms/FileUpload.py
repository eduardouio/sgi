from django.forms import ModelForm
from filemanager.models import FileManager

class FileUploadModelForm(ModelForm):
    class Meta:
        model = FileManager
        fields = [
            'modelo','id_registro','archivo','obserbaciones'
        ]