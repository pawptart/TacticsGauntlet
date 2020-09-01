from renderers.base_renderer import BaseRenderer
from data.objects.menu import Menu
import os


class MenuRenderer(BaseRenderer):
    def __init__(self, screen, game):
        super().__init__(screen, game)

    def render(self, data):
        if data.TILE_MENU_OPEN:
            # TODO: Change to a position next to the tile later
            menu_pos = (0, 0)
            menu_text_offset = (5, 5)
            menu_tiles = Menu.character_menu(self.game)

            menu_tile_width = Menu.SPRITE_BASE_WIDTH
            menu_tile_height = Menu.SPRITE_BASE_HEIGHT

            max_y = len(menu_tiles)
            max_x = len(menu_tiles[0])

            for y in range(0, max_y):
                for x in range(0, max_x):
                    tile = menu_tiles[y][x]
                    tile_rotation = MenuRenderer.calculate_tile_rotation(x, y, max_x, max_y)

                    if tile.IS_CORNER or tile.IS_SIDE:
                        sprite = self.game.transform.rotate(tile.sprite(), tile_rotation)
                    else:
                        sprite = tile.sprite()

                    x_offset, y_offset = (x * menu_tile_width, y * menu_tile_height)
                    tile_pos = (menu_pos[0] + x_offset, menu_pos[1] + y_offset)

                    self.screen.blit(sprite, tile_pos)

            entity_actions = data.TILE_CLICKED_ENTITY.ACTIONS

            for y in range(0, len(entity_actions)):
                text_pos = (Menu.FONT_PADDING, y * Menu.FONT_SIZE + Menu.FONT_PADDING)
                action = entity_actions[y].capitalize()

                action_text = Menu(None, self.game).FONT.render(action, True, Menu.FONT_COLOR)
                self.screen.blit(action_text, text_pos)

    @classmethod
    def calculate_tile_rotation(cls, x, y, max_x, max_y):
        index_max_x = max_x - 1
        index_max_y = max_y - 1

        # Corner checks
        if x in [0, index_max_x] and y in [0, index_max_y]:
            if x == 0 and y == index_max_y:
                return 90
            elif x == index_max_x and y == index_max_y:
                return 180
            elif x == index_max_x and y == 0:
                return 270

        # Side checks
        else:
            if x == 0:
                return 90
            elif y == index_max_y:
                return 180
            elif x == index_max_x:
                return 270

        # Don't need to account for top row of side sprites
        return 0