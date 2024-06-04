from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from galeria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
