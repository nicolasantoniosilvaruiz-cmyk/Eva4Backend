from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import VideojuegoForm
from .models import Videojuego


class VideojuegoListView(ListView):
    model = Videojuego
    template_name = "catalogo/lista.html"
    context_object_name = "videojuegos"
    queryset = Videojuego.objects.select_related("genero").order_by("titulo")


class VideojuegoDetailView(DetailView):
    model = Videojuego
    template_name = "catalogo/detalle.html"
    context_object_name = "videojuego"
    queryset = Videojuego.objects.select_related("genero")


class VideojuegoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    success_message = 'Videojuego añadido correctamente.'
    model = Videojuego
    form_class = VideojuegoForm
    template_name = "catalogo/formulario.html"
    success_url = reverse_lazy("catalogo:lista")


class VideojuegoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    success_message = 'Cambios guardados correctamente.'
    model = Videojuego
    form_class = VideojuegoForm
    template_name = "catalogo/formulario.html"
    success_url = reverse_lazy("catalogo:lista")


class VideojuegoDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    success_message = 'Videojuego eliminado correctamente.'
    model = Videojuego
    template_name = "catalogo/confirmar_eliminacion.html"
    success_url = reverse_lazy("catalogo:lista")
