import pygame
from window import Window


class GameMenu:
    def __init__(self):
        self.WINDOW = Window()
        self.FIGHT_TEXT_BUTTON = "FIGHT"
        self.TEAM_TEXT_BUTTON = "TEAM"
        self.POKEDEX_TEXT_BUTTON = "POKEDEX"
        self.QUIT_TEXT_BUTTON = "QUIT"

    def draw(self):
        self.WINDOW.screen.blit(self.WINDOW.MENU_BACKGROUND, (0, 0))
        self.WINDOW.draw_menu_button(self.FIGHT_TEXT_BUTTON,
                                     self.WINDOW.screen_width/4, 160)
        self.WINDOW.draw_menu_button(self.TEAM_TEXT_BUTTON,
                                     self.WINDOW.screen_width/4 + self.WINDOW.screen_width/2, 160)
        self.WINDOW.draw_menu_button(self.POKEDEX_TEXT_BUTTON,
                                     self.WINDOW.screen_width/4, self.WINDOW.screen_height - 160)
        self.WINDOW.draw_menu_button(self.QUIT_TEXT_BUTTON,
                                     self.WINDOW.screen_width/4 + self.WINDOW.screen_width/2, self.WINDOW.screen_height - 160)

    def selection(self):
        # def button as rectangles
        fight_button = pygame.Rect(
            self.WINDOW.screen_width / 4 - self.WINDOW.MENU_BUTTON_WIDTH / 2,
            160 - self.WINDOW.MENU_BUTTON_HEIGHT / 2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )

        team_button = pygame.Rect(
            self.WINDOW.screen_width / 4 + self.WINDOW.screen_width /
            2 - self.WINDOW.MENU_BUTTON_WIDTH / 2,
            160 - self.WINDOW.MENU_BUTTON_HEIGHT / 2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )

        pokedex_button = pygame.Rect(
            self.WINDOW.screen_width / 4 - self.WINDOW.MENU_BUTTON_WIDTH / 2,
            self.WINDOW.screen_height - 160 - self.WINDOW.MENU_BUTTON_HEIGHT / 2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )

        quit_button = pygame.Rect(
            self.WINDOW.screen_width / 4 + self.WINDOW.screen_width /
            2 - self.WINDOW.MENU_BUTTON_WIDTH / 2,
            self.WINDOW.screen_height - 160 - self.WINDOW.MENU_BUTTON_HEIGHT / 2,
            self.WINDOW.MENU_BUTTON_WIDTH, self.WINDOW.MENU_BUTTON_HEIGHT
        )

        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fight_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "fight"
                if team_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "team"
                if pokedex_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "pokedex"
                if quit_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "false"
        return self.state
    
    def game_menu(self, state):
        self.draw()
        self.state = state
        self.state = self.selection()
        return self.state
