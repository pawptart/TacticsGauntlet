import os
import pygame
from data.objects.entity import Entity


class Tile(Entity):
    BASE_WIDTH = 64
    BASE_HEIGHT = 64

    TYPE = 'tile'

    def __init__(self, name, game):
        super().__init__(game)

        self.name = name
    
    def sprite(self):
        return self.game.image.load(Tile.sprite_path(self.name))

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'tiles', name + '.png')

    @classmethod
    def light_tile(cls, game):
        return Tile('light', game)

    @classmethod
    def dark_tile(cls, game):
        return Tile('dark', game)

    @classmethod
    def highlight(cls, game):
        return Tile('highlight', game)