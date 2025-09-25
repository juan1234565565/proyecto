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


@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')