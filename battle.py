import random
from class_pokemon_joel import Pokemon
import os
import pygame


class Battle:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
        # Dictionary of attacks by type
        self.TYPE_ATTACKS = {
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
        self.TYPE_ADVANTAGES = {
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
        self.SPRITES_PLAYER_FOLDER = os.path.join("sprites", "pokemon", "back")
        self.SPRITES_OPPONENT_FOLDER = os.path.join("sprites", "pokemon")



    def calculate_damage(self, attacker, defender, move):
        """Calculates the damage dealt."""
        damage = move.power
        critical = 1.5 if random.random() < 0.1 else 1.0
        final_damage = max(1, round(damage * critical))
        return final_damage

    def turn(self, attacker, defender):
        """The attacking Pokémon takes its turn."""
        ability = attacker.moves[0]  # Just pick the first move for simplicity
        damage = self.calculate_damage(attacker, defender, ability)
        defender.hp -= damage
        if defender.hp <= 0:
            print(f"💀 {defender.name} is KO!")
            return True
        return False

    def start_battle(self):
        """Starts the battle."""
        print(
            f"⚔️ Battle between {self.player.name} and {self.opponent.name}!")
        while self.player.hp > 0 and self.opponent.hp > 0:
            if self.turn(self.player, self.opponent):
                break
            if self.turn(self.opponent, self.player):
                break
