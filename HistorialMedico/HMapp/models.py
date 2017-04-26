# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PerfilMedico(models.Model):
    nombre = models.CharField(max_length = 30)
    edad = models.CharField(max_length = 100)
    fechaNacimiento = models.DateTimeField()
    tipoSangre = models.TextField()

    def __unicode__(self):
        return self.nombre
