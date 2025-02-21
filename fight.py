import json
import pygame
import random
from window import Window
from pokemon import Pokemon
from restart import Restart


class Fight:
    def __init__(self):
        self.window = Window()
        self.enemy_pokemon = None
        self.my_pokemon = None
        self.restart = Restart
        # Constants for type advantages in battles
        with open("types.json", "r") as file:
            self.TYPE_ADVANTAGES = json.load(file)
        self.ATTACK_TEXT = "ATTACK"
        self.CONTINUE_TEXT = "CONTINUE"

    def load_my_pokemon(self):
        with open("my_pokemon.json", "r") as file:
            self.my_pokemon = json.load(file)
        self.my_pokemon = Pokemon(self.my_pokemon["key"])

    def save_my_pokemon(self):
        with open("my_pokemon.json", "w") as file:
            json.dump(self.my_pokemon.to_dict(), file, indent=4)

    def get_random_enabled_pokemon(self):
        self.list_pokemon = Pokemon()
        enabled_pokemons = [
            p for p in self.list_pokemon.list_pokemon.values() if p["enable"] == "true"]
        return random.choice(enabled_pokemons) if enabled_pokemons else None

    def new_enemy(self):
        random_pokemon = self.get_random_enabled_pokemon()
        self.enemy_pokemon = Pokemon(str(random_pokemon["id"]), random.randint(
            self.my_pokemon.level-3, self.my_pokemon.level+3))

    def fight(self, state):
        self.state = state
        self.draw_fight()
        self.window.draw_fight_button(
            self.ATTACK_TEXT, self.window.SCREEN_WIDTH - self.window.MENU_BUTTON_WIDTH, self.window.ARENA_HEIGHT)
        button = pygame.Rect(
            self.window.SCREEN_WIDTH - self.window.MENU_BUTTON_WIDTH,
            self.window.ARENA_HEIGHT,
            self.window.MENU_BUTTON_WIDTH,
            self.window.TEXTBOX_HEIGHT
        )

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button is clicked
                if button.collidepoint((mouse_x, mouse_y)):
                    self.battle()
                    if self.enemy_pokemon.current_hp <= 0:
                        self.state = "victory"
                    elif self.my_pokemon.current_hp <= 0:
                        self.state = "loose"
        return self.state

    def victory(self, state):
        self.state = state
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button = pygame.Rect(
            self.window.SCREEN_WIDTH - self.window.MENU_BUTTON_WIDTH,
            self.window.ARENA_HEIGHT,
            self.window.MENU_BUTTON_WIDTH,
            self.window.TEXTBOX_HEIGHT
        )
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button is clicked
                if button.collidepoint((mouse_x, mouse_y)):
                    self.state = "continue"
        self.draw_fight()
        self.my_pokemon.add_xp(
            self.enemy_pokemon.level, self.enemy_pokemon.base_xp)
        self.my_pokemon.current_hp = self.my_pokemon.max_hp
        self.save_my_pokemon()
        self.draw_victory()
        self.window.draw_fight_button(self.CONTINUE_TEXT, self.window.TEXTBOX_HEIGHT,
                                      self.window.SCREEN_WIDTH - self.window.MENU_BUTTON_WIDTH)
        return self.state

    def loose(self, state):
        self.state = state
        self.draw_fight()
        self.my_pokemon.add_xp(
            self.enemy_pokemon.level, self.enemy_pokemon.base_xp)
        self.my_pokemon.current_hp = self.my_pokemon.max_hp
        self.save_my_pokemon()
        self.draw_victory()
        self.window.draw_fight_button(self.CONTINUE_TEXT, self.window.TEXTBOX_HEIGHT,
                                      self.window.SCREEN_WIDTH - self.window.MENU_BUTTON_WIDTH)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button = pygame.Rect(
            self.window.SCREEN_WIDTH - self.window.MENU_BUTTON_WIDTH,
            self.window.ARENA_HEIGHT,
            self.window.MENU_BUTTON_WIDTH,
            self.window.TEXTBOX_HEIGHT
        )
        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button is clicked
                if button.collidepoint((mouse_x, mouse_y)):
                    self.state = "start_menu"
        return self.state

    def battle(self):
        """
        Starts the battle and alternates turns based on speed.
        After a win, the player is offered the chance to capture the opponent's Pokémon.
        :param team: The player's team.
        """
        # Determine who attacks first (the faster Pokémon)
        if self.my_pokemon.speed >= self.enemy_pokemon.speed:
            self.my_turn()
            if self.enemy_pokemon.current_hp <= 0:
                return self.enemy_pokemon.current_hp, self.my_pokemon.current_hp
            self.enemy_turn()
        else:
            self.enemy_turn()
            if self.my_pokemon.current_hp <= 0:
                return self.enemy_pokemon.current_hp, self.my_pokemon.current_hp
            self.my_turn()
        return self.enemy_pokemon.current_hp, self.my_pokemon.current_hp

    def my_turn(self):
        """
        The attacking Pokémon takes its turn.
        """
        self.attacker = self.my_pokemon
        self.defender = self.enemy_pokemon
        damage = self.calculate_damage()
        self.enemy_pokemon.current_hp -= damage

    def enemy_turn(self):
        self.attacker = self.enemy_pokemon
        self.defender = self.my_pokemon
        damage = self.calculate_damage()
        self.my_pokemon.current_hp -= damage

    def calculate_damage(self):
        """
        Calculates the damage dealt based on attack, types, and defense.
        """
        # Type modifier (advantages/disadvantages)
        type_multiplier = 1
        for attacker_type in self.attacker.type:
            for defender_type in self.defender.type:
                if attacker_type in self.TYPE_ADVANTAGES and defender_type in self.TYPE_ADVANTAGES[attacker_type]:
                    type_multiplier *= self.TYPE_ADVANTAGES[attacker_type][defender_type]
        fail = 1
        fail = 0 if random.random() < 0.001 else 1
        if self.attacker.attack > self.attacker.special_attack:
            base_damage = (
                (self.attacker.attack * type_multiplier * fail) - self.defender.defense)
        else:
            base_damage = ((self.attacker.special_attack *
                            type_multiplier * fail) - self.defender.special_defense)
            final_damage = max(2, int(base_damage))
        return int(final_damage)

    # Draw lv
    def draw_enemy_lv(self):
        # Draw enemy lv
        self.window.draw_bottomleft_text(
            f"{self.enemy_pokemon.level}", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 247, 92)
        self.window.draw_bottomleft_text(
            f"{self.enemy_pokemon.level}", self.window.NUMBER_FONT, self.window.DARK_GREY, 245, 90)

    def draw_my_lv(self):
        # Draw my lv
        self.window.draw_bottomleft_text(
            f"{self.my_pokemon.level}", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 701, 251)
        self.window.draw_bottomleft_text(
            f"{self.my_pokemon.level}", self.window.NUMBER_FONT, self.window.DARK_GREY, 699, 249)

    def draw_my_hp(self):
        # Draw my hp
        # Draw hp max
        self.window.draw_bottomleft_text(
            f"{self.my_pokemon.max_hp}", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 673, 299)
        self.window.draw_bottomleft_text(
            f"{self.my_pokemon.max_hp}", self.window.NUMBER_FONT, self.window.DARK_GREY, 671, 297)
        # Draw current hp
        self.window.draw_bottomright_text(
            f"{self.my_pokemon.current_hp}", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 649, 299)
        self.window.draw_bottomright_text(
            f"{self.my_pokemon.current_hp}", self.window.NUMBER_FONT, self.window.DARK_GREY, 647, 297)

    # Draw hp bar
    def draw_enemy_hp_bar(self):
        # Draw enemy hp bar
        percent_remaining = (self.enemy_pokemon.current_hp /
                             self.enemy_pokemon.max_hp) * 100
        dif = 140
        if percent_remaining > 50:
            color = self.window.GREEN
        elif percent_remaining < 5:
            color = self.window.DARK_ORANGE
        else:
            color = self.window.LIGHT_ORANGE
        pygame.draw.line(self.window.screen, color,
                         (148, 106), (148+(dif*percent_remaining)/100, 106), width=8)

    def draw_my_hp_bar(self):
        # Draw my hp bar
        percent_remaining = (self.my_pokemon.current_hp /
                             self.my_pokemon.max_hp) * 100
        dif = 144
        pygame.draw.line(self.window.screen, self.window.DARK_ORANGE,
                         (599, 264), (599+(dif*percent_remaining)/100, 264), width=7)

    def draw_xp_bar(self):
        # Draw xp bar
        pygame.draw.line(self.window.screen, self.window.BLUE,
                         (454, 304), (743, 304), width=5)

    # Draw names
    def draw_enemy_name(self):
        # Draw enemy name
        self.window.draw_bottomleft_text(
            f"{self.enemy_pokemon.name}", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 16, 96)
        self.window.draw_bottomleft_text(
            f"{self.enemy_pokemon.name}", self.window.TEXT_FONT, self.window.DARK_GREY, 14, 94)

    def draw_my_name(self):
        # Draw my name
        self.window.draw_bottomleft_text(
            f"{self.my_pokemon.name}", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 447, 258)
        self.window.draw_bottomleft_text(
            f"{self.my_pokemon.name}", self.window.TEXT_FONT, self.window.DARK_GREY, 445, 256)

    def draw_victory(self):
        # Draw my name
        self.window.draw_topleft_text(
            f"{self.enemy_pokemon.name} est KO.", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 27, self.window.ARENA_HEIGHT + 22)
        self.window.draw_topleft_text(
            f"{self.enemy_pokemon.name} est KO.", self.window.TEXT_FONT, self.window.DARK_GREY, 25, self.window.ARENA_HEIGHT + 20)

    def draw_loose(self):
        # Draw my name
        self.window.draw_topleft_text(
            f"{self.my_pokemon.name} est KO.", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 27, self.window.ARENA_HEIGHT + 22)
        self.window.draw_topleft_text(
            f"{self.my_pokemon.name} est KO.", self.window.TEXT_FONT, self.window.DARK_GREY, 25, self.window.ARENA_HEIGHT + 20)

    def draw_fight(self):
        self.window.draw_fight_decor()
        self.window.draw_pokemons(self.my_pokemon.id, self.enemy_pokemon.id)
        self.window.screen.blit(self.window.TEXT_BOX_BACKGROUND,
                                (0, self.window.SCREEN_HEIGHT - self.window.TEXTBOX_HEIGHT))
        self.draw_enemy_lv()
        self.draw_enemy_hp_bar()
        self.draw_enemy_name()
        self.draw_my_lv()
        self.draw_my_hp_bar()
        self.draw_my_name()
        self.draw_my_hp()
        self.draw_xp_bar()
