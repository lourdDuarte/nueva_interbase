from django.contrib import admin
from .models import Renaper


@admin.register(Renaper)
class RenaperAdmin(admin.ModelAdmin):
    list_display = ['id','numerodocumento', 'apellido', 'nombres']
    search_fields = ('numerodocumento','apellido','nombres' )