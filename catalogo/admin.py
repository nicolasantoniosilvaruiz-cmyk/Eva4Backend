from django.contrib import admin

from .models import Genero, Videojuego


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    list_filter = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "genero", "precio", "fecha_lanzamiento", "disponible")
    list_filter = ("genero", "disponible", "fecha_lanzamiento")
    search_fields = ("titulo", "genero__nombre")
