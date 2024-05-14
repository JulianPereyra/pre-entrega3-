from django.urls import path
from . import views

app_name = "Integrantes"

urlpatterns = [
    path("", views.index, name="index"),
]