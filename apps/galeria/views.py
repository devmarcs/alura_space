from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')


    fotografias = Fotografia.objects.order_by("-date_fotography").filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if  not request.user.is_authenticated:
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-date_fotography").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET["buscar"]
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/busca.html', {'cards': fotografias})


def nova_imagem(request):
    return render(request, 'galeria/nova_imagem.html')


def editar_imagem(request):
    return render(request, 'galeria/editar_imagem.html')


def deletar_imagem(request):
    return render(request, 'galeria/deletar_imagem.html')   