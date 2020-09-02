import pygame


class BaseRenderer:

    def __init__(self, screen):
        self.DEBUG_FONT = pygame.font.SysFont(None, 12)
        self.SCREEN_CENTER_POS = (int(screen.get_width() / 2), int(screen.get_height() / 2))
        self.screen = screen
    