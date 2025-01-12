from projekt_2.app.model.pokemon import Pokemon


class ElectricPokemon(Pokemon):
    def __init__(self, name, stats):
        super().__init__(name, ["electric"], stats)

    def special_ability(self):
        return "Electric Shock"

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        raise KeyError(f"Key '{key}' not found in Pokemon attributes.")

    def to_dict(self):
        return {
            "name": self.name,
            "types": self.types,
            "stats": self.stats.to_dict()
        }