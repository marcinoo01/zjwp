import requests

from projekt_2.app.model.electric_pokemon import ElectricPokemon
from projekt_2.app.model.fire_pokemon import FirePokemon

valid_stats = ['attack', 'defense', 'hp', 'special-attack', 'special-defense', 'speed']

def get_json_response(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data list")

    return response.json()

def print_pokemons_special_effects(pokemons):
    for pokemon in pokemons:
        if isinstance(pokemon, FirePokemon):
            print(f"{pokemon.name}: {pokemon.special_ability()}")
        elif isinstance(pokemon, ElectricPokemon):
            print(f"{pokemon.name}: {pokemon.special_ability()}")
        else:
            print(f"{pokemon.name}: None")