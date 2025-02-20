import json


class Pokemon:
    def __init__(self, key: str, level: int = 1) -> None:
        """Initializes a Pokémon with its attributes and levels it up if needed."""
        with open("list-pokemon.json", "r") as f:
            self.list_pokemon = json.load(f)  # Load the Pokémons data

        # Pokémon base stats
        self.key = key
        self.name = self.list_pokemon[self.key]["name"]
        self.type = self.list_pokemon[self.key]["type"]
        self.base_hp = self.list_pokemon[self.key]["hp"]
        self.base_attack = self.list_pokemon[self.key]["attack"]
        self.base_defense = self.list_pokemon[self.key]["defense"]
        self.base_special_attack = self.list_pokemon[self.key]["special_attack"]
        self.base_special_defense = self.list_pokemon[self.key]["special_defense"]
        self.base_speed = self.list_pokemon[self.key]["speed"]
        self.base_xp = self.list_pokemon[self.key]["base_xp"]

        evolution_data = self.list_pokemon[self.key].get("evolution")
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
        if self.level < 100:
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
            self.evolve(self.level)

    def evolve(self, level) -> None:
        """Handles Pokémon evolution."""
        self.key = str(int(self.key) + 1)  # Update key to next Pokémon
        self.name = self.list_pokemon[self.key]["name"]
        self.type = self.list_pokemon[self.key]["type"]
        self.base_hp = self.list_pokemon[self.key]["hp"]
        self.base_attack = self.list_pokemon[self.key]["attack"]
        self.base_defense = self.list_pokemon[self.key]["defense"]
        self.base_special_attack = self.list_pokemon[self.key]["special_attack"]
        self.base_special_defense = self.list_pokemon[self.key]["special_defense"]
        self.base_speed = self.list_pokemon[self.key]["speed"]
        self.base_xp = self.list_pokemon[self.key]["base_xp"]

        evolution_data = self.list_pokemon[self.key].get("evolution")
        self.evolution = evolution_data["next"] if evolution_data else None
        self.evolution_level = evolution_data["level"] if evolution_data else None

        self.level = 1 

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

    def add_xp(self, enemy_level: int, enemy_base_xp: int) -> None:
        """Adds XP to the Pokémon and checks for level-up."""
        needed_xp = 0.8 * (self.level ** 3)
        self.xp += (enemy_base_xp * enemy_level) / 7

        if self.xp >= needed_xp:
            over_xp = self.xp - needed_xp
            self.xp = over_xp  # Carry over extra XP
            self.level_up()

    def __str__(self):
        return f"{self.level} {self.name}"

pokemon = Pokemon("1", 72)
print(pokemon)  # Doit afficher l'ID du Pokémon