import pygame
from generator import Generator

class GeneratorManager:
    def __init__(self, app):
        self.generators = []
        self.app = app
        self.cobblestone = pygame.image.load("assets/textures/cobblestone.png")
        self.breaking_overlays = [pygame.image.load("assets/textures/breaking overlays/1.png").convert_alpha(), pygame.image.load("assets/textures/breaking overlays/2.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/3.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/4.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/5.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/6.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/7.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/8.png").convert_alpha(),pygame.image.load("assets/textures/breaking overlays/9.png").convert_alpha()]
        # make the breaking overlays slightly transparent
        for each in self.breaking_overlays:
            each.fill((255, 255, 255, 170), None, pygame.BLEND_RGBA_MULT)


    def add_generator(self, pos):
        self.generators.append(Generator(pos, self.app.screen, self.cobblestone, self.breaking_overlays))


    def draw(self):
        
        for generator in self.generators:
            if not generator.block_broken:
                generator.block.draw()

    def update(self):

        for generator in self.generators:
            generator.dt = self.app.dt
            generator.update()

    
    def handle_events(self, events):
        for event in events:
            # check if a block was clicked for manual mining
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self.app.game.paused:
                    for generator in self.generators:
                        if not generator.block_broken:
                            if generator.block.block_rect.collidepoint(self.app.mouse_pos):
                                generator.block.hp -= self.app.game.pickaxe.damage
                                generator.block.update()
                                if 0 >= generator.block.hp:
                                    generator.break_block()