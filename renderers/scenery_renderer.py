from renderers.base_renderer import BaseRenderer
from data.objects.scenery import Scenery
from data.objects.tile import Tile
import os
import pygame


class SceneryRenderer(BaseRenderer):
    def __init__(self, screen):
        super().__init__(screen)

    def render(self, data, x, y):
        scenery = Scenery(data.name)
        scenery_pos = self.calculate_iso_scenery_position(x, y)

        if scenery.needs_drop_shadow:
            drop_shadow = Scenery.drop_shadow()
            drop_shadow_pos = self.calculate_iso_drop_shadow_position(*scenery_pos)
            self.screen.blit(drop_shadow.sprite(), drop_shadow_pos)

        self.screen.blit(scenery.sprite(), scenery_pos)

    def calculate_iso_scenery_position(self, x, y):
        scenery_width_offset, scenery_height_offset = self.calculate_iso_scenery_position_offset(x, y)
        tile_width_offset = Tile.BASE_WIDTH / 2
        tile_height_offset = Tile.BASE_HEIGHT / 4

        x_pos = ( x - y ) * tile_width_offset + self.SCREEN_CENTER_POS[0] - tile_width_offset + scenery_width_offset
        y_pos = ( x + y ) * tile_height_offset - scenery_height_offset

        return (int(x_pos), int(y_pos))

    def calculate_iso_scenery_position_offset(self, x, y):
        # Center the scenery horizontally
        width_offset = (Tile.BASE_WIDTH - Scenery.BASE_WIDTH) / 2

        # Place the bottom of the scenery sprite in the middle of the top of the tile
        height_offset = Scenery.BASE_HEIGHT - (Tile.BASE_HEIGHT / 2.5)

        return (width_offset, height_offset)

    def calculate_iso_drop_shadow_position(self, x, y):
        return (x, y + 48)