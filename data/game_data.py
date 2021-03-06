from data.metadata.window import Window
from data.objects.terrain import Terrain
from data.metadata.point import Point

class GameData:
    def __init__(self):
        self.terrain = Terrain().populate_terrain()
        self.window = Window()

        self.TILE_MENU_OPEN = False
        self.TILE_CLICKED_POSITION = None
        self.TILE_CLICKED_ENTITY = None