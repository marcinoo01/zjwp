from projekt_2.app.model.stats import Stats


class Pokemon:
    def __init__(self, name, types, stats):
        self.name = name
        self.types = types
        self.stats = Stats.from_json(stats)

    def __str__(self):
        return f"{self.name} | Types: {', '.join(self.types)} | Stats: {', '.join(self.stats)}"

    def to_dict(self):
        return {
            "name": self.name,
            "types": self.types,
            "stats": self.stats.to_dict()
        }

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        raise KeyError(f"Key '{key}' not found in Pokemon attributes.")

    def __repr__(self):
        return f"Pokemon(name={self.name}, types={self.types}, stats={self.stats})"