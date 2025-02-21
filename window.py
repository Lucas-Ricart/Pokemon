import pygame
import pygame.freetype

pygame.init()  # Initialize Pygame
pygame.font.init()  # Initialize the font module


class Window:
    def __init__(self):
        """Initializes the Window class with colors, fonts, screen settings, and assets."""
        # Define colors
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

        # Fonts for text rendering
        self.TEXT_FONT = pygame.font.Font("assets/text-font.ttf", 50)
        self.SHADOW_TEXT_FONT = pygame.font.Font("assets/text-font.ttf", 51)
        self.NUMBER_FONT = pygame.font.Font("assets/number-font.ttf", 20)
        self.SHADOW_NUMBER_FONT = pygame.font.Font("assets/number-font.ttf", 23)

        # Game window setup
        self.SCREEN_WIDTH = 768
        self.SCREEN_HEIGHT = 450
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Menu background image
        self.MENU_BACKGROUND = pygame.image.load("assets/menu-background.png")
        self.MENU_BACKGROUND = pygame.transform.scale(self.MENU_BACKGROUND, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Menu button dimensions
        self.MENU_BUTTON_WIDTH = 200
        self.MENU_BUTTON_HEIGHT = 60

        # Fight dimensions and decor
        self.ARENA_HEIGHT = 324
        self.TEXTBOX_HEIGHT = 126

        # Fight background and other assets
        self.FIGHT_BACKGROUND = pygame.image.load("assets/fight-background.png")
        self.FIGHT_BACKGROUND = pygame.transform.scale(self.FIGHT_BACKGROUND, (self.SCREEN_WIDTH, self.ARENA_HEIGHT))
        self.TEXT_BOX_BACKGROUND = pygame.image.load("assets/text-box.png")
        self.TEXT_BOX_BACKGROUND = pygame.transform.scale(self.TEXT_BOX_BACKGROUND, (self.SCREEN_WIDTH - self.MENU_BUTTON_WIDTH, self.TEXTBOX_HEIGHT))

        # Ground assets for fight scene
        self.MY_GROUND = pygame.image.load("assets/my-ground.png")
        self.MY_GROUND = pygame.transform.scale(self.MY_GROUND, (self.SCREEN_WIDTH, self.ARENA_HEIGHT / 4))
        self.ENEMY_GROUND = pygame.image.load("assets/enemy-ground.png")
        self.ENEMY_GROUND = pygame.transform.scale(self.ENEMY_GROUND, (self.SCREEN_WIDTH / 2, self.ARENA_HEIGHT / 2))

        # Fight info bars
        self.MY_BAR = pygame.image.load("assets/my-bar.png")
        self.MY_BAR = pygame.transform.scale(self.MY_BAR, (self.SCREEN_WIDTH / 2 + 3, self.ARENA_HEIGHT / 3 + 7))
        self.ENEMY_BAR = pygame.image.load("assets/enemy-bar.png")
        self.ENEMY_BAR = pygame.transform.scale(self.ENEMY_BAR, (self.SCREEN_WIDTH / 2 - 25, self.ARENA_HEIGHT / 4 + 10))

        # Sprite dimensions
        self.SPRITE_WIDTH = 96
        self.SPRITE_HEIGHT = 96

    def draw_menu_button(self, text, x, y):
        """
        Draws a menu button with hover effects and centered text.

        Args:
            text (str): The text to display on the button.
            x (int): X-coordinate of the button's center.
            y (int): Y-coordinate of the button's center.
        """
        # Get mouse position for hover effect
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Define the button as a rectangle
        button = pygame.Rect(x - self.MENU_BUTTON_WIDTH / 2, y - self.MENU_BUTTON_HEIGHT / 2 + 1.5, self.MENU_BUTTON_WIDTH, self.MENU_BUTTON_HEIGHT)

        # Change button color on hover
        if button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(self.screen, self.PURPLE, button)
            pygame.draw.rect(self.screen, self.PINK, button, 3)
        else:
            pygame.draw.rect(self.screen, self.RED, button)
            pygame.draw.rect(self.screen, self.BLACK, button, 3)

        # Draw the button text centered
        self.draw_center_text(text, self.TEXT_FONT, self.WHITE, x, y)

    def draw_fight_button(self, text, x, y):
        """
        Draws a fight button with hover effects and centered text.

        Args:
            text (str): The text to display on the button.
            x (int): X-coordinate of the button's center.
            y (int): Y-coordinate of the button's center.
        """
        # Get mouse position for hover effect
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Define the button as a rectangle
        button = pygame.Rect(x, y, self.MENU_BUTTON_WIDTH, self.TEXTBOX_HEIGHT)

        # Change button color on hover
        if button.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(self.screen, self.PURPLE, button)
            pygame.draw.rect(self.screen, self.PINK, button, 3)
        else:
            pygame.draw.rect(self.screen, self.RED, button)
            pygame.draw.rect(self.screen, self.BLACK, button, 3)

        # Draw the button text in top-left position
        self.draw_topleft_text(text, self.TEXT_FONT, self.WHITE, x + 5, y)

    def draw_fight_decor(self):
        """Draws the fight scene's background and decor (grounds, bars, etc.)."""
        self.screen.blit(self.FIGHT_BACKGROUND, (0, 0))
        self.screen.blit(self.MY_GROUND, self.MY_GROUND.get_rect(bottomright=(574, 344)))
        self.screen.blit(self.ENEMY_GROUND, self.ENEMY_GROUND.get_rect(bottomright=(self.SCREEN_WIDTH, 265)))
        self.screen.blit(self.ENEMY_BAR, (0, self.ARENA_HEIGHT / 8))
        self.screen.blit(self.MY_BAR, self.MY_BAR.get_rect(bottomright=(self.SCREEN_WIDTH, self.ARENA_HEIGHT - 10)))

    def draw_center_text(self, text, font, text_col, x, y):
        """
        Draws text at the center of the screen.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for styling the text.
            text_col (tuple): Color of the text.
            x (int): X-coordinate for the text's center.
            y (int): Y-coordinate for the text's center.
        """
        img = font.render(text, True, text_col)
        rect = img.get_rect(center=(x, y))
        self.screen.blit(img, rect)

    def draw_topleft_text(self, text, font, text_col, x, y):
        """
        Draws text in the top-left position.

        Args:
            text (str): The text to display.
            font (pygame.font.Font): Font object for styling the text.
            text_col (tuple): Color of the text.
            x (int): X-coordinate for the text.
            y (int): Y-coordinate for the text.
        """
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw_menu_pokemon(self, key, x, y):
        """Draws a Pokémon sprite at the specified position."""
        sprite = pygame.image.load(f"assets/sprites/{key}.png")
        sprite = pygame.transform.scale(sprite, (self.SPRITE_WIDTH, self.SPRITE_HEIGHT))
        self.screen.blit(sprite, (x, y))

    def draw_my_pokemon(self, key):
        """Draws the user's Pokémon sprite on the left side of the screen."""
        my_pokemon = pygame.image.load(f"assets/backsprites/{key}.png")
        my_pokemon = pygame.transform.scale(my_pokemon, (350, 350))
        self.screen.blit(my_pokemon, (0, 125))

    def draw_enemy_pokemon(self, key):
        """Draws the enemy's Pokémon sprite on the right side of the screen."""
        enemy_pokemon = pygame.image.load(f"assets/sprites/{key}.png")
        enemy_pokemon = pygame.transform.scale(enemy_pokemon, (250, 250))
        self.screen.blit(enemy_pokemon, (455, 8))
