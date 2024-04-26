from django.db import models

# Create your models here.

class Entidad(models.Model):
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.descripcion