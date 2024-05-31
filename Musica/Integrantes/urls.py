from django.urls import path
from . import views

app_name = "Integrantes"

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('musicos/', views.lista_musicos, name='lista_musicos'),
    path('bandas/', views.lista_bandas, name='lista_bandas'),
    path('generos/', views.lista_generos, name='lista_generos'),
    path('eliminar_musico/<int:musico_id>/', views.eliminar_musico, name='eliminar_musico'),
    path('agregar_musico/', views.agregar_musico, name='agregar_musico'),
    path('solicitud_unirse_banda/', views.solicitud_unirse_banda, name='solicitud_unirse_banda'),
    path('musico/<int:id>/', views.detalles_musico, name='detalles_musico'),
    path('banda/<int:id>/', views.detalles_banda, name='detalles_banda'),
    path('buscar/', views.buscar, name='buscar'),
    path('bandas/', views.lista_bandas, name='lista_bandas'),
    path('bandas/eliminar/<int:id>/', views.eliminar_banda, name='eliminar_banda'),
    path('agregar_banda/', views.agregar_banda, name='agregar_banda'),
]


