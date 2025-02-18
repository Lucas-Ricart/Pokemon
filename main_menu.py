import pygame
from window import Window


class MainMenu:
    def __init__(self):
        self.WINDOW = Window()
        self.BACKGROUND = pygame.image.load("assets/menu-background.png")
        self.BACKGROUND = pygame.transform.scale(
            self.BACKGROUND, (self.WINDOW.screen_width, self.WINDOW.screen_height))
        self.TITTLE = pygame.image.load("assets/tittle.png")
        self.BUTTON_WIDTH, self.BUTTON_HEIGHT = 200, 60
        self.FIRST_TEXT_BUTTON = "CONTINUE"
        self.SECOND_TEXT_BUTTON = "RESTART"
        self.THIRD_TEXT_BUTTON = "QUIT"

    def draw_menu_button(self, text, x, y):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button = pygame.Rect(
            x-self.BUTTON_WIDTH/2, y-self.BUTTON_HEIGHT/2+1.5, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        if button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(self.WINDOW.screen,
                             self.WINDOW.PURPLE, button)
            pygame.draw.rect(self.WINDOW.screen,
                             self.WINDOW.PINK, button, 3)
        else:
            pygame.draw.rect(self.WINDOW.screen, self.WINDOW.RED, button)
            pygame.draw.rect(self.WINDOW.screen,
                             self.WINDOW.BLACK, button, 3)
        self.WINDOW.draw_center_text(
            text, self.WINDOW.font, self.WINDOW.WHITE, x, y)

    def draw(self):
        self.WINDOW.screen.blit(self.BACKGROUND, (0, 0))
        self.WINDOW.screen.blit(
            self.TITTLE, (self.WINDOW.screen_width/2-200, 5))
        self.draw_menu_button(self.FIRST_TEXT_BUTTON,
                              self.WINDOW.screen_width/2, self.WINDOW.screen_height/2-40)
        self.draw_menu_button(self.SECOND_TEXT_BUTTON,
                              self.WINDOW.screen_width/2, self.WINDOW.screen_height/2+60)
        self.draw_menu_button(self.THIRD_TEXT_BUTTON,
                              self.WINDOW.screen_width/2, self.WINDOW.screen_height/2+160)

    def selection(self):
        # def button as rectangles
        continue_button = pygame.Rect(
            self.WINDOW.screen_width/2 - self.BUTTON_WIDTH/2,
            self.WINDOW.screen_height/2 - 40 - self.BUTTON_HEIGHT/2,
            self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        restart_button = pygame.Rect(
            self.WINDOW.screen_width/2 - self.BUTTON_WIDTH/2,
            self.WINDOW.screen_height/2 + 60 - self.BUTTON_HEIGHT/2,
            self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        quit_button = pygame.Rect(
            self.WINDOW.screen_width/2 - self.BUTTON_WIDTH/2,
            self.WINDOW.screen_height/2 + 160 - self.BUTTON_HEIGHT/2,
            self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if continue_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "continue"
                elif restart_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "restart"
                elif quit_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "false"
        return self.state

    def main_menu(self, state):
        self.draw()
        self.state = state
        self.state = self.selection()
        return self.state