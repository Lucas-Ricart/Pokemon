import random
import pygame
import sys
import os

# Pygame Initialization
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokémon Battle")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
DAMAGE_TEXTS = []
MESSAGE_TEXTS = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

POKEMON_LIST = {
    "Sceptile": {
        "name": "Sceptile",
        "types": ["grass"],
        "hp": 70,
        "attack": 85,
        "defense": 65,
        "special_attack": 105,
        "special_defense": 85,
        "speed": 120,
        "moves": [
            {"name": "Leaf Blade", "power": 90, "move_type": "grass"},
            {"name": "Dragon Pulse", "power": 85, "move_type": "dragon"}
        ],
        "number": 254
    },
    "Charizard": {
        "name": "Charizard",
        "types": ["fire", "flying"],
        "hp": 78,
        "attack": 84,
        "defense": 78,
        "special_attack": 109,
        "special_defense": 85,
        "speed": 100,
        "moves": [
            {"name": "Flamethrower", "power": 110, "move_type": "fire"},
            {"name": "Air Slash", "power": 75, "move_type": "flying"}
        ],
        "number": 6
    },
    "Blastoise": {
        "name": "Blastoise",
        "types": ["water"],
        "hp": 79,
        "attack": 83,
        "defense": 100,
        "special_attack": 85,
        "special_defense": 105,
        "speed": 78,
        "moves": [
            {"name": "Hydro Pump", "power": 110, "move_type": "water"},
            {"name": "Ice Beam", "power": 90, "move_type": "ice"}
        ],
        "number": 9
    },
    "Chansey": {
        "name": "Chansey",
        "types": ["normal"],
        "hp": 250,
        "attack": 5,
        "defense": 5,
        "special_attack": 35,
        "special_defense": 105,
        "speed": 50,
        "moves": [
            {"name": "Soft-Boiled", "power": 0, "move_type": "normal"},
            {"name": "Toxic", "power": 0, "move_type": "poison"}
        ],
        "number": 113
    },
    "Garchomp": {
        "name": "Garchomp",
        "types": ["dragon", "ground"],
        "hp": 108,
        "attack": 130,
        "defense": 95,
        "special_attack": 80,
        "special_defense": 85,
        "speed": 102,
        "moves": [
            {"name": "Earthquake", "power": 100, "move_type": "ground"},
            {"name": "Dragon Claw", "power": 80, "move_type": "dragon"}
        ],
        "number": 445
    },
    "Lapras": {
        "name": "Lapras",
        "types": ["water", "ice"],
        "hp": 130,
        "attack": 85,
        "defense": 80,
        "special_attack": 85,
        "special_defense": 95,
        "speed": 60,
        "moves": [
            {"name": "Surf", "power": 90, "move_type": "water"},
            {"name": "Ice Beam", "power": 90, "move_type": "ice"}
        ],
        "number": 131
    },
    "Mewtwo": {
        "name": "Mewtwo",
        "types": ["psychic"],
        "hp": 106,
        "attack": 110,
        "defense": 90,
        "special_attack": 154,
        "special_defense": 90,
        "speed": 130,
        "moves": [
            {"name": "Psychic", "power": 90, "move_type": "psychic"},
            {"name": "Shadow Ball", "power": 80, "move_type": "ghost"}
        ],
        "number": 150
    },
    "Heracross": {
        "name": "Heracross",
        "types": ["bug", "fighting"],
        "hp": 80,
        "attack": 125,
        "defense": 75,
        "special_attack": 40,
        "special_defense": 95,
        "speed": 85,
        "moves": [
            {"name": "Megahorn", "power": 120, "move_type": "bug"},
            {"name": "Close Combat", "power": 120, "move_type": "fighting"}
        ],
        "number": 214
    },
    "Mawile": {
        "name": "Mawile",
        "types": ["steel", "fairy"],
        "hp": 50,
        "attack": 85,
        "defense": 85,
        "special_attack": 55,
        "special_defense": 55,
        "speed": 50,
        "moves": [
            {"name": "Iron Head", "power": 80, "move_type": "steel"},
            {"name": "Dazzling Gleam", "power": 80, "move_type": "fairy"}
        ],
        "number": 303
    },
    "Absol": {
        "name": "Absol",
        "types": ["dark"],
        "hp": 65,
        "attack": 130,
        "defense": 60,
        "special_attack": 75,
        "special_defense": 60,
        "speed": 75,
        "moves": [
            {"name": "Night Slash", "power": 70, "move_type": "dark"},
            {"name": "Sucker Punch", "power": 70, "move_type": "dark"}
        ],
        "number": 359
    },
    "Dragapult": {
        "name": "Dragapult",
        "types": ["dragon", "ghost"],
        "hp": 88,
        "attack": 120,
        "defense": 75,
        "special_attack": 100,
        "special_defense": 75,
        "speed": 142,
        "moves": [
            {"name": "Dragon Pulse", "power": 85, "move_type": "dragon"},
            {"name": "Phantom Force", "power": 90, "move_type": "ghost"}
        ],
        "number": 887
    },
    "Ampharos": {
        "name": "Ampharos",
        "types": ["electric"],
        "hp": 90,
        "attack": 75,
        "defense": 85,
        "special_attack": 115,
        "special_defense": 90,
        "speed": 55,
        "moves": [
            {"name": "Thunder", "power": 110, "move_type": "electric"},
            {"name": "Dragon Pulse", "power": 85, "move_type": "dragon"}
        ],
        "number": 181
    },
    "Nidoking": {
        "name": "Nidoking",
        "types": ["poison", "ground"],
        "hp": 81,
        "attack": 102,
        "defense": 77,
        "special_attack": 85,
        "special_defense": 75,
        "speed": 85,
        "moves": [
            {"name": "Earthquake", "power": 100, "move_type": "ground"},
            {"name": "Megahorn", "power": 120, "move_type": "bug"}
        ],
        "number": 34
    },
    "Noivern": {
        "name": "Noivern",
        "types": ["flying", "dragon"],
        "hp": 85,
        "attack": 70,
        "defense": 80,
        "special_attack": 97,
        "special_defense": 80,
        "speed": 123,
        "moves": [
            {"name": "Hurricane", "power": 110, "move_type": "flying"},
            {"name": "Dragon Pulse", "power": 85, "move_type": "dragon"}
        ],
        "number": 715
    },
    "Primarina": {
        "name": "Primarina",
        "types": ["water", "fairy"],
        "hp": 80,
        "attack": 74,
        "defense": 74,
        "special_attack": 126,
        "special_defense": 116,
        "speed": 60,
        "moves": [
            {"name": "Hydro Pump", "power": 110, "move_type": "water"},
            {"name": "Dazzling Gleam", "power": 80, "move_type": "fairy"}
        ],
        "number": 730
    },
    "Zoroark": {
        "name": "Zoroark",
        "types": ["dark"],
        "hp": 60,
        "attack": 105,
        "defense": 60,
        "special_attack": 120,
        "special_defense": 60,
        "speed": 105,
        "moves": [
            {"name": "Night Slash", "power": 70, "move_type": "dark"},
            {"name": "Shadow Ball", "power": 80, "move_type": "ghost"}
        ],
        "number": 571
    },
    "Aegislash": {
        "name": "Aegislash",
        "types": ["steel", "ghost"],
        "hp": 60,
        "attack": 50,
        "defense": 150,
        "special_attack": 50,
        "special_defense": 150,
        "speed": 60,
        "moves": [
            {"name": "Sacred Sword", "power": 90, "move_type": "fighting"},
            {"name": "Iron Head", "power": 80, "move_type": "steel"}
        ],
        "number": 681
    },
    "Dracovish": {
        "name": "Dracovish",
        "types": ["water", "dragon"],
        "hp": 90,
        "attack": 90,
        "defense": 100,
        "special_attack": 70,
        "special_defense": 80,
        "speed": 75,
        "moves": [
            {"name": "Fishious Rend", "power": 100, "move_type": "water"},
            {"name": "Dragon Pulse", "power": 85, "move_type": "dragon"}
        ],
        "number": 882
    },
    "Tyrantrum": {
        "name": "Tyrantrum",
        "types": ["rock", "dragon"],
        "hp": 82,
        "attack": 121,
        "defense": 119,
        "special_attack": 69,
        "special_defense": 59,
        "speed": 71,
        "moves": [
            {"name": "Dragon Claw", "power": 80, "move_type": "dragon"},
            {"name": "Rock Slide", "power": 100, "move_type": "rock"}
        ],
        "number": 697
    },
    "Snorlax": {
        "name": "Snorlax",
        "types": ["normal"],
        "hp": 160,
        "attack": 110,
        "defense": 65,
        "special_attack": 65,
        "special_defense": 110,
        "speed": 30,
        "moves": [
            {"name": "Body Slam", "power": 85, "move_type": "normal"},
            {"name": "Giga Impact", "power": 150, "move_type": "normal"}
        ],
        "number": 143
    },
    "Golem": {
        "name": "Golem",
        "types": ["rock", "ground"],
        "hp": 80,
        "attack": 120,
        "defense": 130,
        "special_attack": 55,
        "special_defense": 65,
        "speed": 45,
        "moves": [
            {"name": "Rock Slide", "power": 100, "move_type": "rock"},
            {"name": "Earthquake", "power": 100, "move_type": "ground"}
        ],
        "number": 76
    },
    "Weezing": {
        "name": "Weezing",
        "types": ["poison"],
        "hp": 65,
        "attack": 90,
        "defense": 120,
        "special_attack": 85,
        "special_defense": 70,
        "speed": 60,
        "moves": [
            {"name": "Sludge Bomb", "power": 90, "move_type": "poison"},
            {"name": "Flamethrower", "power": 110, "move_type": "fire"}
        ],
        "number": 110
    },
    "Machamp": {
        "name": "Machamp",
        "types": ["fighting"],
        "hp": 90,
        "attack": 130,
        "defense": 80,
        "special_attack": 65,
        "special_defense": 85,
        "speed": 55,
        "moves": [
            {"name": "Dynamic Punch", "power": 100, "move_type": "fighting"},
            {"name": "Ice Punch", "power": 75, "move_type": "ice"}
        ],
        "number": 68
    },
    "Weavile": {
        "name": "Weavile",
        "types": ["ice", "dark"],
        "hp": 70,
        "attack": 120,
        "defense": 65,
        "special_attack": 45,
        "special_defense": 85,
        "speed": 125,
        "moves": [
            {"name": "Ice Shard", "power": 40, "move_type": "ice"},
            {"name": "Night Slash", "power": 70, "move_type": "dark"}
        ],
        "number": 461
    },
    "Zapdos": {
        "name": "Zapdos",
        "types": ["electric", "flying"],
        "hp": 90,
        "attack": 90,
        "defense": 85,
        "special_attack": 125,
        "special_defense": 90,
        "speed": 100,
        "moves": [
            {"name": "Thunder", "power": 110, "move_type": "electric"},
            {"name": "Drill Peck", "power": 80, "move_type": "flying"}
        ],
        "number": 145
    },
    "Moltres": {
        "name": "Moltres",
        "types": ["fire", "flying"],
        "hp": 90,
        "attack": 100,
        "defense": 90,
        "special_attack": 125,
        "special_defense": 85,
        "speed": 90,
        "moves": [
            {"name": "Heat Wave", "power": 95, "move_type": "fire"},
            {"name": "Solar Beam", "power": 120, "move_type": "grass"}
        ],
        "number": 146
    },
    "Venusaur": {
        "name": "Venusaur",
        "types": ["grass", "poison"],
        "hp": 80,
        "attack": 82,
        "defense": 83,
        "special_attack": 100,
        "special_defense": 100,
        "speed": 80,
        "moves": [
            {"name": "Frenzy Plant", "power": 130, "move_type": "grass"},
            {"name": "Sludge Bomb", "power": 90, "move_type": "poison"}
        ],
        "number": 3
    }
}

