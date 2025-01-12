import json

class Stats:
    def __init__(self, attack, defense, hp, special_attack, special_defense, speed):
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def __str__(self):
        return (f"Attack: {self.attack}, Defense: {self.defense}, HP: {self.hp}, "
                f"Special Attack: {self.special_attack}, Special Defense: {self.special_defense}, Speed: {self.speed}")

    def to_dict(self):
        return {
            "attack": self.attack,
            "defense": self.defense,
            "hp": self.hp,
            "special-defense": self.special_defense,
            "special-attack": self.special_attack,
            "speed": self.speed
        }

    @staticmethod
    def from_json(json_data):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        return Stats(
            attack=json_data.get("attack", 0),
            defense=json_data.get("defense", 0),
            hp=json_data.get("hp", 0),
            special_attack=json_data.get("special-attack", 0),
            special_defense=json_data.get("special-defense", 0),
            speed=json_data.get("speed", 0)
        )

    def get(self, key, default=None):
        return self.to_dict().get(key, default)