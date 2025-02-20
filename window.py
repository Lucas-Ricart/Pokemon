import pygame
import pygame.freetype


class Window:
    def __init__(self):
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.PURPLE = (54, 45, 92)
        self.PINK = (162, 92, 126)
        self.DARK_GREY = (72, 72, 72)
        self.LIGHT_GREY = (184, 184, 184)
        self.BLUE = (72, 144, 248)
        self.GREEN = (26, 186, 115)
        self.LIGHT_ORANGE = (255, 179, 0)
        self.DARK_ORANGE = (255, 103, 36)

        # Text font
        self.TEXT_FONT = pygame.font.Font("assets/text-font.ttf", 50)
        self.SHADOW_TEXT_FONT = pygame.font.Font("assets/text-font.ttf", 51)
        self.NUMBER_FONT = pygame.font.Font("assets/number-font.ttf", 20)
        self.SHADOW_NUMBER_FONT = pygame.font.Font(
            "assets/number-font.ttf", 23)

        # Game window setup
        self.SCREEN_WIDTH = 768
        self.SCREEN_HEIGHT = 450
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Menu background
        self.MENU_BACKGROUND = pygame.image.load("assets/menu-background.png")
        self.MENU_BACKGROUND = pygame.transform.scale(
            self.MENU_BACKGROUND, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )

        # Menu button dimensions
        self.MENU_BUTTON_WIDTH = 200
        self.MENU_BUTTON_HEIGHT = 60

        # Fight dimensions
        self.arena_height = 324
        self.text_box_height = 126

        # fight decor
        # Fight Background
        self.FIGHT_BACKGROUND = pygame.image.load(
            "assets/fight-background.png")
        self.FIGHT_BACKGROUND = pygame.transform.scale(
            self.FIGHT_BACKGROUND, (self.SCREEN_WIDTH, self.arena_height))
        # Fight text box
        self.TEXT_BOX_BACKGROUND = pygame.image.load("assets/text-box.png")
        self.TEXT_BOX_BACKGROUND = pygame.transform.scale(
            self.TEXT_BOX_BACKGROUND, (self.SCREEN_WIDTH, self.text_box_height))
        # Fight grounds
        self.MY_GROUND = pygame.image.load("assets/my-ground.png")
        self.MY_GROUND = pygame.transform.scale(
            self.MY_GROUND, (self.SCREEN_WIDTH, self.arena_height/4)
        )
        self.ENEMY_GROUND = pygame.image.load("assets/enemy-ground.png")
        self.ENEMY_GROUND = pygame.transform.scale(
            self.ENEMY_GROUND, (self.SCREEN_WIDTH /
                                2, self.arena_height/2)
        )
        # Fight info bars
        self.MY_BAR = pygame.image.load("assets/my-bar.png")
        self.MY_BAR = pygame.transform.scale(
            self.MY_BAR, (self.SCREEN_WIDTH/2+3, self.arena_height/3 + 7))
        self.ENEMY_BAR = pygame.image.load("assets/enemy-bar.png")
        self.ENEMY_BAR = pygame.transform.scale(
            self.ENEMY_BAR, (self.SCREEN_WIDTH/2 - 25, self.arena_height/4 + 10))

    def draw_menu_button(self, text, x, y):
        """
        Draws a menu button with hover effects and centered text.

        Args:
            text (str): The text to display on the button.
            x (int): X-coordinate of the button's center.
            y (int): Y-coordinate of the button's center.
        """
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Define the button as a rectangle
        button = pygame.Rect(
            x - self.MENU_BUTTON_WIDTH / 2,
            y - self.MENU_BUTTON_HEIGHT / 2 + 1.5,
            self.MENU_BUTTON_WIDTH,
            self.MENU_BUTTON_HEIGHT
        )

        # Change button color on hover
        if button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(self.screen, self.PURPLE, button)
            pygame.draw.rect(self.screen, self.PINK, button, 3)
        else:
            pygame.draw.rect(self.screen, self.RED, button)
            pygame.draw.rect(self.screen, self.BLACK, button, 3)

        # Draw the button text centered
        self.draw_center_text(text, self.TEXT_FONT, self.WHITE, x, y)

    def draw_fight_decor(self):
        self.screen.blit(self.FIGHT_BACKGROUND, (0, 0))
        self.screen.blit(self.MY_GROUND,
                         self.MY_GROUND.get_rect(bottomright=(574, 344)))
        self.screen.blit(self.ENEMY_GROUND, self.ENEMY_GROUND.get_rect(
            bottomright=(self.SCREEN_WIDTH, 265)))
        self.screen.blit(self.TEXT_BOX_BACKGROUND,
                         (0, self.SCREEN_HEIGHT - self.text_box_height))
        self.screen.blit(self.ENEMY_BAR, (0, self.arena_height/8))
        self.screen.blit(self.MY_BAR, self.MY_BAR.get_rect(
            bottomright=(self.SCREEN_WIDTH, self.arena_height - 10)))

    def draw_topleft_text(self, text, font, text_col, x, y):
        """
        Draws text at the top-left position.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for text styling.
            text_col (tuple): Color of the text.
            x (int): X-coordinate.
            y (int): Y-coordinate.
        """
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw_topright_text(self, text, font, text_col, x, y):
        """
        Draws text at the top-right position.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for text styling.
            text_col (tuple): Color of the text.
            x (int): X-coordinate.
            y (int): Y-coordinate.
        """
        img = font.render(text, True, text_col)
        rect = img.get_rect(topright=(x, y))
        self.screen.blit(img, rect)

    def draw_bottomright_text(self, text, font, text_col, x, y):
        """
        Draws text at the bottom-right position.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for text styling.
            text_col (tuple): Color of the text.
            x (int): X-coordinate.
            y (int): Y-coordinate.
        """
        img = font.render(text, True, text_col)
        rect = img.get_rect(bottomright=(x, y))
        self.screen.blit(img, rect)

    def draw_bottomleft_text(self, text, font, text_col, x, y):
        """
        Draws text at the bottom-left position.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for text styling.
            text_col (tuple): Color of the text.
            x (int): X-coordinate.
            y (int): Y-coordinate.
        """
        img = font.render(text, True, text_col)
        rect = img.get_rect(bottomleft=(x, y))
        self.screen.blit(img, rect)

    def draw_center_text(self, text, font, text_col, x, y):
        """
        Draws text at the center position.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for text styling.
            text_col (tuple): Color of the text.
            x (int): X-coordinate.
            y (int): Y-coordinate.
        """
        img = font.render(text, True, text_col)
        rect = img.get_rect(center=(x, y))
        self.screen.blit(img, rect)

    def draw_pokemon(self, key):
        pokemon = pygame.image.load(f"assets/sprites/{key}.png")
        self.screen.blit(pokemon, (100, 0))

    def draw_my_pokemon(self, key):
        my_pokemon = pygame.image.load(f"assets/backsprites/{key}.png")
        self.screen.blit(my_pokemon, (500, 0))

    