import json

class Pokedex:
    def __init__(self):
        with open("list-pokemon.json", "r") as f:
            self.list_pokemon = json.load(f)  # Load the Pokémons data
        self.pokedex = self.load_pokedex()

    def load_pokedex(self):
        try:
            with open("pokedex.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return self.list_pokemon

    def add_pokemon(self, key):
        """Adds a Pokémon to the Pokédex."""
        self.pokedex[key]["encounter"] += 1

    def save_pokedex(self):
        """Saves the Pokédex."""
        with open("pokedex.json", "w") as file:
            json.dump(self.pokedex, file, indent=4)

    # need graphique display
    def display_pokedex(self):
        """Displays the Pokédex."""
        for pokemon in self.pokedex:
            print(f"{pokemon['name']}")
