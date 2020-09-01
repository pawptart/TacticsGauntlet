import os
from data.objects.entity import Entity

class Menu(Entity):
    SPRITE_BASE_WIDTH = 16
    SPRITE_BASE_HEIGHT = 16

    FONT_SIZE = 20
    FONT_COLOR = (25, 25, 25)
    FONT_PADDING = 10

    def __init__(self, name, game, is_corner=False, is_side=False):
        super().__init__(game)

        self.name = name
        self.FONT = game.font.SysFont(None, self.FONT_SIZE)
        self.IS_CORNER = is_corner
        self.IS_SIDE = is_side

    def sprite(self):
        return self.game.image.load(Menu.sprite_path(self.name))

    @classmethod
    def character_menu(cls, game):
        return Menu.build_menu(10, 6, game)
    
    @classmethod
    def build_menu(cls, tile_size_x, tile_size_y, game):
        menu_tiles = []

        for y in range(0, tile_size_y):
            row = []

            for x in range(0, tile_size_x):
                if x in [0, tile_size_x - 1] and y in [0, tile_size_y - 1]:
                    row.append(Menu.corner_tile(game))
                elif x in [0, tile_size_x - 1] or y in [0, tile_size_y - 1]:
                    row.append(Menu.side_tile(game))
                else:
                    row.append(Menu.fill_tile(game))

            menu_tiles.append(row)

        return menu_tiles

    @classmethod
    def sprite_path(cls, name):
        return os.path.join('assets', 'static', name + '.png')
    
    @classmethod
    def corner_tile(cls, game):
        return Menu('menu_corner', game, is_corner=True)

    @classmethod
    def side_tile(cls, game):
        return Menu('menu_side', game, is_side=True)

    @classmethod
    def fill_tile(cls, game):
        return Menu('menu_fill', game)