from renderers.base_renderer import BaseRenderer
import pygame


class DebugRenderer(BaseRenderer):
    # TODO: Break this out into a config
    DEBUG_ENABLED = True
    DEBUG_FONT_COLOR = (0, 0, 255)

    def __init__(self, screen, game):
        super().__init__(screen, game)

    def render(self, data):
        if not DebugRenderer.DEBUG_ENABLED:
            return

        self.data = data
        self.render_mouse_pos()

    def render_mouse_pos(self):
        mouse_pos = self.game.mouse.get_pos()
        mouse_pos_text = self.DEBUG_FONT.render("({}, {})".format(*mouse_pos), True, self.DEBUG_FONT_COLOR)
        self.screen.blit(mouse_pos_text, mouse_pos)
