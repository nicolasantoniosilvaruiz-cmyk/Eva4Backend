from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=150)
    precio = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0"))]
    )
    fecha_lanzamiento = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
