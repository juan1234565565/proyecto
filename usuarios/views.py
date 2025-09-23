from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
