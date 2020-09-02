import os
import pygame
from data.objects.entity import Entity


class Tile(Entity):
    BASE_WIDTH = 64
    BASE_HEIGHT = 64

    TYPE = 'tile'

    def __init__(self, name):
        super().__init__()

        self.name = name
    
    def sprite(self):
        return pygame.image.load(Tile.sprite_path(self.name))

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'tiles', name + '.png')

    @classmethod
    def light_tile(cls):
        return Tile('light')

    @classmethod
    def dark_tile(cls):
        return Tile('dark')

    @classmethod
    def highlight(cls):
        return Tile('highlight')

    @classmethod
    def drop_shadow(cls):
        return Tile('drop_shadow')