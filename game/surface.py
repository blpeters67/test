import pygame

class Surface:
    def __init__(self, surface, pos):
        self.surface = surface
        self.pos = pos
        self.color_palette = self.get_color_palette(self.surface)

    def get_color_palette(surface, exclude):
        array = pygame.PixelArray(surface)
        colors = {tuple(surface.unmap_rgb(mapped_color)) for row in array for mapped_color in row}

        if exclude:
            return [color for color in colors if color not in exclude]

        return list(colors)