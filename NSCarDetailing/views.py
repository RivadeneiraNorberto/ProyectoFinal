from io import UnsupportedOperation
from django.contrib import messages
from urllib import request
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from App.views import AvatarView

from NSCarDetailing.forms import FormRegistro, UserEditForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contrasenia = form.cleaned_data['password']
            user = authenticate(username=usuario,password=contrasenia)
            
            if user is not None:
                login(request, user)
                return redirect ('inicio')
            else:
                return render(request,'login.html', {'form' : form, 'error' : 'El usuario y/o contrasenia no son validos.'})        
        else:
            return render(request,'login.html', {'form' : form})
    else:
        form = AuthenticationForm()
        return render(request,'login.html', {'form' : form})
    
   
def register(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponse(f'Usuario {username} fue creado correctamente!.')
                  
    else:
        form = FormRegistro()
    
    return render(request,'registro.html', {'form' : form})

class UserCreateView(CreateView, AvatarView):
        model = User
        success_url = reverse_lazy('login')
        template_name = 'registro.html'
        form_class = FormRegistro

@login_required        
def editarPerfil(request):
    usuario = request.user
    
    if request.method == 'POST' :
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            usuario.first_name = data ['first_name']
            usuario.last_name = data ['last_name']
            usuario.save()
            return redirect('inicio')
    else:
        formulario = UserEditForm({'email':usuario.email})
    
    return render(request, 'registro.html', {'form' : formulario})

