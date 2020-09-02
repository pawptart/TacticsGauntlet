import os
import pygame


class Entity:

    TYPE = None
    IS_SELECTED = False
    ACTIONS = []

    def __init__(self, sprite_name=''):
        self.sprite_name = sprite_name

    def sprite(self):
        return pygame.image.load(Entity.sprite_path(self.sprite_name))

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'shared', name + '.png')

    @classmethod
    def drop_shadow(cls):
        return Entity('drop_shadow')