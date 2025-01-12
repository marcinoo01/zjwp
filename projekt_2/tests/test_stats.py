import unittest
import json
from projekt_2.app.model.stats import Stats


class TestStatsFromJson(unittest.TestCase):

    def test_from_json_with_valid_json_string(self):
        json_data = '{"attack": 55, "defense": 40, "hp": 90, "special-attack": 50, "special-defense": 45, "speed": 60}'
        stats = Stats.from_json(json_data)

        self.assertEqual(stats.attack, 55)
        self.assertEqual(stats.defense, 40)
        self.assertEqual(stats.hp, 90)
        self.assertEqual(stats.special_attack, 50)
        self.assertEqual(stats.special_defense, 45)
        self.assertEqual(stats.speed, 60)

    def test_from_json_with_dict(self):
        json_data = {
            "attack": 70,
            "defense": 50,
            "hp": 100,
            "special-attack": 60,
            "special-defense": 50,
            "speed": 80
        }
        stats = Stats.from_json(json_data)

        self.assertEqual(stats.attack, 70)
        self.assertEqual(stats.defense, 50)
        self.assertEqual(stats.hp, 100)
        self.assertEqual(stats.special_attack, 60)
        self.assertEqual(stats.special_defense, 50)
        self.assertEqual(stats.speed, 80)

    def test_from_json_with_missing_fields(self):
        json_data = '{"attack": 30}'
        stats = Stats.from_json(json_data)

        self.assertEqual(stats.attack, 30)
        self.assertEqual(stats.defense, 0)
        self.assertEqual(stats.hp, 0)
        self.assertEqual(stats.special_attack, 0)
        self.assertEqual(stats.special_defense, 0)
        self.assertEqual(stats.speed, 0)

    def test_from_json_with_empty_json(self):
        json_data = '{}'
        stats = Stats.from_json(json_data)

        self.assertEqual(stats.attack, 0)
        self.assertEqual(stats.defense, 0)
        self.assertEqual(stats.hp, 0)
        self.assertEqual(stats.special_attack, 0)
        self.assertEqual(stats.special_defense, 0)
        self.assertEqual(stats.speed, 0)

    def test_from_json_with_invalid_json(self):
        json_data = 'not a json'
        with self.assertRaises(json.JSONDecodeError):
            Stats.from_json(json_data)
