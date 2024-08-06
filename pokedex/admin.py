from django.contrib import admin
from .models import Pokemon
from .models import Trainer

# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass