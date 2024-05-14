from django.urls import path
from . import views

app_name = "Integrantes"

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('musicos/', views.lista_musicos, name='lista_musicos'),
    path('bandas/', views.lista_bandas, name='lista_bandas'),
    path('generos/', views.lista_generos, name='lista_generos'),
    # 
]