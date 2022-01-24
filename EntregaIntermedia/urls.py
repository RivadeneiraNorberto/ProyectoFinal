"""EntregaIntermedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from App import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('servicios/', views.Servicios, name='servicios'),
    path('tecnicos/', views.Tecnicos, name='tecnicos'),
    path('insumos/', views.Insumos, name='insumos'),
    path('altaServicio/', views.AltaServicio, name='altaServicio'),
    path('altaInsumo/', views.AltaInsumo, name='altaInsumo'),
    path('altaTecnico/', views.AltaTecnico, name='altaTecnico'),
    path('buscarInsumo/', views.BuscarInsumo, name='buscarInsumo'),
    path('buscarServicio/', views.BuscarServicio, name='buscarServicio'),
    path('buscarTecnico/', views.BuscarTecnico, name='buscarTecnico'),
    path('busquedaInsumo/', views.BusquedaInsumo, name='busquedaInsumo'),
    path('busquedaServicio/', views.BusquedaServicio, name='busquedaServicio'),
    path('busquedaTecnico/', views.BusquedaTecnico, name='busquedaTecnico'),
]
