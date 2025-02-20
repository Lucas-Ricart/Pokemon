import pygame
from window import Window


class Fight:
    def __init__(self):
        self.window = Window()
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

    # Draw lv
    def draw_enemy_lv(self):
        # Draw enemy lv
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 247, 92)
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.DARK_GREY, 245, 90)

    def draw_my_lv(self):
        # Draw my lv
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 701, 251)
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.DARK_GREY, 699, 249)

    def draw_my_hp(self):
        # Draw my hp
        # Draw hp max
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 673, 299)
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.DARK_GREY, 671, 297)
        # Draw current hp
        self.window.draw_bottomright_text(
            "83", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 649, 299)
        self.window.draw_bottomright_text(
            "83", self.window.NUMBER_FONT, self.window.DARK_GREY, 647, 297)

    # Draw hp bar
    def draw_enemy_bar(self):
        # Draw enemy hp bar
        pygame.draw.line(self.window.screen, self.window.LIGHT_ORANGE,
                         (148, 106), (288, 106), width=8)

    def draw_my_bar(self):
        # Draw my hp bar
        pygame.draw.line(self.window.screen, self.window.DARK_ORANGE,
                         (599, 264), (743, 264), width=7)

    def draw_xp_bar(self):
        # Draw xp bar
        pygame.draw.line(self.window.screen, self.window.BLUE,
                         (454, 304), (743, 304), width=5)

    # Draw names
    def draw_enemy_name(self):
        # Draw enemy name
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 16, 96)
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.TEXT_FONT, self.window.DARK_GREY, 14, 94)

    def draw_my_name(self):
        # Draw my name
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 447, 258)
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.TEXT_FONT, self.window.DARK_GREY, 445, 256)

    def draw_fight(self, test):
        self.window.draw_fight_decor()
        self.draw_enemy_lv()
        self.draw_enemy_bar()
        self.draw_enemy_name()
        self.draw_my_lv()
        self.draw_my_bar()
        self.draw_my_name()
        self.draw_my_hp()
        self.draw_xp_bar()
        mouse_x, mouse_y = "lol", "lol"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
        return (mouse_x, mouse_y)
