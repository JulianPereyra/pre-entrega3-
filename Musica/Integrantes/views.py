from . import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Musico, Banda, GeneroMusical
from .forms import MusicoForm,SolicitudUnirseBandaForm,BandaForm
from django.contrib.auth.decorators import login_required
from .models import SolicitudUnirseBanda
from django.views.decorators.csrf import csrf_protect

@login_required
def pagina_principal(request):
    musicos = Musico.objects.all()
    bandas = Banda.objects.all()
    return render(request, 'integrantes/pagina_principal.html', {
        'musicos': musicos,
        'bandas': bandas
    })
    
    
@login_required
def lista_musicos(request):
    musicos = Musico.objects.all()
    return render(request, 'integrantes/lista_musicos.html', {'musicos': musicos})


@login_required
@csrf_protect
def lista_bandas(request):
    bandas = Banda.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        generos = request.POST.get('generos')
        instrumentos_buscados = request.POST.get('instrumentos_buscados')
        Banda.objects.create(nombre=nombre, generos=generos, instrumentos_buscados=instrumentos_buscados)
        return redirect('Integrantes:lista_bandas')
    return render(request, 'integrantes/lista_bandas.html', {'bandas': bandas})

@csrf_protect
def eliminar_banda(request, id):
    banda = get_object_or_404(Banda, id=id)
    if request.method == 'POST':
        banda.delete()
        return redirect('Integrantes:lista_bandas')
    return render(request, 'integrantes/lista_bandas.html')

@csrf_protect
def agregar_banda(request):
    if request.method == 'POST':
        form = BandaForm(request.POST)
        if form.is_valid():
            banda = form.save(commit=False)
            banda.save()
            return redirect('Integrantes:lista_bandas')
    else:
        form = BandaForm()

    return render(request, 'integrantes/agregar_banda.html', {'form': form})

@login_required
def lista_generos(request):
    generos = GeneroMusical.objects.all()
    return render(request, 'integrantes/lista_generos.html', {'generos': generos})

@login_required
def eliminar_musico(request, musico_id):
    Musico.objects.filter(pk=musico_id).delete()
    return redirect('Integrantes:lista_musicos')

@login_required
def agregar_musico(request):
    if request.method == 'POST':
        form = MusicoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Integrantes:lista_musicos')
    else:
        form = MusicoForm()
    return render(request, 'integrantes/agregar_musico.html', {'form': form})     

@login_required
def solicitud_unirse_banda(request):
    if request.method == 'POST':
        form = SolicitudUnirseBandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Integrantes:pagina_principal')
    else:
        form = SolicitudUnirseBandaForm()
    return render(request, 'integrantes/solicitud_unirse_banda.html', {'form': form})

@login_required
def detalles_musico(request, id):
    musico = get_object_or_404(Musico, id=id)
    return render(request, 'integrantes/detalles_musico.html', {'musico': musico})

@login_required
def detalles_banda(request, id):
    banda = get_object_or_404(Banda, id=id)
    return render(request, 'integrantes/detalles_banda.html', {'banda': banda})

@login_required
def buscar(request):
    query = request.GET.get('q')
    resultados_musicos = Musico.objects.filter(nombre__icontains=query)
    resultados_bandas = Banda.objects.filter(nombre__icontains=query)
    return render(request, 'integrantes/resultados_busqueda.html', {
        'resultados_musicos': resultados_musicos,
        'resultados_bandas': resultados_bandas,
        'query': query,
    })

