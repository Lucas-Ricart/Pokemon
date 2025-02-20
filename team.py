import json
from pokemon import Pokemon
from utils import load_pokedex

class Team:
    def __init__(self):
        self.pokemons = self.load_team()

    def load_team(self):
        try:
            with open("pokemon.json", "r") as file:
                pokemons_data = json.load(file)
                if not isinstance(pokemons_data, list):
                    return []
                team = [Pokemon(**p) for p in pokemons_data]
                return team
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_pokemon(self, pokemon):
        """Adds a Pokémon to the team and saves it."""
        if len(self.pokemons) < 6:
            self.pokemons.append(pokemon)
            self.save_team()

    def save_team(self):
        """Saves the team to pokemon.json."""
        with open("pokemon.json", "w") as file:
            json.dump([p.to_dict() for p in self.pokemons], file, indent=4)

    def display_team(self):
        """Displays the Pokémon in the team."""
        for pokemon in self.pokemons:
            print(f"{pokemon.name} (Level {pokemon.level})")

    def choose_pokemon(self):
        """Allows the player to choose a Pokémon for battle."""
        if not self.pokemons:
            return None

        for i, pokemon in enumerate(self.pokemons, 1):
            print(f"{i}. {pokemon.name} (Level {pokemon.level})")

        choice = int(input("\nSelect a Pokémon (1-6): ")) - 1
        if 0 <= choice < len(self.pokemons):
            return self.pokemons[choice]
        return None
