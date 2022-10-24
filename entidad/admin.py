from django.contrib import admin
from .models import Localidad, Persona, Autor, Libro

# Register your models here.

modelos = [Localidad, Persona, Autor, Libro]

admin.site.register(modelos)
