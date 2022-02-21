from django.contrib import admin

from App.models import Avatar, Insumo, Servicio, Tecnico

# Register your models here.
admin.site.register(Tecnico)
admin.site.register(Servicio)
admin.site.register(Insumo)
admin.site.register(Avatar)