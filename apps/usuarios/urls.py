from django.urls import path, include
from apps.usuarios.views import login, cadastro, logout

urlpatterns = [
    path("", login, name="login"),
    path("cadastro", cadastro, name="cadastro"),
    path("logout", logout, name="logout"),
]