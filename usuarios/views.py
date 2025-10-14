from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirigir a la página de login
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def inicio(request):
    return render(request, 'usuarios/inicio.html')


def perfil(request):
    return render(request, 'usuarios/perfil.html')

def modulos(request):
    return render(request, 'usuarios/modulos.html')


def modulo1(request):
    return render(request, 'Modulo/modulo1.html')

def pruebaMod1(request):
    return render(request, 'Cuestionarios/pruebaMod1.html')

def modulo2(request):
    return render(request, 'Modulo/modulo2.hmtl')
