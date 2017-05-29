# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import DatosUser1, Visitas, Alergias_Medicamentos

# Register your models here.

class AdminUsuario(admin.ModelAdmin):
    list_display=["nombre","email","edad","fechaNacimiento","Tipo_Sangre"]
    search_fields = ["nombre","email"]
    list_editable = ["email"]
    list_filter = ["fechaNacimiento","edad"]
    class Meta:
        model = DatosUser1


admin.site.register(DatosUser1, AdminUsuario)

class adminvisitas(admin.ModelAdmin):
    list_display=["doctor","motivo","problema","NotaMedic"]
    search_fields = ["doctor"]
    list_filter = ["problema","NotaMedic","motivo"]
    class Meta:
        model = Visitas

admin.site.register(Visitas, adminvisitas)

class adminalergias(admin.ModelAdmin):
    list_display=["medicamento","motivo","alergias"]
    search_fields = ["medicamento"]
    list_filter = ["alergias","motivo"]
    class Meta:
        model = Alergias_Medicamentos
        
admin.site.register(Alergias_Medicamentos, adminalergias)
