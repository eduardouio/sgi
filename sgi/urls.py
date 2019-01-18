from django.contrib import admin
from django.urls import path, include

admin.site.site_title = 'SGI'
admin.site.site_header = 'Agencia Y Representaciones Cordovez S.A.'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='autehtications')),
    path('costos/', include('costings.urls', namespace='costings')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('api/', include('api.urls', namespace='api_urls')),
]