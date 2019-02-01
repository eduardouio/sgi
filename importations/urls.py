from django.urls import include, path
from importations.views.UploadFiles import FileUploadFormView

app_name='importations'

urlpatterns = [
     path('subir-liquidacion/', FileUploadFormView.as_view(), name="upload-liquidation")
]