PLAYER_SPRITES_FOLDER = os.path.join("sprites", "pokemon", "back")
OPPONENT_SPRITES_FOLDER = os.path.join("sprites", "pokemon")
def load_sprite(number, is_player=True):
    """Loads a sprite based on its number."""
    folder = PLAYER_SPRITES_FOLDER if is_player else OPPONENT_SPRITES_FOLDER
    path = os.path.join(folder, f"{number}.png")
    if os.path.exists(path):
        return pygame.image.load(path)
    else:
        print(f"❌ File not found: {path}")
        return None

class Pokemon:
    def __init__(self, name, types, hp, attack, defense, special_attack, special_defense, speed, number, moves, is_player=True):
        print(f"Creating {name} with {hp} HP")
        self.name = name
        self.types = types
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.number = number
        self.moves = [Move(**move) for move in moves]
        self.sprite = load_sprite(number, is_player)
        self.is_player = is_player

    def take_damage(self, damage):
        if damage > 0:
            self.hp = max(0, self.hp - damage)
            print(f"{self.name} takes {damage} damage! Remaining HP: {self.hp}/{self.max_hp}")
        else:
            print(f"{self.name} takes no damage!")

    def is_alive(self):
        return self.hp > 0

class Move:
    def __init__(self, name, power, move_type):
        self.name = name
        self.power = power
        self.move_type = move_type

    def __str__(self):
        return f"{self.name} (Type: {self.move_type}, Power: {self.power})"

