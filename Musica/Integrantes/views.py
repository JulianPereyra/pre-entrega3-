from . import models
from django.shortcuts import render, redirect
from .models import Musico, Banda, GeneroMusical
from .forms import MusicoForm

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

def eliminar_musico(request, musico_id):
    Musico.objects.filter(pk=musico_id).delete()
    return redirect('Integrantes:lista_musicos')

def agregar_musico(request):
    if request.method == 'POST':
        form = MusicoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Integrantes:lista_musicos')
    else:
        form = MusicoForm()
    return render(request, 'integrantes/agregar_musico.html', {'form': form})     


