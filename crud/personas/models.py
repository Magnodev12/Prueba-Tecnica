from django.db import models
from django.db.models.base import Model

class Persona(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    cedula = models.CharField(max_length=100, blank=False, null=False)
    telefono = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name




# Create your models here.
