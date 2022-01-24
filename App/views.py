
from django.shortcuts import render, redirect
from django.http import HttpResponse

from App.forms import formAltaInsumo, formAltaServicio, formAltaTecnico
from .models import Servicio, Tecnico, Insumo
# Create your views here.

def Inicio(request):
    return render(request,'App/inicio.html')

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

def BuscarInsumo(request):
    return render (request, 'App/buscarInsumo.html')

def BuscarServicio(request):
    return render (request, 'App/buscarServicio.html')

def BuscarTecnico(request):
    return render (request, 'App/buscarTecnico.html')

def BusquedaInsumo(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        insumos = Insumo.objects.filter(nombre__icontains=nombre)
        return render (request,'App/busquedaInsumo.html', {'insumos':insumos,'nombre':nombre})
    else:
        return HttpResponse(f'No enviaste datos para buscar.')
    
    
def BusquedaServicio(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        servicios = Servicio.objects.filter(nombre__icontains=nombre)
        return render (request,'App/busquedaServicio.html', {'servicios':servicios,'nombre':nombre})
    else:
        return HttpResponse(f'No enviaste datos para buscar.')

def BusquedaTecnico(request): 
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        tecnicos = Tecnico.objects.filter(nombre__icontains=nombre)
        return render (request,'App/busquedaTecnico.html', {'tecnicos':tecnicos,'nombre':nombre})
    else:
        return HttpResponse(f'No enviaste datos para buscar.')