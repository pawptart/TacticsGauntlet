import os
import pygame
import random
from data.objects.entity import Entity


class Scenery(Entity):
    BASE_WIDTH = 32
    BASE_HEIGHT = 64

    SCENERY_OPTIONS = {
        'cactus_1': {
            'needs_drop_shadow': False
        },
        'rock_1': {
            'needs_drop_shadow': False
        },
        'shrub_1': {
            'needs_drop_shadow': False
        },
    }

    TYPE = 'scenery'

    def __init__(self, name):
        super().__init__()

        self.name = name
        self.needs_drop_shadow = self.SCENERY_OPTIONS[name]['needs_drop_shadow']

    def sprite(self):
        return pygame.image.load(Scenery.sprite_path(self.name))

    @classmethod
    def random(cls):
        scenery_choices = [key for key in Scenery.SCENERY_OPTIONS.keys()]
        name = random.choice(scenery_choices)

        return Scenery(name)

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'scenery', name + '.png')

    @classmethod
    def drop_shadow(cls):
        return Entity.drop_shadow()
