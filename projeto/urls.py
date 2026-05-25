from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.perfil.urls')),
    path('api/', include('apps.barbearia.urls')),
]
