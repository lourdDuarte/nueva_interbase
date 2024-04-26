from django.db import models

# Create your models here.



class Persona(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=500, blank=True, null=True)
    apellido = models.CharField(max_length=500, blank=True, null=True)
    fecha_nacimiento = models.CharField(max_length=500, blank=True, null=True)
    sexo = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.dni



    
class PersonasNoEncontradas(models.Model):
    sexo = models.CharField(max_length=500, blank=True, null=True)
    numero_documento = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.numero_documento