from . import models
from django.shortcuts import render
from .models import Musico, Banda, GeneroMusical

def pagina_principal(request):
    musicos = Musico.objects.all()
    bandas = Banda.objects.all()
    generos = GeneroMusical.objects.all()
    return render(request, 'integrantes/pagina_principal.html', {'musicos': musicos, 'bandas': bandas, 'generos': generos})

def lista_musicos(request):
    musicos = Musico.objects.all()
    return render(request, 'integrantes/lista_musicos.html', {'musicos': musicos})

def lista_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'integrantes/lista_bandas.html', {'bandas': bandas})

def lista_generos(request):
    generos = GeneroMusical.objects.all()
    return render(request, 'integrantes/lista_generos.html', {'generos': generos})

