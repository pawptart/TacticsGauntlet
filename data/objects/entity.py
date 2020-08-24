import os
import pygame


class Entity:
    def __init__(self, game, entity_type=''):
        self.type = entity_type
        self.game = game

    def sprite(self):
        return self.game.image.load(Entity.sprite_path(self.type))

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'shared', name + '.png')

    @classmethod
    def drop_shadow(cls, game):
        return Entity(game, entity_type='drop_shadow')