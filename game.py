import pygame
from start_menu import StartMenu
from game_menu import GameMenu
from fight import Fight
from restart import Restart

# Initialize Pygame and clock
pygame.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        """
        Initializes the Game class with menus, state, and clock settings.
        """
        # Initialize menus
        self.start_menu = StartMenu()
        self.game_menu = GameMenu()
        self.restart = Restart()

        # Initialize fight
        self.fight = Fight()

        # Game state and control variables
        self.run = True
        self.state = "start_menu"

        # Frame rate settings
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def game(self):
        """
        Main game loop that manages different game states and updates the display.
        """
        while self.run:
            # Set frame rate
            self.clock.tick(self.FPS)

            # Handle start menu state
            if self.state == "start_menu":
                self.state = self.start_menu.start_menu(self.state)

            # Handle game exit state
            if self.state == "false":
                pygame.quit()

            # Handle game continuation state (game menu)
            if self.state == "continue":
                self.state = self.game_menu.game_menu(self.state)

            # Handle restart state
            if self.state == "restart":
                self.state = self.restart.restart(self.state)

            # Handle fight state
            if self.state == "fight":
                # Initialize my Pokemon if not already loaded
                if not self.fight.my_pokemon:
                    self.fight.load_my_pokemon()
                # Initialize enemy Pokemon if not already loaded
                if not self.fight.enemy_pokemon:
                    self.fight.new_enemy()
                self.state = self.fight.fight(self.state)

            # Handle victory state
            if self.state == "victory":
                self.state = self.fight.victory(self.state)

            # Handle loss state
            if self.state == "loose":
                self.state = self.fight.loose(self.state)

            # Update the display
            pygame.display.update()

        # Quit Pygame when the game loop ends
        pygame.quit()
