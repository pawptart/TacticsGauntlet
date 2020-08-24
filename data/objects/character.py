import math
import os
import pygame
from data.objects.entity import Entity


class Character(Entity):
    BASE_WIDTH = 32
    BASE_HEIGHT = 64

    TYPE = 'character'

    def __init__(self, name, game, should_walk=False, can_walk=True):
        super().__init__(game)

        self.name = name
        self.can_walk = can_walk
        self.walking = should_walk
        self.walk_cycle_time = 1500 # milliseconds
        self.walk_cycle_sprite_count = 4

    def sprite(self):
        character_name = self.name

        if self.can_walk and self.walking:
            sprite_number = self.walk_cycle()
            character_name = character_name + '_walk_{}'.format(str(sprite_number))
        elif self.can_walk:
            character_name = character_name + '_walk_0'

        return self.game.image.load(Character.sprite_path(character_name))

    def walk_cycle(self):
        ticks = self.game.time.get_ticks()
        cycle_position = ticks % (self.walk_cycle_time)
        sprite_count = math.floor((cycle_position / self.walk_cycle_time) * self.walk_cycle_sprite_count)

        return sprite_count if sprite_count % 2 == 1 else 0

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'characters', name + '.png')

    @classmethod
    def player(cls, game):
        return Character('marche', game, should_walk=True)

    @classmethod
    def drop_shadow(cls, game):
        return Entity.drop_shadow(game)