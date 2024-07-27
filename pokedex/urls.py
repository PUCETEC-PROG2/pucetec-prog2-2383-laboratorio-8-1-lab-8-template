from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:id>/", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view() , name="login"),
]