from django.urls import include, path

from filemanager.views import UploadFileFormView

app_name = 'filemanager'

urlpatterns = [
    path('facinfo/<id_partial>/', UploadFileFormView.as_view(), name="Subir Factura Informativa")
]
