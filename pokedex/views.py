from django.shortcuts import render
from django.http import HttpResponse
from. models import Pokemons, Type
from .filters import PokemonFilter
from django.db.models import Avg, Min, Max, Count
from bs4 import BeautifulSoup
import requests
import pandas as pd


def filter(request):
    all = Pokemons.objects.all()
    filt = Pokemons.objects.all()
    pokemon_filter = PokemonFilter(request.GET, queryset=all)
    types = Type.objects.all()
    name = request.GET.get('name')


    data = {    'all' : all,
                'types' : types,
                'pokemon_filter': pokemon_filter,
                'filt': filt,
                'form': pokemon_filter.form,

            }

    return render(request, 'filter.html', data )






def index(request):
    all = Pokemons.objects.all()
    filt = Pokemons.objects.all()
    name = request.GET.get('name')
    pokemon_filter = PokemonFilter(request.GET, queryset=all)

    # if name:
    #     all = pokemon_filter(name__icontains=name)
    types = Type.objects.all()


    data = {'all' : all,
               'types' : types,
                'pokemon_filter': pokemon_filter,
                'pokemon_filter2': pokemon_filter.qs,
                'name': name,
                'form': pokemon_filter.form,

                # 'pokemon_type': pokemon_type,
                # 'pokemon_object': pokemon_object,
                # 'pokemon_hp': pokemon_hp,
                # 'pokemon_attack': pokemon_attack,
                # 'pokemon_defense': pokemon_defense,
                # 'pokemon_total': pokemon_total,
                # 'pokemon_name' : pokemon_name,

            }
    if not request.GET.get('q'):
        return render(request, 'pokemon.html', data)
    else:
        return render(request, 'filter.html', data)


def category (request, name):

    types = Type.objects.all()
    all = Pokemons.objects.all()
    category_user = Type.objects.get(name=name)
    category_pokemon = Pokemons.objects.filter(type_id=category_user).order_by('-total')
    pokemon_filter = PokemonFilter(request.GET, queryset=all)
    categories = Type.objects.all()
    average_HP = round(category_pokemon.aggregate(Avg('hp')).get('hp__avg'),1)
    average_defense = round(category_pokemon.aggregate(Avg('defense')).get('defense__avg'),1)
    average_attack = round(category_pokemon.aggregate(Avg('attack')).get('attack__avg'),1)
    average_total = round(category_pokemon.aggregate(Avg('total')).get('total__avg'),1)
    count = category_pokemon.aggregate(Count('hp')).get('hp__count')
    filt = Pokemons.objects.all()
    name = request.GET.get('name')



    data = {'types': types,
            'all': all,
            'category_user': category_user,
            'category_pokemon': category_pokemon,
            'pokemon_filter': pokemon_filter,
            'categories': categories,
            'average_HP' : average_HP,
            'average_attack': average_attack,
            'average_defense': average_defense,
            'average_total': average_total,
            'count': count,

}
    return render(request, 'pokemon_types.html', data )

def pokemon(request, name):
    all = Pokemons.objects.all()
    pokemon_object = Pokemons.objects.get(name=name)
    pokemon_type = pokemon_object.type
    pokemon_hp= pokemon_object.hp
    pokemon_attack= pokemon_object.attack
    pokemon_defense= pokemon_object.defense
    pokemon_total= pokemon_object.total
    types = Type.objects.all()
    categories = Type.objects.all()
    url = 'https://www.pokemon.com/uk/pokedex/'+str(pokemon_object)
    r=requests.get(url)
    html=r.text
    soup = BeautifulSoup(html, 'html.parser')
    links = str(soup.find('div',  {'class': 'profile-images'}))
    try:
        image = list(links.split(' '))[4].strip('/> </div>')
        index = image.find('https')
        index2 = image.find('.png')
        image = image[index:(index2+4)]
    except IndexError:
        image = 'https://assets.pokemon.com/assets/cms2/img/misc/gus/buttons/logo-pokemon-79x45.png'

    data = {
            'all': all,
            'types': types,
            'categories': categories,
            'image': image,
            'url': url,
            'pokemon_attack': pokemon_attack,
            'pokemon_hp': pokemon_hp,
            'pokemon_defense': pokemon_defense,
            'pokemon_total': pokemon_total,
            'pokemon_object': pokemon_object,
            'pokemon_type' : pokemon_type,

    }

    return render(request, 'pokemon.html', data)

def comparison(request):
    types = Type.objects.all()
    all = Pokemons.objects.all().values()
    df = pd.DataFrame(all, columns = ["type_id", "hp", "total", "attack"])
    adf= df.groupby("type_id", axis=0).mean()
    adf=adf.round(0).sort_values(by=['total'], ascending= False)
    # adf=adf.style.format('{:.0f}')
    # zz=adf.loc['Bug','hp']

    pokemon_count=all.count()
    list_of_types=[]
    categories = Pokemons.objects.annotate(Count('type'))
    for type in types:
        if type not in list_of_types:
            list_of_types.append(type)
        else: pass


    data = {'types': types,
            'all': all,
            'pokemon_count': pokemon_count,
            'list_of_types': list_of_types,
            'categories': categories,
            'adf': adf.to_html(classes="table table-striped"),
            }


    return render(request, 'comparison.html', data)