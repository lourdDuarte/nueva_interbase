from django.db import models
from personas.models import Persona
from entidades.models import Entidad
# Create your models here.


class Contacto(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    persona =  models.ForeignKey(Persona, on_delete=models.CASCADE)
    email = models.CharField(max_length=500, blank=True, null=True)
    telefono_movil = models.CharField(max_length=500, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=500, blank=True, null=True)
    

    def __str__(self):
        return self.persona