from renderers.base_renderer import BaseRenderer
from renderers.character_renderer import CharacterRenderer
from renderers.scenery_renderer import SceneryRenderer
from data.objects.tile import Tile
import os


class TerrainRenderer(BaseRenderer):
    BASE_TERRAIN = [[0 for x in range(0, 15)] for y in range(0, 15)]

    def __init__(self, screen, game):
        super().__init__(screen, game)

        self.light_tile = game.image.load(Tile.sprite_path('light'))
        self.dark_tile = game.image.load(Tile.sprite_path('dark'))
        self.drop_shadow = game.image.load(Tile.sprite_path('drop_shadow'))

    def render(self, data):
        for y in range(0, len(data.terrain)):
            for x in range(0, len(data.terrain[y])):
                tile_pos = self.calculate_iso_tile_position(x, y)
                tile_data = data.terrain[y][x]

                if y == len(data.terrain) - 1 or x == len(data.terrain[y]) - 1:
                    self.render_drop_shadow(tile_pos)

                if ( x + y ) % 2 == 0:
                    tile = Tile.light_tile(self.game).sprite()
                else:
                    tile = Tile.dark_tile(self.game).sprite()

                self.screen.blit(tile, tile_pos)

                # Render some debug text to the screen
                tile_pos_text = self.DEBUG_FONT.render("({}, {})".format(x, y), True, (0, 0, 255))
                self.screen.blit(tile_pos_text, TerrainRenderer.tile_debug_text_pos(*tile_pos))

                if tile_data:
                        if tile_data.TYPE == 'character':
                            CharacterRenderer(self.screen, self.game).render(tile_data, x, y)
                        elif tile_data.TYPE == 'scenery':
                            SceneryRenderer(self.screen, self.game).render(tile_data, x, y)
                

    def render_drop_shadow(self, tile_pos):
        drop_shadow_pos = self.calculate_iso_tile_drop_shadow_position(*tile_pos)
        self.screen.blit(self.drop_shadow, drop_shadow_pos)

    def calculate_iso_tile_position(self, x, y):
        tile_width_offset = Tile.BASE_WIDTH / 2
        tile_height_offset = Tile.BASE_HEIGHT / 4

        x_pos = ( x - y ) * tile_width_offset + self.SCREEN_CENTER_POS[0] - tile_width_offset
        y_pos = ( x + y ) * tile_height_offset

        return (int(x_pos), int(y_pos))

    def calculate_iso_tile_drop_shadow_position(self, x, y):
        vertical_offset = Tile.BASE_HEIGHT - 24

        return (x, y + vertical_offset)

    @classmethod
    def tile_debug_text_pos(cls, x, y):
        return (x + 12, y + 12)