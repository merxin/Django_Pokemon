from django.contrib import admin
from .models import Pokemons, Type, Second_Type
# Register your models here.
admin.site.register(Pokemons)
admin.site.register(Type)
admin.site.register(Second_Type)