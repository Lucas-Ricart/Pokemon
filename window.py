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

        # Text font
        self.font = pygame.font.Font("assets/pokemon-font.ttf", 60)

        # Game window setup
        self.screen_width = 854
        self.screen_height = 480
        pygame.display.set_caption("Pokemon")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Menu background
        self.MENU_BACKGROUND = pygame.image.load("assets/menu-background.png")
        self.MENU_BACKGROUND = pygame.transform.scale(
            self.MENU_BACKGROUND, (self.screen_width, self.screen_height)
        )
        
        # Menu button dimensions
        self.MENU_BUTTON_WIDTH = 200
        self.MENU_BUTTON_HEIGHT = 60

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
        self.draw_center_text(text, self.font, self.WHITE, x, y)

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
