from django.contrib import admin
from .models import Contacto



@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['entidad', 'persona', 'email']
    search_fields = ('entidad','persona', 'email')

