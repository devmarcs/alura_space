from django.urls import path
from apps.galeria.views import index, imagem, buscar

urlpatterns = [
    path('home/', index, name='home'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="busca"),
]