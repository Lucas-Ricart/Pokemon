import requests
import json
import os

class PokemonAPI:
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    @staticmethod
    def get_pokemon(nom):
        """Récupère les infos d'un Pokémon par son nom ou ID"""
        response = requests.get(f"{PokemonAPI.BASE_URL}{nom.lower()}")
        if response.status_code == 200:
            data = response.json()
            return {
                "nom": data["name"].capitalize(),
                "types": [t["type"]["name"].capitalize() for t in data["types"]],
                "pv": data["stats"][0]["base_stat"],
                "attaque": data["stats"][1]["base_stat"],
                "defense": data["stats"][2]["base_stat"],
                "capacites": [m["move"]["name"] for m in data["moves"][:4]],  # Prend 4 attaques max
            }
        else:
            print(f"Erreur : Pokémon {nom} introuvable.")
            return None


class Pokemon:
    def __init__(self, nom, types, pv, attaque, defense, capacites):
        self.nom = nom
        self.types = types
        self.pv_max = pv
        self.pv = pv
        self.attaque = attaque
        self.defense = defense
        self.capacites = capacites  # Liste des attaques

    @classmethod
    def from_api(cls, nom):
        """Créer un Pokémon en récupérant ses infos depuis l'API"""
        data = PokemonAPI.get_pokemon(nom)
        if data:
            return cls(
                data["nom"],
                data["types"],
                data["pv"],
                data["attaque"],
                data["defense"],
                data["capacites"]
            )
        return None

class PokemonStorage:
    FILE_PATH = "pokemon.json"

    @staticmethod
    def save_pokemon(pokemon):
        """Ajoute un Pokémon au fichier JSON en évitant les doublons"""
        pokemons = PokemonStorage.load_pokemons()
        if pokemon.nom not in pokemons:
            pokemons[pokemon.nom] = vars(pokemon)
            with open(PokemonStorage.FILE_PATH, "w") as f:
                json.dump(pokemons, f, indent=4)
            print(f"{pokemon.nom} ajouté à {PokemonStorage.FILE_PATH}.")

    @staticmethod
    def load_pokemons():
        """Charge les Pokémon sauvegardés"""
        if os.path.exists(PokemonStorage.FILE_PATH):
            with open(PokemonStorage.FILE_PATH, "r") as f:
                return json.load(f)
        return {}

# Test de sauvegarde
if __name__ == "__main__":
    bulbizarre = Pokemon.from_api("bulbasaur")
    if bulbizarre:
        PokemonStorage.save_pokemon(bulbizarre)
# Test de création d'un Pokémon
if __name__ == "__main__":
    bulbizarre = Pokemon.from_api("bulbasaur")
    print(vars(bulbizarre))