import pygame
from window import Window


class Fight:
    def __init__(self):
        self.window = Window()

    # Draw lv
    def draw_enemy_lv(self):
        # Draw enemy lv
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 247, 92)
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.DARK_GREY, 245, 90)

    def draw_my_lv(self):
        # Draw my lv
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 701, 251)
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.DARK_GREY, 699, 249)

    def draw_my_hp(self):
        # Draw my hp
        # Draw hp max
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 673, 299)
        self.window.draw_bottomleft_text(
            "100", self.window.NUMBER_FONT, self.window.DARK_GREY, 671, 297)
        # Draw current hp
        self.window.draw_bottomright_text(
            "83", self.window.NUMBER_FONT, self.window.LIGHT_GREY, 649, 299)
        self.window.draw_bottomright_text(
            "83", self.window.NUMBER_FONT, self.window.DARK_GREY, 647, 297)

    # Draw hp bar
    def draw_enemy_bar(self):
        # Draw enemy hp bar
        pygame.draw.line(self.window.screen, self.window.LIGHT_ORANGE,
                         (148, 106), (288, 106), width=8)

    def draw_my_bar(self):
        # Draw my hp bar
        pygame.draw.line(self.window.screen, self.window.DARK_ORANGE,
                         (599, 264), (743, 264), width=7)

    def draw_xp_bar(self):
        # Draw xp bar
        pygame.draw.line(self.window.screen, self.window.BLUE,
                         (454, 304), (743, 304), width=5)

    # Draw names
    def draw_enemy_name(self):
        # Draw enemy name
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 16, 96)
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.TEXT_FONT, self.window.DARK_GREY, 14, 94)

    def draw_my_name(self):
        # Draw my name
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.SHADOW_TEXT_FONT, self.window.LIGHT_GREY, 447, 258)
        self.window.draw_bottomleft_text(
            "Dragapult", self.window.TEXT_FONT, self.window.DARK_GREY, 445, 256)

    def draw_fight(self, test):
        self.window.draw_fight_decor()
        self.draw_enemy_lv()
        self.draw_enemy_bar()
        self.draw_enemy_name()
        self.draw_my_lv()
        self.draw_my_bar()
        self.draw_my_name()
        self.draw_my_hp()
        self.draw_xp_bar()
        mouse_x, mouse_y = "lol", "lol"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
        return (mouse_x, mouse_y)