class Battle:
    def __init__(self, player_pokemon, opponent_pokemon):
        self.player = player_pokemon
        self.opponent = opponent_pokemon
        self.move_choice = None
        self.turn = 0
        self.wait_timer = 0  # Added to handle timing without blocking

    def display_interface(self):
        screen.fill(WHITE)
        if self.player.sprite:
            screen.blit(self.player.sprite, (100, 400))
        display_text(f"{self.player.name} (HP: {self.player.hp}/{self.player.max_hp})", 100, 380)
        
        if self.opponent.sprite:
            screen.blit(self.opponent.sprite, (500, 100))
        display_text(f"{self.opponent.name} (HP: {self.opponent.hp}/{self.opponent.max_hp})", 500, 80)
        
        y = 500
        for i, move in enumerate(self.player.moves):
            display_text(f"{i + 1}. {move.name}", 100, y)
            y += 30
        
        for text_info in DAMAGE_TEXTS[:]:
            text, x, y, color, timer = text_info
            if timer > 0:
                display_text(text, x, y, color)
                text_info[4] -= 1
            else:
                DAMAGE_TEXTS.remove(text_info)
        
        for text_info in MESSAGE_TEXTS[:]:
            text, x, y, timer = text_info
            if timer > 0:
                display_text(text, x, y, GREEN)
                text_info[3] -= 1
            else:
                MESSAGE_TEXTS.remove(text_info)
        
        pygame.display.flip()

    def calculate_damage(self, attacker, defender, move):
        attack = attacker.attack
        defense = defender.defense
        multiplier = 1.0
        for defender_type in defender.types:
            multi = TYPE_ADVANTAGES.get(move.move_type, {}).get(defender_type, 1)
            multiplier *= multi
            if multi > 1:
                MESSAGE_TEXTS.append(["Super effective!", 300, 300, 60])
        
        damage = (((2 * 50 / 5 + 2) * attack * move.power / defense) / 50 + 2) * multiplier
        return max(1, int(damage))

    def execute_turn(self, attacker, defender, move, x_pos, y_pos):
        damage = self.calculate_damage(attacker, defender, move)
        defender.take_damage(damage)
        DAMAGE_TEXTS.append([f"-{damage}", x_pos, y_pos, RED, 60])
        self.wait_timer = 30  # Set a wait period (1 second at 30 FPS)

    def start_battle(self):
        print(f"\n⚔️ Battle start: {self.player.name} VS {self.opponent.name}!")
        
        while self.player.is_alive() and self.opponent.is_alive():
            self.display_interface()
            
            # Handle wait timer
            if self.wait_timer > 0:
                self.wait_timer -= 1
                clock.tick(30)
                continue

            # Determine turn order
            if self.player.speed >= self.opponent.speed:
                first = self.player
                second = self.opponent
                first_pos = (100, 400)
                second_pos = (500, 100)
            else:
                first = self.opponent
                second = self.player
                first_pos = (500, 100)
                second_pos = (100, 400)

            # Handle input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and self.move_choice is None:
                    if event.key == pygame.K_1 and len(self.player.moves) >= 1:
                        self.move_choice = 0
                    elif event.key == pygame.K_2 and len(self.player.moves) >= 2:
                        self.move_choice = 1

            # Execute turns
            if self.turn == 0:  # First Pokémon's turn
                if first == self.player and self.move_choice is not None:
                    move = first.moves[self.move_choice]
                    self.execute_turn(first, second, move, second_pos[0], second_pos[1])
                    self.move_choice = None
                    self.turn = 1
                elif first == self.opponent:
                    move = random.choice(first.moves)
                    self.execute_turn(first, second, move, second_pos[0], second_pos[1])
                    self.turn = 1

            elif self.turn == 1 and second.is_alive():  # Second Pokémon's turn
                if second == self.player and self.move_choice is not None:
                    move = second.moves[self.move_choice]
                    self.execute_turn(second, first, move, first_pos[0], first_pos[1])
                    self.move_choice = None
                    self.turn = 0
                elif second == self.opponent:
                    move = random.choice(second.moves)
                    self.execute_turn(second, first, move, first_pos[0], first_pos[1])
                    self.turn = 0

            # Check for victory
            if not self.opponent.is_alive():
                print(f"🏆 {self.player.name} has won!")
                display_victory_message()
                return
            if not self.player.is_alive():
                print(f"💀 {self.player.name} has lost the battle...")
                display_defeat_message()
                return

            clock.tick(30)

def display_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def display_victory_message():
    screen.fill(WHITE)
    display_text("🏆 You have won!", 250, 250, GREEN)
    pygame.display.flip()
    pygame.time.wait(3000)

def display_defeat_message():
    screen.fill(WHITE)
    display_text("💀 You have lost...", 250, 250, RED)
    pygame.display.flip()
    pygame.time.wait(3000)

def display_menu():
    screen.fill(WHITE)
    display_text("🌟 MAIN MENU 🌟", 250, 50)
    display_text("1. Start a battle", 250, 150)
    display_text("2. Quit", 250, 200)
    pygame.display.flip()

def main():
    while True:
        display_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pokemon_list = list(POKEMON_LIST.values())
                    player = Pokemon(**random.choice(pokemon_list), is_player=True)
                    opponent = Pokemon(**random.choice(pokemon_list), is_player=False)
                    battle = Battle(player, opponent)
                    battle.start_battle()
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()
        clock.tick(30)

if __name__ == "__main__":
    main()