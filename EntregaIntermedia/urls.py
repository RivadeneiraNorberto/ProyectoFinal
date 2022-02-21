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
from django.contrib.auth.views import LogoutView, LoginView
from EntregaIntermedia.settings import MEDIA_ROOT
from EntregaIntermedia.views import UserCreateView, editarPerfil, register , login_request
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('admin', admin.site.urls),
    path('buscarInsumo/', views.BuscarInsumo, name='buscarInsumo'),
    path('buscarServicio/', views.BuscarServicio, name='buscarServicio'),
    path('buscarTecnico/', views.BuscarTecnico, name='buscarTecnico'),
    path('busquedaInsumo/', views.BusquedaInsumo, name='busquedaInsumo'),
    path('busquedaServicio/', views.BusquedaServicio, name='busquedaServicio'),
    path('busquedaTecnico/', views.BusquedaTecnico, name='busquedaTecnico'),
    
    path('tecnicos/', views.TecnicoListView.as_view(), name='tecnicos'),
    path('altaTecnico/', views.TecnicoCreateView.as_view(), name='altaTecnico'),
    path('tecnicos/modificar/<pk>', views.TecnicoUpdateView.as_view(), name='modificarTecnico'),
    path('tecnicos/eliminar/<pk>', views.TecnicoDeleteView.as_view(), name='eliminarTecnico'),
    path('tecnicos/ver/<pk>', views.TecnicoDetailView.as_view(), name='detalleTecnico'),
    
    path('servicios/', views.ServicioListView.as_view(), name='servicios'),
    path('altaServicio/', views.ServicioCreateView.as_view(), name='altaServicio'),
    path('servicios/modificar/<pk>', views.ServicioUpdateView.as_view(), name='modificarServicio'),
    path('servicios/eliminar/<pk>', views.ServicioDeleteView.as_view(), name='eliminarServicio'),
    path('servicios/ver/<pk>', views.ServicioDetailView.as_view(), name='detalleServicio'),
    
    path('insumos/', views.InsumoListView.as_view(), name='insumos'),
    path('altaInsumo/', views.InsumoCreateView.as_view(), name='altaInsumo'),
    path('insumos/modificar/<pk>', views.InsumoUpdateView.as_view(), name='modificarInsumo'),
    path('insumos/eliminar/<pk>', views.InsumoDeleteView.as_view(), name='eliminarInsumo'),
    path('insumos/ver/<pk>', views.InsumoDetailView.as_view(), name='detalleInsumo'),
    
    path('login', login_request, name = 'login'),
    #path('login', LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('registro', register, name = 'registro'),
    path('logout', LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('user/editar', editarPerfil, name = 'editarPerfil'),
    path('user/avatar', views.agregarAvatar, name = 'agregarAvatar'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)