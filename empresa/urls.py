"""
URL configuration for empresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('django.contrib.auth.urls')), # Includes login/logout
    path('accounts/profile/', views.perfil, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('', views.inicio, name='inicio'),
    path('perfil/', views.perfil, name='perfil'),
    path('modulos/', views.modulos, name='modulos'),
    path('modulo1/', views.modulo1, name='modulo1'),
    path('modulo2/', views.modulo2, name='modulo2'),
    path('modulo3/', views.modulo3, name='modulo3'),
    path('modulo4/', views.modulo4, name='modulo4'),
    path('modulo5/', views.modulo5, name='modulo5'),
    path('modulo6/', views.modulo6, name='modulo6'),
    path('modulo7/', views.modulo7, name='modulo7'),

]
