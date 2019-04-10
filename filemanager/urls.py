from django.urls import include, path
from filemanager.views import UploadFileView, ListFilesTemplateView

app_name = 'filemanager'

urlpatterns = [
    path('', ListFilesTemplateView.as_view(), name="subir-archivo"),
    path('subir/', UploadFileView.as_view(), name="subir-archivo"),
]
