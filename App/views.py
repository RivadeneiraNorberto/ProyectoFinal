
from dataclasses import fields
from pyexpat import model
from urllib import request
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from App.forms import FormAvatar, formAltaInsumo, formAltaServicio, formAltaTecnico, formAltaInsumo, FormAvatar
from .models import Avatar, Servicio, Tecnico, Insumo

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def Inicio(request):
    avatares = Avatar.objects.filter(user=request.user)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
        
    return render(request,'App/inicio.html', {'avatar_url':avatar_url})

@login_required
def Servicios(request):
    return render(request,'App/servicios.html', {'servicios': Servicio.objects.all()})

def Tecnicos(request):
    return render(request,'App/tecnicos.html', {'tecnicos': Tecnico.objects.all()})

def Insumos(request):
    return render(request,'App/insumos.html', {'insumos': Insumo.objects.all()})

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

class AvatarView():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url'] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        return context
    
#######  TECNICOS
class TecnicoListView(LoginRequiredMixin, ListView, AvatarView):
    model = Tecnico
    template_name = 'App/tecnicos.html'
    context_object_name = 'tecnicos'
    
class TecnicoDetailView(LoginRequiredMixin, DetailView, AvatarView):
    model = Tecnico
    template_name = 'App/detalleTecnico.html'
    
class TecnicoCreateView(LoginRequiredMixin, CreateView, AvatarView):
    model = Tecnico
    success_url = reverse_lazy('tecnicos')
    fields = ['nombre', 'apellido', 'edad']
    template_name = 'App/tecnicoForm.html'
    
class TecnicoUpdateView(LoginRequiredMixin, UpdateView,AvatarView):
    model = Tecnico
    success_url = reverse_lazy('tecnicos')
    fields = ['nombre', 'apellido', 'edad']
    template_name = 'App/tecnicoForm.html'
    
class TecnicoDeleteView(LoginRequiredMixin, DeleteView,AvatarView):
    model = Tecnico
    success_url = reverse_lazy('tecnicos')
    template_name = 'App/tecnicoDelete.html'
    
#######  SERVICIOS

class ServicioListView(LoginRequiredMixin, ListView, AvatarView):
    model = Servicio
    template_name = 'App/servicios.html'
    context_object_name = 'servicios'
    
class ServicioDetailView(LoginRequiredMixin, DetailView,AvatarView):
    model = Servicio
    template_name = 'App/detalleServicio.html'
    
class ServicioCreateView(LoginRequiredMixin, CreateView, AvatarView):
    model = Servicio
    success_url = reverse_lazy('servicios')
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'App/servicioForm.html'
    
class ServicioUpdateView(LoginRequiredMixin, UpdateView,AvatarView):
    model = Servicio
    success_url = reverse_lazy('servicios')
    fields = ['nombre', 'descripcion', 'precio']
    template_name = 'App/servicioForm.html'
    
class ServicioDeleteView(LoginRequiredMixin, DeleteView,AvatarView):
    model = Servicio
    success_url = reverse_lazy('servicios')
    template_name = 'App/servicioDelete.html'
    

#######  INSUMOS

class InsumoListView(LoginRequiredMixin, ListView, AvatarView):
    model = Insumo
    template_name = 'App/insumos.html'
    context_object_name = 'insumos'
    
class InsumoDetailView(LoginRequiredMixin, DetailView, AvatarView):
    model = Insumo
    template_name = 'App/detalleInsumo.html'
    
class InsumoCreateView(LoginRequiredMixin, CreateView, AvatarView):
    model = Insumo
    success_url = reverse_lazy('insumos')
    fields = ['nombre', 'cantidad']
    template_name = 'App/insumoForm.html'
    
class InsumoUpdateView(LoginRequiredMixin, UpdateView, AvatarView):
    model = Insumo
    success_url = reverse_lazy('insumos')
    fields = ['nombre', 'cantidad']
    template_name = 'App/insumoForm.html'
    
class InsumoDeleteView(LoginRequiredMixin, DeleteView, AvatarView):
    model = Insumo
    success_url = reverse_lazy('insumos')
    template_name = 'App/insumoDelete.html'

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        formulario = FormAvatar(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect('inicio')
    else:
        formulario = FormAvatar()
        
    return render(request, 'App/crearAvatar.html', {'form': formulario})

@login_required
def nosotros(request):
    return render(request, 'App/nosotros.html')