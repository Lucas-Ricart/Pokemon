import json


class Pokemon:
    def __init__(self, key: str, level: int = 1) -> None:
        """Initializes a Pokémon with its attributes and levels it up if needed."""
        with open("pokedex.json", "r") as f:
            self.pokedex = json.load(f)  # Load the Pokédex data

        # Pokémon base stats
        self.key = key
        self.name = self.pokedex[self.key]["name"]
        self.type = self.pokedex[self.key]["type"]
        self.base_hp = self.pokedex[self.key]["hp"]
        self.base_attack = self.pokedex[self.key]["attack"]
        self.base_defense = self.pokedex[self.key]["defense"]
        self.base_special_attack = self.pokedex[self.key]["special_attack"]
        self.base_special_defense = self.pokedex[self.key]["special_defense"]
        self.base_speed = self.pokedex[self.key]["speed"]
        self.base_xp = self.pokedex[self.key]["base_xp"]

        evolution_data = self.pokedex[self.key].get("evolution")
        self.evolution = evolution_data["next"] if evolution_data else None
        self.evolution_level = evolution_data["level"] if evolution_data else None

        self.level = 1
        self.xp = 0

        # Initialize stats
        self.max_hp = self.base_hp
        self.attack = self.base_attack
        self.defense = self.base_defense
        self.special_attack = self.base_special_attack
        self.special_defense = self.base_special_defense
        self.speed = self.base_speed

        # Level up to the desired level
        for _ in range(level - 1):
            self.level_up()

    def level_up(self) -> None:
        """Increases the level of the Pokémon and updates its stats."""
        self.level += 1

        # Apply level scaling
        self.max_hp += 0.2 * self.base_hp
        self.attack += 0.2 * self.base_attack
        self.defense += 0.2 * self.base_defense
        self.special_attack += 0.2 * self.base_special_attack
        self.special_defense += 0.2 * self.base_special_defense
        self.speed += 0.2 * self.base_speed

        # Handle evolution
        if self.evolution and self.level >= self.evolution_level:
            self.evolve()

    def evolve(self) -> None:
        """Handles Pokémon evolution."""
        self.key = str(int(self.key) + 1)  # Update key to next Pokémon
        self.name = self.pokedex[self.key]["name"]
        self.type = self.pokedex[self.key]["type"]
        self.base_hp = self.pokedex[self.key]["hp"]
        self.base_attack = self.pokedex[self.key]["attack"]
        self.base_defense = self.pokedex[self.key]["defense"]
        self.base_special_attack = self.pokedex[self.key]["special_attack"]
        self.base_special_defense = self.pokedex[self.key]["special_defense"]
        self.base_speed = self.pokedex[self.key]["speed"]
        self.base_xp = self.pokedex[self.key]["base_xp"]

        evolution_data = self.pokedex[self.key].get("evolution")
        self.evolution = evolution_data["next"] if evolution_data else None
        self.evolution_level = evolution_data["level"] if evolution_data else None

        self.level_up()

    def add_xp(self, enemy_level: int, enemy_base_xp: int) -> None:
        """Adds XP to the Pokémon and checks for level-up."""
        needed_xp = 0.8 * (self.level ** 3)
        self.xp += (enemy_base_xp * enemy_level) / 7

        if self.xp >= needed_xp:
            over_xp = self.xp - needed_xp
            self.xp = over_xp  # Carry over extra XP
            self.level_up()