
from django.shortcuts import render, redirect
from django.http import HttpResponse

from App.forms import formAltaInsumo, formAltaServicio, formAltaTecnico
from .models import Servicio, Tecnico, Insumo
# Create your views here.

def Inicio(request):
    return HttpResponse(f'Esto es el home')

def Servicios(request):
    return render(request,'App/servicios.html', {'servicios': Servicio.objects.all()})

def Tecnicos(request):
    return render(request,'App/tecnicos.html', {'tecnicos': Tecnico.objects.all()})

def Insumos(request):
    return render(request,'App/insumos.html', {'insumos': Insumo.objects.all()})

def AltaServicio(request):
    if request.method == 'POST':
        formulario = formAltaServicio(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Servicio.objects.create(nombre=data['nombre'], descripcion=data['descripcion'], precio=data['precio'])
            return redirect('servicios')
    else:
        formulario=formAltaServicio()
    
    return render(request, 'App/altaServicio.html', {'formulario':formulario})

def AltaInsumo(request):
    if request.method == 'POST':
        formulario = formAltaInsumo(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Insumo.objects.create(cantidad=data['cantidad'], nombre=data['nombre'])
            return redirect('insumos')
    else:
        formulario=formAltaInsumo()
    
    return render(request, 'App/altaInsumo.html', {'formulario':formulario})


def AltaTecnico(request):
    if request.method == 'POST':
        formulario = formAltaTecnico(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Tecnico.objects.create(nombre=data['nombre'], apellido=data['apellido'], edad=data['edad'])
            return redirect('tecnicos')
    else:
        formulario=formAltaTecnico()
    
    return render(request, 'App/altaTecnico.html', {'formulario':formulario})

def BusquedaInsumo(request):
    return render (request, 'App/buscarInsumo.html')

def Busqueda(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        insumos = Insumo.objects.filter(nombre=nombre)
        return render (request,'App/busqueda.html', {'insumos':insumos,'nombre':nombre})
    else:
        return HttpResponse(f'No enviaste datos para buscar.')