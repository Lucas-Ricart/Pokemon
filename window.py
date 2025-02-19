import pygame
import pygame.freetype


class Window:
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

    # menu
        self.MENU_BACKGROUND = pygame.image.load("assets/menu-background.png")
        self.MENU_BACKGROUND = pygame.transform.scale(
            self.MENU_BACKGROUND, (self.screen_width, self.screen_height))
        self.MENU_BUTTON_WIDTH, self.MENU_BUTTON_HEIGHT = 200, 60

    def draw_menu_button(self, text, x, y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button = pygame.Rect(
            x-self.MENU_BUTTON_WIDTH/2, y-self.MENU_BUTTON_HEIGHT/2+1.5, self.MENU_BUTTON_WIDTH, self.MENU_BUTTON_HEIGHT)
        if button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(self.screen,
                             self.PURPLE, button)
            pygame.draw.rect(self.screen,
                             self.PINK, button, 3)
        else:
            pygame.draw.rect(self.screen, self.RED, button)
            pygame.draw.rect(self.screen,
                             self.BLACK, button, 3)
        self.draw_center_text(
            text, self.font, self.WHITE, x, y)

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
