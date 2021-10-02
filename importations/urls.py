from django.urls import include, path

from importations.views import (AssistantTemplateView, FileUploadFormView,
                                UpdateProcesTV)

app_name='importations'

urlpatterns = [
    path('subir/', FileUploadFormView.as_view(), name="upload-liquidation"),
    path('asistente/', AssistantTemplateView.as_view(), name="asistente-correos"),
    path('actualizar-procesos/', UpdateProcesTV.as_view(), name="actualizar-procesos"),
]
