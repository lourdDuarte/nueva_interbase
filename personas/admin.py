from django.contrib import admin
from .models import Persona
from .models import PersonasNoEncontradas
# Register your models here.

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id','dni', 'nombre', 'apellido']
    search_fields = ('dni','nombre','apellido' )



@admin.register(PersonasNoEncontradas)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id','numero_documento', 'sexo']
    search_fields = ('numero_documento','sexo' )


