import json
from moves import Move
from utils import load_pokedex
from utils import TYPE_ATTACKS
class Pokemon:
    def __init__(self, name, types, hp, attack, special_attack, defense, speed, level=5, exp=0, evolution=None, evolution_level=None):
        self.name = name
        self.types = types
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.special_attack = special_attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.exp = exp
        self.evolution = evolution
        self.evolution_level = evolution_level
        self.moves = self.assign_moves()

    def assign_moves(self):
        """Assigns moves based on the Pokémon's types."""
        moves = []
        for t in self.types:
            if t in TYPE_ATTACKS:
                power = self.special_attack if self.special_attack > self.attack else self.attack
                moves.append(Move(TYPE_ATTACKS[t], power, t))
        return moves

    def gain_experience(self, exp_gained):
        """Adds experience and levels up if necessary."""
        self.exp += exp_gained
        exp_threshold = self.level * 10  
        while self.exp >= exp_threshold:
            self.exp -= exp_threshold
            self.level_up()
            exp_threshold = self.level * 10
    def take_damage(self, damage):
        """Reduces the Pokémon's HP by the given damage."""
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(f"💀 {self.name} has fainted!")

    def is_fainted(self):
        """Returns True if the Pokémon has fainted."""
        return self.hp <= 0
    def level_up(self):
        """Increases the Pokémon's level and improves its stats."""
        self.level += 1
        self.max_hp += 10
        self.attack += 5
        self.defense += 5
        self.speed += 5
        self.hp = self.max_hp  # Restore HP after leveling up
        if self.evolution and self.evolution_level and self.level >= self.evolution_level:
            self.evolve()

    def evolve(self):
        """Evolves the Pokémon if possible."""
        if self.evolution:
            evolved_pokemon = fetch_pokemon(self.evolution)
            if evolved_pokemon:
                self.__dict__.update(evolved_pokemon.__dict__)

    def to_dict(self):
        """Returns a serializable dictionary of the Pokémon."""
        return {
            "name": self.name,
            "types": self.types,
            "hp": self.hp,
            "attack": self.attack,
            "special_attack": self.special_attack,
            "defense": self.defense,
            "speed": self.speed,
            "level": self.level,
            "exp": self.exp,
            "evolution": self.evolution,
            "evolution_level": self.evolution_level,
            "moves": [m.__dict__ for m in self.moves]
        }

def fetch_pokemon(name):
    """Retrieves a Pokémon from the local Pokédex."""
    pokedex = load_pokedex()
    if name.lower() in pokedex:
        data = pokedex[name.lower()]
        return Pokemon(
            name=data["name"],
            types=data["types"],
            hp=data["hp"],
            attack=data["attack"],
            special_attack=data["special_attack"],
            defense=data["defense"],
            speed=data["speed"],
            evolution=data.get("evolution"),
            evolution_level=data.get("evolution_level")
        )
    else:
        print(f"❌ {name} does not exist in the local Pokédex.")
        return None
def assign_moves(self):
        """Assigns moves based on the Pokémon's types."""
        from constants import TYPE_ATTACKS
        moves = []
        for t in self.types:
            if t in TYPE_ATTACKS:
                # Use Attack or Special Attack, whichever is higher
                power = self.special_attack if self.special_attack > self.attack else self.attack
                moves.append(Move(TYPE_ATTACKS[t], power, t))
        return moves

def choose_move(self):
        """Chooses a move based on the Pokémon's types."""
        if not self.moves:
            return None
        # Randomly select a move from the available moves
        return random.choice(self.moves)
