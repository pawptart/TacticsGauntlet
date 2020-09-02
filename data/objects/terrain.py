import math
import random
import pygame
from data.objects.empty import Empty
from data.objects.team import Team
from data.objects.scenery import Scenery

class Terrain:
    TERRAIN_MIN_SIZE = 15 # tiles
    TERRAIN_MAX_SIZE = 25 # tiles
    SPAWN_DISTANCE = 5 # rows
    TEAM_SIZE = random.randint(5, 10)
    SCENERY_POPULATION_PERCENTAGE = 5 # percent

    def __init__(self):
        self.size = random.randint(self.TERRAIN_MIN_SIZE, self.TERRAIN_MAX_SIZE)
        self.entities = [[Empty() for _x in range(0, self.size)] for _y in range(0, self.size)]

        self.ENEMY_TEAM = Team(self.TEAM_SIZE, is_enemy=True)
        self.PLAYER_TEAM = Team(self.TEAM_SIZE)

    def populate_terrain(self):
        self.populate_characters()
        self.populate_scenery()

        return self.entities

    def populate_characters(self):
        coords_list = Terrain.spawn_coordinates(self.size)

        for team in [self.PLAYER_TEAM, self.ENEMY_TEAM]:
            valid_coords = coords_list['enemy'] if team.is_enemy else coords_list['player']
            for character in team:
                spawn_successful = False

                while not spawn_successful:
                    spawn_x, spawn_y = random.choice(valid_coords)
                    spawn_successful = self.spawn(spawn_x, spawn_y, character)

    def populate_scenery(self):
        for y in range(0, len(self.entities)):
            for x in range(0, len(self.entities[y])):
                if self.entities[y][x] == None:
                    pass

                if random.randint(0, 100) < self.SCENERY_POPULATION_PERCENTAGE:
                    scenery = Scenery.random()
                    self.spawn(x, y, scenery)

    def spawn(self, spawn_x, spawn_y, entity):
        if self.entities[spawn_y][spawn_x].TYPE != None:
            return False
        else:
            self.entities[spawn_y][spawn_x] = entity
            
            return True

    @classmethod
    def max_enemy_y_spawn(cls, size):
        return math.floor(size / Terrain.SPAWN_DISTANCE)

    @classmethod
    def min_player_y_spawn(cls, size):
        return size - math.floor(size / Terrain.SPAWN_DISTANCE) - 1

    @classmethod
    def spawn_coordinates(cls, size):
        enemy_values = Terrain.coords(0, Terrain.max_enemy_y_spawn(size), size)
        player_values = Terrain.coords(Terrain.min_player_y_spawn(size), size - 1, size)

        return {
            'enemy': enemy_values,
            'player': player_values
        }

    @classmethod
    def coords(cls, start_y, end_y, size):
        tuples = []

        for y in range(start_y, end_y + 1):
            tuples.extend([(x, y) for x in range(0, size)])

        return tuples