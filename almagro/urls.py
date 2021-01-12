from django.urls import include, path

app_name='importations'

urlpatterns = [
     path('subir/', FileUploadFormView.as_view(), name="upload-liquidation"),
    path('asistente/', AssistantTemplateView.as_view(), name="asistente-correos"),
]
