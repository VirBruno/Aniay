from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("clientes/", view=views.clients_repository, name="clients_repo"),
    path("clientes/nuevo/", view=views.clients_form, name="clients_form"),
    path("clientes/editar/<int:id>/", view=views.clients_form, name="clients_edit"),
    path("clientes/eliminar/", view=views.clients_delete, name="clients_delete"),
    path("animales/", view=views.pets_repository, name="pets_repo"),
    path("animales/nuevo/", view=views.pets_form, name="pets_form"),
    path("animales/editar/<int:id>/", view=views.pets_form, name="pets_edit"),
    path("animales/eliminar/", view=views.pets_delete, name="pets_delete"),
    path("veterinarios/", view=views.vets_repository, name="vets_repo"),
    path("veterinarios/nuevo/", view=views.vets_form, name="vets_form"),
    path("veterinarios/editar/<int:id>/", view=views.vets_form, name="vets_edit"),
    path("veterinacios/eliminar/", view=views.vets_delete, name="vets_delete"),
]
