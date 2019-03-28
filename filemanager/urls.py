from django.urls import include, path
from filemanager.views import UploadFileView

app_name = 'filemanager'

urlpatterns = [
    path('subir/', UploadFileView.as_view(), name="subir-archivo")
]
