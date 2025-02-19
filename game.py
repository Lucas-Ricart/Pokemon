import pygame
from start_menu import StartMenu
from game_menu import GameMenu

pygame.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.start_menu = StartMenu()
        self.game_menu = GameMenu()
        self.run = True
        self.state = "main_menu"
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def game(self):
        while self.run:
            self.clock.tick(self.FPS)
            if self.state == "main_menu":
                self.state = self.start_menu.start_menu(self.state)
            if self.state == "false":
                pygame.quit()
            if self.state == "continue":
                self.state = self.game_menu.game_menu(self.state)
            pygame.display.update()

        pygame.quit()
