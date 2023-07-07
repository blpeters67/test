import pygame
class SFXPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.button_hovered = pygame.mixer.Sound('assets/sfx/button hovered.mp3')
        self.button_hovered.set_volume(0.1)