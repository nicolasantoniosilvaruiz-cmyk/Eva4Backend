from django.urls import path

from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.VideojuegoListView.as_view(), name="lista"),
    path("nuevo/", views.VideojuegoCreateView.as_view(), name="crear"),
    path("juegos/<int:pk>/", views.VideojuegoDetailView.as_view(), name="detalle"),
    path("juegos/<int:pk>/editar/", views.VideojuegoUpdateView.as_view(), name="editar"),
    path("juegos/<int:pk>/eliminar/", views.VideojuegoDeleteView.as_view(), name="eliminar"),
]
