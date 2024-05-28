from django.urls import path
from . import views

app_name = 'core'  

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('about_me/', views.about_me, name='about_me'),
]

