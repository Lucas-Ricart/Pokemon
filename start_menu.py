import pygame
from window import Window


class StartMenu:
    def __init__(self):
        # Initialize window and assets
        self.window = Window()
        self.tittle = pygame.image.load("assets/tittle.png")
        self.continue_text_button = "CONTINUE"
        self.restart_text_button = "RESTART"
        self.quit_text_button = "QUIT"

    def draw(self):
        # Draw the background and title
        self.window.screen.blit(self.window.MENU_BACKGROUND, (0, 0))
        self.window.screen.blit(
            self.tittle, (self.window.SCREEN_WIDTH / 2 - 200, 5))

        # Draw menu buttons
        self.window.draw_menu_button(
            self.continue_text_button,
            self.window.SCREEN_WIDTH / 2,
            200
        )
        self.window.draw_menu_button(
            self.restart_text_button,
            self.window.SCREEN_WIDTH / 2,
            285
        )
        self.window.draw_menu_button(
            self.quit_text_button,
            self.window.SCREEN_WIDTH / 2,
            370
        )

    def selection(self):
        # Define buttons as rectangles for collision detection
        continue_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 2 - self.window.MENU_BUTTON_WIDTH / 2,
            200 - self.window.MENU_BUTTON_HEIGHT / 2,
            self.window.MENU_BUTTON_WIDTH, self.window.MENU_BUTTON_HEIGHT
        )
        restart_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 2 - self.window.MENU_BUTTON_WIDTH / 2,
            285 - self.window.MENU_BUTTON_HEIGHT / 2,
            self.window.MENU_BUTTON_WIDTH, self.window.MENU_BUTTON_HEIGHT
        )
        quit_button = pygame.Rect(
            self.window.SCREEN_WIDTH / 2 - self.window.MENU_BUTTON_WIDTH / 2,
            370 - self.window.MENU_BUTTON_HEIGHT / 2,
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
                if continue_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "continue"
                elif restart_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "restart"
                elif quit_button.collidepoint((mouse_x, mouse_y)):
                    self.state = "false"

        return self.state

    def start_menu(self, state):
        # Draw the menu and check for selection
        self.draw()
        self.state = state
        self.state = self.selection()
        return self.state
