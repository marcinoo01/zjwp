from projekt_2.app.model.redis_handler import RedisHandler
from projekt_2.app.utils.pokemon_mapper import map_pokemon


class PokemonCache(RedisHandler):
    def __init__(self, redis_instance):
        super().__init__(redis_instance)

    def get_pokemons(self):
        raw_pokemons = self.get_data("pokemons")
        return [map_pokemon(pokemon) for pokemon in raw_pokemons]

    def save_pokemons(self, pokemons):
        serialized_pokemons = [pokemon.to_dict() for pokemon in pokemons]
        self.set_data("pokemons", serialized_pokemons)
