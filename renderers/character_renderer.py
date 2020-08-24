from renderers.base_renderer import BaseRenderer
from data.objects.character import Character
from data.objects.tile import Tile
import os


class CharacterRenderer(BaseRenderer):
    def __init__(self, screen, game):
        super().__init__(screen, game)

    def render(self, data, x, y):
        character = Character(data.name, self.game, should_walk=True)

        drop_shadow = Character.drop_shadow(self.game)
        character_pos = self.calculate_iso_character_position(x, y)
        drop_shadow_pos = self.calculate_iso_drop_shadow_position(*character_pos)

        self.screen.blit(drop_shadow.sprite(), drop_shadow_pos)
        self.screen.blit(character.sprite(), character_pos)

    def calculate_iso_character_position(self, x, y):
        character_width_offset, character_height_offset = self.calculate_iso_character_position_offset(x, y)
        tile_width_offset = Tile.BASE_WIDTH / 2
        tile_height_offset = Tile.BASE_HEIGHT / 4

        x_pos = ( x - y ) * tile_width_offset + self.SCREEN_CENTER_POS[0] - tile_width_offset + character_width_offset
        y_pos = ( x + y ) * tile_height_offset - character_height_offset

        return (int(x_pos), int(y_pos))

    def calculate_iso_character_position_offset(self, x, y):
        # Center the character horizontally
        width_offset = (Tile.BASE_WIDTH - Character.BASE_WIDTH) / 2

        # Place the bottom of the character sprite in the middle of the top of the tile
        height_offset = Character.BASE_HEIGHT - (Tile.BASE_HEIGHT / 2.5)

        return (width_offset, height_offset)

    def calculate_iso_drop_shadow_position(self, x, y):
        return (x, y + 48)