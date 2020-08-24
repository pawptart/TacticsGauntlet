import pygame


class BaseRenderer:

    def __init__(self, screen, game):
        self.DEBUG_FONT = game.font.SysFont(None, 12)
        self.SCREEN_CENTER_POS = (int(screen.get_width() / 2), int(screen.get_height() / 2))
        self.screen = screen
        self.game = game
    