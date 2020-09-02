import math
import os
import pygame
from data.objects.entity import Entity


class Character(Entity):
    BASE_WIDTH = 32
    BASE_HEIGHT = 64

    TYPE = 'character'

    def __init__(self, name, should_walk=False, can_walk=True):
        super().__init__()

        self.name = name
        self.can_walk = can_walk
        self.walking = should_walk
        self.walk_cycle_time = 1500 # milliseconds
        self.walk_cycle_sprite_count = 4

        # TODO: Break these out into configurable stats
        self.MOVE_DISTANCE = 5
        self.ACTIONS = ['move', 'attack', 'item', 'wait']

    def sprite(self):
        character_name = self.name

        if self.can_walk and self.walking:
            sprite_number = self.walk_cycle()
            character_name = character_name + '_walk_{}'.format(str(sprite_number))
        elif self.can_walk:
            character_name = character_name + '_walk_0'

        return pygame.image.load(Character.sprite_path(character_name))

    def walk_cycle(self):
        ticks = pygame.time.get_ticks()
        cycle_position = ticks % (self.walk_cycle_time)
        sprite_count = math.floor((cycle_position / self.walk_cycle_time) * self.walk_cycle_sprite_count)

        return sprite_count if sprite_count % 2 == 1 else 0

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'characters', name + '.png')

    @classmethod
    def player(cls):
        return Character('marche', should_walk=True)

    @classmethod
    def drop_shadow(cls):
        return Entity.drop_shadow()
