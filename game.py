import pygame
from start_menu import StartMenu
from game_menu import GameMenu

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

            # Handle main menu state
            if self.state == "start_menu":
                self.state = self.start_menu.start_menu(self.state)

            # Handle game exit state
            if self.state == "false":
                pygame.quit()

            # Handle game continuation state
            if self.state == "continue":
                self.state = self.game_menu.game_menu(self.state)

            # Update the display
            pygame.display.update()

        # Quit Pygame when the game loop ends
        pygame.quit()