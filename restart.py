import json
import pygame
from window import Window
from pokemon import Pokemon


class Restart:
    def __init__(self):
        """Initializes the Restart class and sets up starter Pokémon options."""
        self.window = Window()
        self.starter = ["1", "4", "7"]  # Starter Pokémon options

    def draw(self):
        """Draws the background and starter Pokémon choices on the screen."""
        self.window.screen.blit(self.window.MENU_BACKGROUND, (0, 0))
        self.window.draw_menu_pokemon(self.starter[0], *self.first_starter_rect.topleft)
        self.window.draw_menu_pokemon(self.starter[1], *self.second_starter_rect.topleft)
        self.window.draw_menu_pokemon(self.starter[2], *self.third_starter_rect.topleft)

    def selection(self):
        """Handles user selection of a starter Pokémon using mouse clicks."""
        # Define the positions and sizes of the Pokémon options
        self.first_starter_rect = pygame.Rect(
            self.window.SCREEN_WIDTH / 4 - self.window.SPRITE_WIDTH / 2,
            self.window.SCREEN_HEIGHT / 2 - self.window.SPRITE_HEIGHT / 2,
            self.window.SPRITE_WIDTH, self.window.SPRITE_HEIGHT
        )
        self.second_starter_rect = pygame.Rect(
            self.window.SCREEN_WIDTH / 2 - self.window.SPRITE_WIDTH / 2,
            self.window.SCREEN_HEIGHT / 2 - self.window.SPRITE_HEIGHT / 2,
            self.window.SPRITE_WIDTH, self.window.SPRITE_HEIGHT
        )
        self.third_starter_rect = pygame.Rect(
            self.window.SCREEN_WIDTH - self.window.SCREEN_WIDTH / 4 - self.window.SPRITE_WIDTH / 2,
            self.window.SCREEN_HEIGHT / 2 - self.window.SPRITE_HEIGHT / 2,
            self.window.SPRITE_WIDTH, self.window.SPRITE_HEIGHT
        )

        # Get mouse position for click detection
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Event handling loop for mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if any starter Pokémon is clicked
                if self.first_starter_rect.collidepoint((mouse_x, mouse_y)):
                    self.my_pokemon = Pokemon(self.starter[0])  # Choose first starter
                    self.save_my_pokemon()
                    self.state = "start"
                elif self.second_starter_rect.collidepoint((mouse_x, mouse_y)):
                    self.my_pokemon = Pokemon(self.starter[1])  # Choose second starter
                    self.save_my_pokemon()
                    self.state = "start"
                elif self.third_starter_rect.collidepoint((mouse_x, mouse_y)):
                    self.my_pokemon = Pokemon(self.starter[2])  # Choose third starter
                    self.save_my_pokemon()
                    self.state = "start"

        return self.state
    
    def save_my_pokemon(self):
        """Saves the chosen Pokémon's data to a JSON file."""
        with open("my_pokemon.json", "w") as file:
            json.dump(self.my_pokemon.to_dict(), file, indent=4)

    def restart(self, state):
        """Handles the restart process by calling selection and drawing methods."""
        self.state = state
        self.state = self.selection()
        self.draw()
        return self.state
