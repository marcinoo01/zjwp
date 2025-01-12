from pokemon import Pokemon

class PokemonDetailed(Pokemon):
    def __init__(self, name, types, stats, abilities, moves):
        super().__init__(name, types, stats)
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        return f"{super().__str__()} | Abilities: {', '.join(self.abilities)} | moves: {', '.join(self.moves)}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "abilities": self.abilities,
            "moves": self.moves
        })
        return data