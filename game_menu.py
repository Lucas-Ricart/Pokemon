import pygame
from window import Window


class GameMenu:
    def __init__(self):
        # Initialize window and button labels
        self.window = Window()
        self.fight_text_button = "FIGHT"
        self.team_text_button = "TEAM"
        self.pokedex_text_button = "POKEDEX"
        self.quit_text_button = "QUIT"

    def draw(self):
        # Draw the background
        self.window.screen.blit(self.window.MENU_BACKGROUND, (0, 0))

        # Draw the menu buttons
        self.window.draw_menu_button(
            self.fight_text_button,
            self.window.SCREEN_WIDTH / 4,
            160
        )
        self.window.draw_menu_button(
            self.team_text_button,
            self.window.SCREEN_WIDTH / 4 + self.window.SCREEN_WIDTH / 2,
            160
        )
        self.window.draw_menu_button(
            self.pokedex_text_button,
            self.window.SCREEN_WIDTH / 4,
            self.window.SCREEN_HEIGHT - 160
        )
        self.window.draw_menu_button(
            self.quit_text_button,
            self.window.SCREEN_WIDTH / 4 + self.window.SCREEN_WIDTH / 2,
            self.window.SCREEN_HEIGHT - 160
        )

    def selection(self):
        # Define buttons as rectangles for collision detection
        fight_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 4 - self.window.MENU_BUTTON_WIDTH / 2,
            160 - self.window.MENU_BUTTON_HEIGHT / 2,
            self.window.MENU_BUTTON_WIDTH, self.window.MENU_BUTTON_HEIGHT
        )

        team_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 4 + self.window.SCREEN_WIDTH / 2 - self.window.MENU_BUTTON_WIDTH / 2,
            160 - self.window.MENU_BUTTON_HEIGHT / 2,
            self.window.MENU_BUTTON_WIDTH, self.window.MENU_BUTTON_HEIGHT
        )

        pokedex_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 4 - self.window.MENU_BUTTON_WIDTH / 2,
            self.window.SCREEN_HEIGHT - 160 - self.window.MENU_BUTTON_HEIGHT / 2,
            self.window.MENU_BUTTON_WIDTH, self.window.MENU_BUTTON_HEIGHT
        )

        quit_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 4 + self.window.SCREEN_WIDTH / 2 - self.window.MENU_BUTTON_WIDTH / 2,
            self.window.SCREEN_HEIGHT - 160 - self.window.MENU_BUTTON_HEIGHT / 2,
            self.window.MENU_BUTTON_WIDTH, self.window.MENU_BUTTON_HEIGHT
        )

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = "false"  # Quit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button is clicked
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
        # Draw the menu and check for selection
        self.draw()
        self.state = state
        self.state = self.selection()
        return self.state