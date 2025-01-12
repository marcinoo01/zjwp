import unittest
from projekt_2.app.model.pokemon import Pokemon
from projekt_2.app.model.fire_pokemon import FirePokemon
from projekt_2.app.model.electric_pokemon import ElectricPokemon
from projekt_2.app.model.stats import Stats
from projekt_2.app.utils.pokemon_mapper import map_pokemon
class TestMapPokemon(unittest.TestCase):

    def test_map_fire_pokemon(self):
        pokemon_data = {
            "name": "Charmander",
            "types": ["fire"],
            "stats": Stats(attack=52, defense=43, hp=39, special_attack=60, special_defense=50, speed=65)
        }
        result = map_pokemon(pokemon_data)
        self.assertIsInstance(result, FirePokemon)
        self.assertEqual(result.name, "Charmander")
        self.assertEqual(result.stats.attack, 52)
        self.assertEqual(result.stats.defense, 43)
        self.assertEqual(result.stats.hp, 39)

    def test_map_electric_pokemon(self):
        pokemon_data = {
            "name": "Pikachu",
            "types": ["electric"],
            "stats": Stats(attack=55, defense=40, hp=35, special_attack=50, special_defense=50, speed=90)
        }
        result = map_pokemon(pokemon_data)
        self.assertIsInstance(result, ElectricPokemon)
        self.assertEqual(result.name, "Pikachu")
        self.assertEqual(result.stats.attack, 55)
        self.assertEqual(result.stats.defense, 40)
        self.assertEqual(result.stats.hp, 35)

    def test_map_default_pokemon(self):
        pokemon_data = {
            "name": "Bulbasaur",
            "types": ["grass", "poison"],
            "stats": Stats(attack=49, defense=49, hp=45, special_attack=65, special_defense=65, speed=45)
        }
        result = map_pokemon(pokemon_data)
        self.assertIsInstance(result, Pokemon)
        self.assertEqual(result.name, "Bulbasaur")
        self.assertEqual(result.types, ["grass", "poison"])
        self.assertEqual(result.stats.attack, 49)
        self.assertEqual(result.stats.defense, 49)
        self.assertEqual(result.stats.hp, 45)

