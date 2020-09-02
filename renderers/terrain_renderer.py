from renderers.base_renderer import BaseRenderer
from renderers.character_renderer import CharacterRenderer
from renderers.scenery_renderer import SceneryRenderer
from data.objects.tile import Tile
from data.metadata.point import Point
import os
import pygame


class TerrainRenderer(BaseRenderer):
    BASE_TERRAIN = [[0 for x in range(0, 15)] for y in range(0, 15)]

    TILE_WIDTH_OFFSET = int(Tile.BASE_WIDTH / 2)
    TILE_HEIGHT_OFFSET = int(Tile.BASE_HEIGHT / 4)

    def __init__(self, screen):
        super().__init__(screen)

        self.LIGHT_TILE = Tile.light_tile().sprite()
        self.DARK_TILE = Tile.dark_tile().sprite()
        self.DROP_SHADOW = Tile.drop_shadow().sprite()
        self.HIGHLIGHT = Tile.highlight().sprite()

        self.last_selected = Point(0, 0)

    def render(self, data):
        new_click = data.window.attributes.click
        click_handled = False

        for y in range(0, len(data.terrain)):
            for x in range(0, len(data.terrain[y])):
                tile_pos = self.calculate_iso_tile_position(x, y)
                tile = data.terrain[y][x]
                window_data = data.window

                if y == len(data.terrain) - 1 or x == len(data.terrain[y]) - 1:
                    self.render_drop_shadow(tile_pos)

                tile_type = self.LIGHT_TILE if ( x + y ) % 2 == 0 else self.DARK_TILE

                self.screen.blit(tile_type, tile_pos)

                if self.tile_is_hovered(x, y, window_data):
                    self.screen.blit(self.HIGHLIGHT, tile_pos)

                tile_clicked = self.hovered_tile_is_clicked(x, y, window_data)
                # Set click_handled if a tile is clicked
                if tile_clicked:
                    click_handled = True

                # Handle the tile click, or render the menu for selected tile
                if (data.TILE_MENU_OPEN and tile.IS_SELECTED) or tile_clicked:
                    self.set_data_tile_clicked(x, y, data)
                    self.last_selected = Point(x, y)
                    data.TILE_MENU_OPEN = True
                    self.screen.blit(self.HIGHLIGHT, tile_pos)

                # Render some debug text to the screen
                tile_pos_text = self.DEBUG_FONT.render("({}, {})".format(x, y), True, (0, 0, 255))
                self.screen.blit(tile_pos_text, TerrainRenderer.tile_debug_text_pos(*tile_pos))

                if tile:
                        if tile.TYPE == 'character':
                            CharacterRenderer(self.screen).render(tile, x, y)
                        elif tile.TYPE == 'scenery':
                            SceneryRenderer(self.screen).render(tile, x, y)

        if new_click and click_handled:
            window_data.attributes.click = False

    def render_drop_shadow(self, tile_pos):
        drop_shadow_pos = self.calculate_iso_tile_drop_shadow_position(*tile_pos)
        self.screen.blit(self.DROP_SHADOW, drop_shadow_pos)

    def calculate_iso_tile_position(self, x, y):
        x_pos, y_pos = self.calculate_absolute_coords(x, y)

        return (int(x_pos), int(y_pos))

    def calculate_iso_tile_drop_shadow_position(self, x, y):
        vertical_offset = Tile.BASE_HEIGHT - 24

        return (x, y + vertical_offset)

    def tile_is_hovered(self, x, y, data):
        x_pos, y_pos = self.calculate_absolute_coords(x, y)

        tile_center_x, tile_center_y = (x_pos + self.TILE_WIDTH_OFFSET, y_pos + self.TILE_HEIGHT_OFFSET)

        dx = abs(data.attributes.mouse_x_pos - tile_center_x)
        dy = abs(data.attributes.mouse_y_pos - tile_center_y)

        if (dx / self.TILE_WIDTH_OFFSET) + (dy / self.TILE_HEIGHT_OFFSET) < 1:
            return True

        return False

    def hovered_tile_is_clicked(self, x, y, data):
        return self.tile_is_hovered(x, y, data) and data.attributes.click

    def calculate_absolute_coords(self, x, y):
        x_pos = ( x - y ) * self.TILE_WIDTH_OFFSET + self.SCREEN_CENTER_POS[0] - self.TILE_WIDTH_OFFSET
        y_pos = ( x + y ) * self.TILE_HEIGHT_OFFSET

        return (x_pos, y_pos)

    def set_data_tile_clicked(self, x, y, data):
        data.terrain[self.last_selected.y][self.last_selected.x].IS_SELECTED = False
        data.terrain[y][x].IS_SELECTED = True
        data.TILE_MENU_OPEN = True
        data.TILE_CLICKED_POSITION = Point(x, y)
        data.TILE_CLICKED_ENTITY = data.terrain[y][x]

    @classmethod
    def tile_debug_text_pos(cls, x, y):
        return (x + 12, y + 12)