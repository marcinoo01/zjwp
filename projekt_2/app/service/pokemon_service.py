import json

import requests

from projekt_2.app.model.electric_pokemon import ElectricPokemon
from projekt_2.app.model.fire_pokemon import FirePokemon
from projekt_2.app.model.pokemon import Pokemon
from projekt_2.app.model.redis_handler import RedisHandler
from projekt_2.app.utils.pokemon_mapper import map_pokemon
from projekt_2.app.utils.utils import get_json_response, print_pokemons_special_effects
from projekt_2.app.model.redis_handler import r

BASE_URL = "https://pokeapi.co/api/v2"

redis_handler = RedisHandler(r)


def find_all_pokemons(limit=10, offset=0):
    url = f"{BASE_URL}/pokemon?limit={limit}&offset={offset}"

    data = get_json_response(url).get('results', [])
    pokemons = []
    lsp = []

    for pokemon in data:
        pokemon_data = requests.get(pokemon['url']).json()
        pokemons.append({
            "name": pokemon_data['name'],
            "types": [t['type']['name'] for t in pokemon_data['types']],
            "stats": {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
        })
        lsp.append(pokemon_data)

    r.append("pokemons", json.dumps(pokemons))
    return pokemons


def compare_pokemon(pokemon1_name, pokemon2_name):
    pokemon1 = fetch_pokemon_data(pokemon1_name)
    pokemon2 = fetch_pokemon_data(pokemon2_name)

    comparison = {
        "pokemon1": pokemon1['name'],
        "pokemon2": pokemon2['name'],
        "stats_comparison": {
            stat: pokemon1['stats'].get(stat, 0) - pokemon2['stats'].get(stat, 0)
            for stat in pokemon1['stats'].keys()
        }
    }

    return comparison


def fetch_pokemon_data(name):
    url = f"{BASE_URL}/pokemon/{name}"

    data = get_json_response(url)

    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    types = [t['type']['name'] for t in data['types']]

    return Pokemon(name=data['name'], types=types, stats=stats).to_dict()


def get_sorted(sort_rq):
    pokemons = redis_handler.get_data("pokemons")
    pokemons = [map_pokemon(pokemon) for pokemon in pokemons]
    print_pokemons_special_effects(pokemons)

    pokemons = sorted(
        pokemons,
        key=lambda pokemon: pokemon.stats.get(sort_rq.field, float('-inf')),
        reverse=(sort_rq.order == 'desc')
    )

    if sort_rq.to_display:
        fields_to_display = sort_rq.to_display.split(',')
        pokemons = [
            {key: value for key, value in pokemon.to_dict().items() if key in fields_to_display}
            for pokemon in pokemons
        ]
    else:
        pokemons = [pokemon.to_dict() for pokemon in pokemons]

    return pokemons[:sort_rq.limit] if sort_rq.limit is not None else pokemons
