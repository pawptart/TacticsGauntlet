import os
import pygame


class Entity:

    TYPE = None

    def __init__(self, game, sprite_name=''):
        self.sprite_name = sprite_name
        self.game = game

    def sprite(self):
        return self.game.image.load(Entity.sprite_path(self.sprite_name))

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'shared', name + '.png')

    @classmethod
    def drop_shadow(cls, game):
        return Entity(game, 'drop_shadow')