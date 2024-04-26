from django.contrib import admin
from .models import Domicilio
# Register your models here.

@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    list_display = ['id','entidad', 'persona']
    search_fields = ('persona','entidad')