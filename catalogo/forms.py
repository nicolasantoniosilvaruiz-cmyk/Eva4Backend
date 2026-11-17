from django import forms

from .models import Videojuego


class VideojuegoForm(forms.ModelForm):
    class Meta:
        model = Videojuego
        fields = ("titulo", "genero", "precio", "fecha_lanzamiento", "disponible")
        labels = {"titulo": "Título", "genero": "Género"}
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "genero": forms.Select(attrs={"class": "form-select"}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "min": "0", "step": "0.01"}),
            "fecha_lanzamiento": forms.DateInput(
                format="%Y-%m-%d", attrs={"class": "form-control", "type": "date"}
            ),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
