import django_filters
from .models import Pokemons

class PokemonFilter(django_filters.FilterSet):
    total = django_filters.RangeFilter()

    def __init__(self, *args, **kwargs):
        super(PokemonFilter, self).__init__(*args, **kwargs)


    class Meta:
        model = Pokemons
        fields = {'name': ['icontains'],
                  'hp': ['gt'],
                  'type': ['exact'],
                  # 'type': ['icontains'],
                  # 'defense': ['gt'],
                  # 'attack': ['gt'],

                                    }