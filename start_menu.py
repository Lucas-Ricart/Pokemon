import pygame
from window import Window


class StartMenu:
    def __init__(self):
        self.WINDOW = Window()
        self.TITTLE = pygame.image.load("assets/tittle.png")
        self.CONTINUE_TEXT_BUTTON = "CONTINUE"
        self.RESTART_TEXT_BUTTON = "RESTART"
        self.QUIT_TEXT_BUTTON = "QUIT"

    def draw(self):
        self.WINDOW.screen.blit(self.WINDOW.MENU_BACKGROUND, (0, 0))
        self.WINDOW.screen.blit(
            self.TITTLE, (self.WINDOW.screen_width/2-200, 5))
        self.WINDOW.draw_menu_button(self.CONTINUE_TEXT_BUTTON,
                                     self.WINDOW.screen_width/2, self.WINDOW.screen_height/2-40)
        self.WINDOW.draw_menu_button(self.RESTART_TEXT_BUTTON,
                                     self.WINDOW.screen_width/2, self.WINDOW.screen_height/2+60)
        self.WINDOW.draw_menu_button(self.QUIT_TEXT_BUTTON,
                                     self.WINDOW.screen_width/2, self.WINDOW.screen_height/2+160)

    def selection(self):
        # def button as rectangles
        continue_button = pygame.Rect(
            self.WINDOW.screen_width/2 - self.WINDOW.MENU_BUTTON_WIDTH/2,
            self.WINDOW.screen_height/2 - 40 - self.WINDOW.MENU_BUTTON_HEIGHT/2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )
        restart_button = pygame.Rect(
            self.WINDOW.screen_width/2 - self.WINDOW.MENU_BUTTON_WIDTH/2,
            self.WINDOW.screen_height/2 + 60 - self.WINDOW.MENU_BUTTON_HEIGHT/2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )
        quit_button = pygame.Rect(
            self.WINDOW.screen_width/2 - self.WINDOW.MENU_BUTTON_WIDTH/2,
            self.WINDOW.screen_height/2 + 160 - self.WINDOW.MENU_BUTTON_HEIGHT/2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )

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

    def start_menu(self, state):
        self.draw()
        self.state = state
        self.state = self.selection()
        return self.state
