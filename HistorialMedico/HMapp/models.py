# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

Tipo_Sangre = (
('O+', 'O+',),
('O-', 'O-'),
('A+', 'A+'),
('A-', 'A-'),
('B+', 'B+'),
('B-', 'B-'),
('AB+', 'AB+'),
('AB-', 'AB-'),
)


class DatosUser1(models.Model):
    nombre = models.CharField(max_length = 30)
    edad = models.DecimalField(max_digits=100, decimal_places=2)
    fechaNacimiento = models.CharField(max_length=50)
    Tipo_Sangre = models.CharField(max_length=11,choices=Tipo_Sangre)
    email = models.EmailField()


    def __unicode__(self):
      return self.nombre

class Visitas(models.Model):
    doctor = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    problema = models.CharField(max_length=500)
    NotaMedic = models.CharField(max_length=500)



class Alergias_Medicamentos(models.Model):
    """Anota los medicamentos que actualmente estás tomando. Escribe el nombre, el motivo por el cual lo estás tomando, y desde
hace cuanto tiempo:"""
    medicamento = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)

    alergias = models.CharField(max_length=100)





"""
fechaNacimiento = models.DateTimeField(auto_now_add=True, auto_now=False)
"""
