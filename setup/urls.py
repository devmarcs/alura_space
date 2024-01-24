from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    #path('imagem/', include('galeria.urls')) #Verificar essa linha de código
]
