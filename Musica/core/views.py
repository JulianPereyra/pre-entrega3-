from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse

def index(request):
    return render(request, "core/index.html")

def login_view(request):
    if request.method == 'POST':
        print("POST request received")
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Usuario autenticado correctamente")
                login(request, user)
                return redirect('Integrantes:pagina_principal')
            else:
                print("Authentication failed: nombre de usuario o contraseña invalido")
        else:
            print("Form is not valid")
    else:
        form = AuthenticationForm()
    return render(request, 'core/registrar/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('core:login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Integrantes:pagina_principal')
    else:
        form = UserCreationForm()
    return render(request, 'core/registrar/register.html', {'form': form})


def about_me(request):
    return render(request, 'core/registrar/about_me.html')
