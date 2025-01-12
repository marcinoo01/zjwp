from projekt_2.app.model.electric_pokemon import ElectricPokemon
from projekt_2.app.model.fire_pokemon import FirePokemon
from projekt_2.app.model.pokemon import Pokemon


def map_pokemon(self):
    if "fire" in self["types"]:
        return FirePokemon(self["name"], self["stats"])
    elif "electric" in self["types"]:
        return ElectricPokemon(self["name"], self["stats"])
    else:
        return Pokemon(self["name"], self["types"], self["stats"])
