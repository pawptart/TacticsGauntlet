from data.objects.terrain import Terrain

class GameData:
    def __init__(self, game):
        self.game = game

        self.terrain = Terrain(game).populate_terrain()
