import os
import pygame
from data.game_data import GameData
from data.objects.tile import Tile
from renderers.terrain_renderer import TerrainRenderer
from renderers.character_renderer import CharacterRenderer
from renderers.menu_renderer import MenuRenderer
from renderers.debug_renderer import DebugRenderer

class Game:
    VERSION = open('VERSION').read()

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set the game window options
        Game.set_window_options()
        
        # Create an 800x600 window
        screen = pygame.display.set_mode((800, 600))
        screen_center = (int(screen.get_width() / 2), int(screen.get_height() / 2))
        
        # Load the renderers
        terrain = TerrainRenderer(screen, pygame)
        menu = MenuRenderer(screen, pygame)
        debug = DebugRenderer(screen, pygame)

        renderers = [terrain, debug]

        # Seed the game data
        data = GameData(pygame)

        # Set a flag to run the game
        running = True
        
        # Execute main game loop while running
        while running:

            Game.set_default_data_window_attributes(data)

            # Grab events from the event queue
            for event in pygame.event.get():
                # Exit the game loop if QUIT signal received
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    data.window.attributes.click = True
            
            Game.set_data_window_values(data, screen_center)
            Game.render(renderers, screen, data)

    @classmethod
    def set_window_options(cls):
        icon_path = os.path.join('assets/logos/icon.png')
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
        pygame.display.set_caption("TacticsGauntlet {}".format(Game.VERSION))

    @classmethod
    def render(cls, renderers, screen, data):
        # Fill background with white
        screen.fill((255, 255, 255))

        # Call renderers in order
        for renderer in renderers:
            renderer.render(data)

        # Draw to screen
        pygame.display.update()

    @classmethod
    def set_default_data_window_attributes(cls, data):
        data.window.attributes.click = False

    @classmethod
    def set_data_window_values(cls, data, screen_center):
        mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()

        data.window.attributes.mouse_x_pos = mouse_x_pos
        data.window.attributes.mouse_y_pos = mouse_y_pos

     
# Run the game if started from CLI
if __name__ == "__main__":
    # Start the game
    Game()