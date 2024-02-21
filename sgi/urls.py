from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import include, path

admin.site.site_title = 'SGI'
admin.site.site_header = settings.EMPRESA['nombre']

handler404 = 'authentication.views.errors.error_404'
handler500 = 'authentication.views.errors.error_500'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='autehtications')),
    path('costos/', include('costings.urls', namespace='costings')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('api/', include('api.urls', namespace='api_urls')),
    path('importaciones/', include('importations.urls', namespace='importaciones_urls')),
    path('productos/', include('products.urls', namespace='productos_urls')),
    path('archivos/', include('filemanager.urls', namespace='filemanager_urls')),
    path('auditoria/', include('audit.urls', namespace='audit_urls')),
    path('reportes/', include('reports.urls', namespace='reports_urls')),
    path('almagro/', include('almagro.urls', namespace='almagro_urls')),
    path('sap/', include('migrationSAP.urls', namespace='sap_urls')),
    path('etiquetas/', include('labels.urls', namespace='labels_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

