import pygame
import json
import os

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load local Pokédex
def load_pokedex():
    try:
        with open("pokedex.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\u26a0\ufe0f Erreur: pokedex.json introuvable ou corrompu.")
        return {}

# Dictionary of attacks by type
TYPE_ATTACKS = {
    "fire": "Flamethrower",
    "water": "Hydro Pump",
    "grass": "Solar Beam",
    "electric": "Thunderbolt",
    "ice": "Ice Beam",
    "fighting": "Close Combat",
    "poison": "Sludge Bomb",
    "ground": "Earthquake",
    "flying": "Air Slash",
    "psychic": "Psychic",
    "bug": "X-Scissor",
    "rock": "Stone Edge",
    "ghost": "Shadow Ball",
    "dragon": "Dragon Claw",
    "dark": "Dark Pulse",
    "steel": "Iron Head",
    "fairy": "Moonblast",
    "normal": "Body Slam"
}

# Constants for type advantages in battles
TYPE_ADVANTAGES = {
    "normal": {"rock": 0.5, "ghost": 0, "steel": 0.5},
    "fire": {"grass": 2, "water": 0.5, "fire": 0.5, "ice": 2, "bug": 2, "steel": 2, "rock": 0.5, "dragon": 0.5},
    "water": {"fire": 2, "grass": 0.5, "water": 0.5, "ground": 2, "rock": 2, "dragon": 0.5},
    "grass": {"water": 2, "fire": 0.5, "grass": 0.5, "flying": 0.5, "poison": 0.5, "ground": 2, "rock": 2, "bug": 0.5, "dragon": 0.5, "steel": 0.5},
    "electric": {"water": 2, "ground": 0, "flying": 2, "electric": 0.5, "dragon": 0.5},
    "ice": {"fire": 0.5, "water": 0.5, "ice": 0.5, "grass": 2, "ground": 2, "flying": 2, "dragon": 2, "steel": 0.5},
    "fighting": {"normal": 2, "flying": 0.5, "poison": 0.5, "rock": 2, "bug": 0.5, "ghost": 0, "steel": 2, "ice": 2, "psychic": 0.5, "dark": 2, "fairy": 0.5},
    "poison": {"grass": 2, "ground": 0.5, "rock": 0.5, "ghost": 0.5, "steel": 0, "fairy": 2},
    "ground": {"fire": 2, "electric": 2, "grass": 0.5, "poison": 2, "flying": 0, "rock": 2, "steel": 2},
    "flying": {"electric": 0.5, "fighting": 2, "ground": 1, "rock": 0.5, "bug": 2, "steel": 0.5},
    "psychic": {"fighting": 2, "poison": 2, "psychic": 0.5, "dark": 0, "steel": 0.5, "bug": 0.5},
    "bug": {"fire": 0.5, "fighting": 0.5, "grass": 2, "flying": 0.5, "poison": 0.5, "ghost": 0.5, "steel": 0.5, "psychic": 2, "dark": 2, "fairy": 0.5},
    "rock": {"fire": 2, "fighting": 0.5, "flying": 2, "ground": 0.5, "bug": 2, "steel": 0.5, "ice": 2},
    "ghost": {"normal": 0, "psychic": 2, "ghost": 2, "dark": 0.5},
    "dragon": {"dragon": 2, "steel": 0.5, "fairy": 0},
    "dark": {"fighting": 0.5, "ghost": 2, "psychic": 2, "fairy": 0.5},
    "steel": {"fire": 0.5, "water": 0.5, "electric": 0.5, "ice": 2, "rock": 2, "steel": 0.5, "fairy": 2},
    "fairy": {"fighting": 2, "poison": 0.5, "steel": 0.5, "dragon": 2, "dark": 2}
}

# Paths for sprite folders
SPRITES_PLAYER_FOLDER = os.path.join("sprites", "pokemon", "back")
SPRITES_OPPONENT_FOLDER = os.path.join("sprites", "pokemon")

# Function to load a local image
def load_local_image(number, is_player=True):
    """Loads an image from the sprite folder using the number."""
    try:
        if is_player:
            path = os.path.join(SPRITES_PLAYER_FOLDER, f"{number}.png")
        else:
            path = os.path.join(SPRITES_OPPONENT_FOLDER, f"{number}.png")
        if os.path.exists(path):
            return pygame.image.load(path)
        else:
            print(f"❌ File not found: {path}")
            return None
    except Exception as e:
        print(f"❌ Error loading image for Pokémon No. {number}: {e}")
        return None
