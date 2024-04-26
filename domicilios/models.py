from django.db import models
from personas.models import Persona
from entidades.models import Entidad

# Create your models here.
class Domicilio(models.Model):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    domicilio = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.persona