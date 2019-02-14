from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import include, path

admin.site.site_title = 'SGI'
admin.site.site_header = 'Agencia Y Representaciones Cordovez S.A.'
#admin.site.site_header = 'IMNAC Importadora Nacional Cia. Ltda.'
#admin.site.site_header = 'VID Internacional S.A.'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='autehtications')),
    path('costos/', include('costings.urls', namespace='costings')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('api/', include('api.urls', namespace='api_urls')),
    path('importaciones/', include('importations.urls', namespace='importaciones_urls')),
    path('productos/', include('products.urls', namespace='productos_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
