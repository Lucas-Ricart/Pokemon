import pygame
import pygame.freetype


class Window:
    """class to define the window, to link : window.screen"""

    def __init__(self):
        # color
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.PURPLE = (54, 45, 92)
        self.PINK = (162, 92, 126)

        # text font
        self.font = pygame.font.Font("assets/pokemon-font.ttf", 60)

        # game window
        self.screen_width = 854
        self.screen_height = 480

        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))

    def draw_topleft_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw_topright_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        rect = img.get_rect(topright=(x, y))
        self.screen.blit(img, rect)

    def draw_bottomright_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        rect = img.get_rect(bottomright=(x, y))
        self.screen.blit(img, rect)

    def draw_bottomleft_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        rect = img.get_rect(bottomleft=(x, y))
        self.screen.blit(img, rect)

    def draw_center_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        rect = img.get_rect(center=(x, y))
        self.screen.blit(img, rect)
