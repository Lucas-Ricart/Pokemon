import json
from pokemon import Pokemon

class Pokedex:
    def __init__(self):
        self.pokemons = self.load_pokedex()

    def load_pokedex(self):
        try:
            with open("pokedex.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_pokemon(self, pokemon):
        """Adds a Pokémon to the Pokédex."""
        if pokemon.name not in [p["name"] for p in self.pokemons]:
            self.pokemons.append(pokemon.to_dict())
            self.save_pokedex()

    def save_pokedex(self):
        """Saves the Pokédex."""
        with open("pokedex.json", "w") as file:
            json.dump(self.pokemons, file, indent=4)

    def display_pokedex(self):
        """Displays the Pokédex."""
        for pokemon in self.pokemons:
            print(f"{pokemon['name']}")
