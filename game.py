import pygame
from main_menu import MainMenu

pygame.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.main_menu = MainMenu()
        self.run = True
        self.state = "main_menu"
        self.FPS = 60
        self.clock = pygame.time.Clock()

    def game(self):
        while self.run:
            self.clock.tick(self.FPS)
            if self.state == "main_menu":
                self.state = self.main_menu.main_menu(self.state)
            if self.state == "false":
                pygame.quit()
            pygame.display.update()

        pygame.quit()
