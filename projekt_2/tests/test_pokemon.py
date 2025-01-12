# tests/test_pokemon.py

import unittest
from projekt_2.app.model.pokemon import Pokemon
from projekt_2.app.model.stats import Stats

class TestPokemon(unittest.TestCase):
    def setUp(self):
        stats = Stats(attack=55, defense=40, hp=90, special_attack=50, special_defense=45, speed=60)
        self.pokemon = Pokemon(name="Pikachu", types=["Electric"], stats=stats)

    def test_pokemon_initialization(self):
        self.assertEqual(self.pokemon.name, "Pikachu")
        self.assertEqual(self.pokemon.types, ["Electric"])
        self.assertEqual(self.pokemon.stats.attack, 55)

    def test_pokemon_to_dict(self):
        pokemon_dict = self.pokemon.to_dict()
        self.assertEqual(pokemon_dict["name"], "Pikachu")
        self.assertEqual(pokemon_dict["types"], ["Electric"])
        self.assertEqual(pokemon_dict["stats"]["attack"], 55)

