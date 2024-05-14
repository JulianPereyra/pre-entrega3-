from django.shortcuts import render

from . import models

def index(request):
    consulta = models.Musico.objects.all
    contexto = {"Musicos": consulta}
    return render(request, "Integrantes/index.html", contexto)
